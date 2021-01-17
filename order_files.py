#A Simple Python Script to Order your Downloads Folder (Maybe It Could Update in the Future with new Features)
import os 

image_extensions = ['.png', '.jpg', '.jpeg', '.gif']
video_extensions = ['.mov', '.mp4', '.m4v']
audio_extensions = ['.mp3', '.m4a', '.wav', '.ogg']
doc_extensions = ['.txt', '.pdf']

docs_folder = '' #Write here the path of your documents folder
images_folder = '' #Write here the path of your images folder
wallpapers_folder = '' #Write here the path of your wallpapers folder
gifs_folder = '' #Write here the path of your gifs folder
videos_folder = '' #Write here the path of your videos folder
audios_folder = '' #Write here the path of your audios folder

def order_files(work_area):
    os.chdir(work_area)
    with os.scandir(work_area) as files:
        for file in files:
            if os.path.isfile(file):
                os.chdir(work_area)
                filename, extension = os.path.splitext(file)
                if extension in doc_extensions:
                    path = f'{docs_folder}\\' + file.name
                elif not file.name.lower().find('wallpaper') == -1:
                    os.rename(file, filename + '.png')
                    path = f'{wallpaper_folder}\\' + file.name
                elif extension in image_extensions[0:-1]:
                    if not extension == '.png':
                        os.rename(file, filename + '.png')
                    path = f'{images_folder}\\' + file.name
                elif extension == '.gif':
                    path = f'{gifs_folder}\\' + file.name
                elif extension in video_extensions:
                    path = f'{videos_folder}\\' + file.name
                elif extension in audio_extensions:
                    path = f'{videos_folder}\\' + file.name                   

                os.rename(file, os.path.join(os.path.expanduser('~'), path))
            elif os.path.isdir(file):
                os.chdir(file)
                with os.scandir(file) as folder:
                    for archive in folder:
                        if os.path.isfile(archive):
                            filename, extension = os.path.splitext(file)
                            if extension in image_extensions[0:-1]:
                                if not extension == '.png':
                                    os.rename(file, filename + '.png')
                                
                                os.rename(archive, file_name)
                            
                    os.chdir(work_area)
                    os.rename(file, f'{images_folder}\\' + file.name)


if __name__ == '__main__':
    work_area = os.path.join(os.path.expanduser('~'), 'downloads')
    order_files(work_area)

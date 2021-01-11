#Maybe you have to change some things because this script is made for my own Downloads Folder

import os 

image_extensions = ['.png', '.jpg', '.jpeg', '.gif']
video_extensions = ['.mov', '.mp4', '.m4v']
audio_extensions = ['.mp3', '.m4a', '.wav', '.ogg']

def order_files(work_area):
    os.chdir(work_area)
    with os.scandir(work_area) as files:
        for file in files:
            if os.path.isfile(file):
                extens = file.name.find('.')
                extension = file.name[extens::]
                if not file.name.lower().find('wallpaper') == -1:
                    file_name = file.name[::extens] + '.png'
                    path = 'Pictures\\Imagenes\\Wallpapers\\' + file_name
                elif extension in image_extensions[::-1]:
                    if not extension == '.png':
                        file_name = file.name[::extens] + '.png'
                    else:
                        file_name = file.name
                    path = 'Pictures\\Imagenes\\' + file_name
                elif extension == '.gif':
                    path = 'Pictures\\Imagenes\\Gifs\\' + file.name
                elif extension in video_extensions:
                    path = 'Pictures\\Videos\\' + file.name
                elif extension in audio_extensions:
                    if not file.name.find('Python Course Leasson') == -1:
                        path = 'Desktop\\Python Course\\Audios\\' + file.name
                    else:
                        path = 'Pictures\\Audios\\' + file.name                   

                os.rename(file, os.path.join(os.path.expanduser('~'), path))

if __name__ == '__main__':
    work_area = os.path.join(os.path.expanduser('~'), 'downloads')
    order_files(work_area)
    work_area = os.path.join(os.path.expanduser('~'), 'downloads\\MyFlow')
    order_files(work_area)

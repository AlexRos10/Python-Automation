import os 

image_extensions = ['.png', '.jpg', '.jpeg', '.gif']
video_extensions = ['.mov', '.mp4', '.m4v']
audio_extensions = ['.mp3', '.m4a', '.wav', '.ogg']
doc_extensions = ['.txt', '.pdf']

def order_files(work_area):
    os.chdir(work_area)
    with os.scandir(work_area) as files:
        for file in files:
            if os.path.isfile(file):
                os.chdir(work_area)
                extens = file.name.find('.')
                extension = file.name[extens::]
                if extension in doc_extensions:
                    path = 'Desktop\\' + file.name
                elif extension == '.xcf':
                    path = 'Documents\\Gimp\\' + file.name
                elif not file.name.lower().find('wallpaper') == -1:
                    file_name = file.name[0:extens] + '.png'
                    print(file.name, file.name[0:extens], file_name)
                    path = 'Pictures\\Galeria\\Wallpapers\\' + file_name
                elif not file.name.lower().find('certificado') == -1 or file.name.lower().find('cert-') != -1:
                    if extension in image_extensions:
                        file_name = file.name[0:extens] + '.png'
                        path = 'Pictures\\Galeria\\Certificados\\' + file_name
                elif extension in image_extensions[0:-1]:
                    if not extension == '.png':
                        file_name = file.name[0:extens] + '.png'
                    else:
                        file_name = file.name
                    path = 'Pictures\\Galeria\\' + file_name
                elif extension == '.gif':
                    path = 'Pictures\\Galeria\\Gifs\\' + file.name
                elif extension in video_extensions:
                    path = 'Pictures\\Videos\\' + file.name
                elif extension in audio_extensions:
                    if not file.name.find('Python Course Leasson') == -1:
                        path = 'Desktop\\Python Course\\Audios\\' + file.name
                    else:
                        path = 'Pictures\\Audios\\' + file.name                   

                os.rename(file, os.path.join(os.path.expanduser('~'), path))
            elif os.path.isdir(file) and file.name != 'MyFlow':
                os.chdir(file)
                with os.scandir(file) as folder:
                    for archive in folder:
                        if os.path.isfile(archive):
                            extens = archive.name.find('.')
                            extension = archive.name[extens::]
                            if extension in image_extensions[0:-1]:
                                if not extension == '.png':
                                    file_name = archive.name[0:extens] + '.png'
                                else:
                                    file_name = archive.name
                                
                                os.rename(archive, file_name)
                            
                    os.chdir('C:\\Users\\Alex Ros\\downloads')
                    os.rename(file, 'C:\\Users\\Alex Ros\\Pictures\\Galeria\\' + file.name)


if __name__ == '__main__':
    work_area = os.path.join(os.path.expanduser('~'), 'downloads')
    order_files(work_area)
    work_area = os.path.join(os.path.expanduser('~'), 'downloads\\MyFlow')
    order_files(work_area)

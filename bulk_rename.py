#A Python Code to rename in bulk files in Windows

import os

class File_Manager(object):
    def __init__(self, work_area):
        os.chdir(work_area)

    def rename_files(self):
        with os.scandir(work_area) as files:
            for file in files:
                source = work_area + '\\' + file.name
                file_name = file.name
                try:
                    new_name = input('Rename: {} \n >>> '.format(file_name))
                    if new_name == 'exit':
                        break
                    if not new_name == 'pass':
                        desti = work_area + '\\' + new_name
                        os.rename(source, desti)
                except Exception as e:
                    print('Invalid Filename')
                    new_name = input('Rename: {} \n >>> '.format(file_name))
                    if new_name == 'exit':
                        break
                    if not new_name == 'pass':
                        desti = work_area + '\\' + new_name
                        os.rename(source, desti)

def selectPath():
    path = input('Enter the path C:\\Users\\Rosar\\ \n >>> ')
    if path == '':
        path = 'Desktop'

    return path

if __name__ == '__main__':
    work_area = os.path.join(os.path.expanduser('~'), selectPath())
    file = File_Manager(work_area)
    file.rename_files()

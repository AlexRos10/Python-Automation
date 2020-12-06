

import os

class Folder_Management(object):
    def __init__(self, work_area):
        try:
            os.chdir(work_area)
        except Exception as e:
            work_area = os.path.join(os.path.expanduser('~'), 'OneDrive\\Desktop')
            os.chdir(work_area)
    
    def create_folders(self, amount = 1):
        amount = amount
        while True:
            try:
                if amount == 1:
                    folder_name = input('Enter the Folder Name\n >>> ')
                    os.mkdir(folder_name)
                    break
                else:
                    for i in range(amount):
                        folder_name = input('Enter the Folder Name\n >>> ')
                        os.makedirs(folder_name)
                        amount -= 1
                    break
            except Exception as e:
                print('Invalid Filname')
                continue

def quantify_folders():
    quant_folders = int(input('How many folders do you wanna create\n >>> '))
    return quant_folders

def selectPath():
    path = input('Enter the path C:\\Users\\Rosar\\ \n >>> ')
    if path == '':
        path = 'Desktop'

    return path
    
if __name__ == '__main__':
    work_area = os.path.join(os.path.expanduser('~'), selectPath())
    folder = Folder_Management(work_area)
    folder.create_folders(quantify_folders())

# Working with files
import os


def show_cwd():
    '''Display current working directory'''
    cwd = os.getcwd()
    print(cwd)


def up_1level():
    '''Go up 1 level'''
    os.chdir("../")


def list_dir(directory):
    '''List files and folders'''
    with os.scandir(directory) as entries:
        for entry in entries:
            print(entry.name)


if __name__ == "__main__":
    show_cwd()
    up_1level()
    show_cwd()
    list_dir("./")

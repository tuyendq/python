# Working with files
# LinkedIn Learning course: Working with Files by Kathryn Hodge
from datetime import datetime
import os
import glob


def format_datetime(timestamp):
    '''Format date time'''
    utc_timestamp = datetime.utcfromtimestamp(timestamp)
    formated_date = utc_timestamp.strftime("%d %b %Y %H %M %S")
    return formated_date


def show_cwd():
    '''Display current working directory'''
    cwd = os.getcwd()
    print(cwd)


def up_1level():
    '''Go up 1 level'''
    os.chdir("../")


def list_all(directory):
    '''List files and folders'''
    with os.scandir(directory) as entries:
        for entry in entries:
            print(entry.name, end='\t')
            info = entry.stat()
            print("Created time: ", format_datetime(info.st_ctime))
            print("Last access time: ", format_datetime(info.st_atime))
            print("Size: ", info.st_size)


def list_dir(directory):
    '''List directories only'''
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_dir():
                print("Directory: ", entry.name)


def list_file(directory):
    '''List files only'''
    with os.scandir(directory) as entries:
        for entry in entries:
            if entry.is_file():
                print("File: ", entry.name)


def list_txt():
    txt_files = glob.glob('*.txt')
    print(txt_files)


def top_down_walk():
    '''Recursively list all files in a directory top down'''
    for dirpath, dirnames, files in os.walk("F:/Projects/github/python"):
        print("Directory: ", dirpath)
        print("Includes these directories")
        for dirname in dirnames:
            print(dirname)
        print("Includes these files")
        for filename in files:
            print(filename)
        print()


def bottum_up_walk():
    '''Recursively list all files in a directory bottom up'''
    for dirpath, dirnames, files in os.walk("F:/Projects/github/python", topdown=False):
        print("Directory: ", dirpath)
        print("Includes these directories")
        for dirname in dirnames:
            print(dirname)
        print("Includes these files")
        for filename in files:
            print(filename)
        print()


if __name__ == "__main__":
    show_cwd()
    # up_1level()
    show_cwd()
    list_all("./")
    list_all("F:/Projects/github/python")
    list_dir("./")
    list_file("F:/Projects/github/python")
    list_txt()
    top_down_walk()

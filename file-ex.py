# Working with files
# LinkedIn Learning course: Working with Files by Kathryn Hodge
from datetime import datetime
import os


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


if __name__ == "__main__":
    show_cwd()
    up_1level()
    show_cwd()
    list_all("./")
    list_all("F:/Projects/github/python")
    list_dir("./")
    list_file("F:/Projects/github/python")

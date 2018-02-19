import os
import sys
import os.path
import shutil

def fileDir():
    path = '/Users/xiejiacheng/Documents/iTongue/itongue/temp'
    print(path)

    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)


def suffix(file, *suffixName):
    array = map(file.endswith, suffixName)
    if True in array:
        return True
    else:
        return False


def deleteFile():
    targetDir = fileDir()
    for file in os.listdir(targetDir):
        targetFile = os.path.join(targetDir, file)
        if suffix(file, '.ppm'):
            os.remove(targetFile)


if __name__ == '__main__':
    deleteFile()
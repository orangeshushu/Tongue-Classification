import os
import sys
import os.path
import shutil

def fileDir(i):

    path ='/Users/xiejiacheng/coding/alldata_cut/'
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
    for j in range(9):
        targetDir = fileDir(j)
        for file in os.listdir(targetDir):
            targetFile = os.path.join(targetDir, file)
            if suffix(file, '.DS_Store'):
                os.remove(targetFile)


if __name__ == '__main__':
    deleteFile()
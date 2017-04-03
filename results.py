from shutil import copyfile
import shutil
import os


def copyFilesInList(myList):

    shutil.rmtree("results")
    os.mkdir("results")

    for ind,fi in enumerate(myList):
        copyfile("samples/"+fi[1], "results/"+str(ind+1)+'.JPG')
import tensorflow as tf
import numpy as np
import math
from nearest import euclidean
import os
import shutil
from results import copyFilesInList
from tensorflow.python import debug as tf_debug

original = np.load("original.npy")

near= []

for f in os.listdir("vectors"):
    test = np.load("vectors/"+f)
 
    res = euclidean(original,test)
    near.append([res,f.strip(".npy")])
    

#print near
    
nearSort = sorted(near,key=lambda l:l[0])

for ne in nearSort:
    print ne

copyFilesInList(nearSort)



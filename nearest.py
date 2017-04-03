import tensorflow as tf
import math
import itertools

def euclidean(original, similar):
    
    eucl = 0

    for siA,siB in itertools.izip(original, similar):
        eucl += (siA - siB)*(siA - siB)

    eucl = math.sqrt(eucl)
    #print math.floor(eucl)
    return eucl
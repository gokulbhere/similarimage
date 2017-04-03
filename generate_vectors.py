import tensorflow as tf
import numpy as np
import os
import itertools
import math
import os
from nearest import euclidean


def create_graph():
  """Creates a graph from saved GraphDef file and returns a saver."""
  # Creates graph from saved graph_def.pb.
  with tf.gfile.FastGFile(os.path.join(
      'graph', 'classify_image_graph_def.pb'), 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    _ = tf.import_graph_def(graph_def, name='')

def run_inference_on_image(image):

    image_data = tf.gfile.FastGFile(image, 'rb').read()
    
    #print image

   
    with tf.Session() as sess:
        '''
        for test in sess.graph.get_operations():
            print test.name
            print test.values()
        '''
       
        feature_tensor = sess.graph.get_tensor_by_name('pool_3:0')
        feature_set = sess.run(feature_tensor,
                        {'DecodeJpeg/contents:0': image_data}) 
        #print feature_set.shape 
        feature_set = np.squeeze(feature_set) 
        #print feature_set.shape 
        
        return feature_set
        
    


    
if __name__=='__main__':
    
    create_graph()

    simi = []
    image = "original/"+os.listdir("original")[0]
    
    original = run_inference_on_image(image)
    np.save("original.npy",original)
    
    near = []
    
    if os.path.exists("vectors"):
        print "Vectors Exist"
    else:
        os.mkdir("vectors")
        for f in os.listdir('samples'):
            print f
            test = run_inference_on_image('samples/'+f)
            print test.shape
            np.save("vectors/"+f+".npy",test) 
        

# -*- coding: utf-8 -*-
"""
Created on Thu May 23 15:02:56 2024

@author: andre
"""
# import tensorflow as tf
# import os


# dire = "../../tfrecord/dataset_"
# arraydata = range(1140,7000,1)

# for index in arraydata:
#     file = dire+str(index)+".tfrecord"
#     for example in tf.compat.v1.python_io.tf_record_iterator(file):
#         print(file)
#         aaa=tf.train.Example.FromString(example)


import tensorflow as tf
import json
from google.protobuf.json_format import MessageToJson
import numpy as np

shpy = 201
shpx = 192
shpz = 96
padding = 15
dtype = 'float32'
# -------------------------------------------------------------------------------------------------------------------
# Define the function to parse
# -------------------------------------------------------------------------------------------------------------------
def parse_function(proto):
    """
    
    .................................................................................................................
    # _parse_function: Function for parsing the data
    .................................................................................................................

    Parameters
    ----------
    proto : TFRecords data
        Information to parse.

    Returns
    -------
    feature : TFRecords data
        Parsed features.
    label : TYPE
        Parsed labels.

    """
    # ---------------------------------------------------------------------------------------------------------------
    # Define your `features` dictionary here:
    # Adjust shape based on how data was flattened
    # ---------------------------------------------------------------------------------------------------------------
    feature_description = {'feature': tf.io.FixedLenFeature([shpy*(shpz+2*padding)*(shpx+2*padding)*3],dtype),
                            'label': tf.io.FixedLenFeature([shpy*shpz*shpx*3],dtype)}
    parsed_features     = tf.io.parse_single_example(proto,feature_description)
    feature             = tf.reshape(parsed_features['feature'],[shpy,shpz+2*padding,shpx+2*padding,3])
    label               = tf.reshape(parsed_features['label'],[shpy,shpz,shpx,3])
    return feature,label


files   = tf.data.Dataset.from_tensor_slices(["../../tfrecord/dataset_1000.tfrecord"])
dataset = files.interleave(tf.data.TFRecordDataset, cycle_length=tf.data.experimental.AUTOTUNE)
mapdata = dataset.map(parse_function) 
data_tf = list(mapdata.take(1).as_numpy_iterator())[0][0]
data_tf_out = list(mapdata.take(1).as_numpy_iterator())[0][1]



# -----------------------------------------------------------------------------------------------------------
# In the case of limiting to a number the GPUs, from this point in advance, only these GPUs are taken
# -----------------------------------------------------------------------------------------------------------
physical_devices = tf.config.list_physical_devices('GPU') # Physical devices
available_gpus   = len(physical_devices) 
if physical_devices:
    try:
        for gpu in physical_devices:
            
            # -----------------------------------------------------------------------------------------------
            # Allocate only as much GPU memory as needed for the runtime allocations
            # -----------------------------------------------------------------------------------------------
            tf.config.experimental.set_memory_growth(gpu,True)
            print("Memory growth for GPU: "+str(gpu),flush=True)
    except RuntimeError as ee:
        print(ee,flush=True)
# -----------------------------------------------------------------------------------------------------------
# Update number of GPUs and select the devices for the strategy
# -----------------------------------------------------------------------------------------------------------
ngpu = len(tf.config.list_logical_devices('GPU'))
list_compute   = ['CPU:0']
list_parameter = 'CPU:0'
for ii in np.arange(ngpu,dtype='int'):
    list_compute.append('GPU:'+str(ii))
        
# -----------------------------------------------------------------------------------------------------------
# Define the strategy for distributing the training
# we use central storage strategy because the size of the fields requires loading them on the CPU RAM
# and then take inside the GPUs the batch size. With other strategies such as mirrored we are having 
# overflows in the memory. Central storage is experimental, there may be compatibility problems
# -----------------------------------------------------------------------------------------------------------
strategy = tf.distribute.MirroredStrategy()
with strategy.scope():
    model = tf.keras.models.load_model("d20240524_models/trained_model.h5")
data_in = data_tf.reshape(1,shpy,shpz+2*padding,shpx+2*padding,3)
aaaa = model.predict(data_in)[0,:,:,:,0]
bbbb = data_tf_out[:,:,:,0]
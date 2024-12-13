# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 17:26:40 2024

@author: andre
"""
import tensorflow as tf
from tensorflow.keras import Model
from tensorflow.keras.optimizers import RMSprop
import numpy as np

shpy = 201
shpz = 288
shpx = 384
padding = 15
nfil = 32
stride = 1
activation = "relu"
kernel = 3
pooling = 2
mean_norm = False
data_type = "float32"
model_h5_weight = "../../../scratch/P125/models/trained_model_5285.weights.h5"
model_h5 = "../../../scratch/P125/models/trained_model_5285.h5"



def block(data_in={"input":[],"nfil":16,"stride":1,"activ":"relu","kernel":3,"dtype":None}):
    """
    .....................................................................................................................
    # block: function for defining the convolutional block: CNN+BN+Activation.
    .....................................................................................................................
    Parameters
    ----------
    data_in : dict, optional
        Data for defining the block.
        The default is {"xx":[],"nfil":16,"stride":1,"activ":"relu","kernel":3,dtype:None}.
        Data:
            - input  : tensor with the input of the layer
            - nfil   : number of filters of the layer
            - stride : stride of the layer
            - activ  : activation function of the layer
            - kernel : kernel used for the convolution
            - dtype  : type of the output data, if none do not specify (float32,float16)

    Returns
    -------
    data_out : dict
        Data of the output of the block.
        Data:
            - output : tensor with the output of the layer

    """
    # -------------------------------------------------------------------------------------------------------------------
    # Import the packages
    # -------------------------------------------------------------------------------------------------------------------
    from tensorflow.keras.layers import Conv3D, BatchNormalization, Activation
    
    # -------------------------------------------------------------------------------------------------------------------
    # Read the data
    # -------------------------------------------------------------------------------------------------------------------
    xx     = data_in["input"]
    nfil   = int(data_in["nfil"])
    stride = int(data_in["stride"])
    activ  = str(data_in["activ"])
    kern   = int(data_in["kernel"])
    kernel = (int(kern),int(kern),int(kern)) 
    dtype  = data_in["dtype"]
    flagt  = False
    if dtype is not None:
        if dtype != "float32" or dtype != "float16":
            dtype = "float32"
    else:
        flagt = True
    
    # -------------------------------------------------------------------------------------------------------------------
    # Define the block: Convolution+Batch Normalization+Activation
    # -------------------------------------------------------------------------------------------------------------------
    if flagt:
        xx = Conv3D(nfil, kernel_size=kernel,strides=(stride,stride,stride),padding="same")(xx)
        xx = BatchNormalization()(xx) 
        xx = Activation(activ)(xx)
    else:
        xx = Conv3D(nfil, kernel_size=kernel,strides=(stride,stride,stride),padding="same",dtype=dtype)(xx)
        xx = BatchNormalization(dtype=dtype)(xx)
        xx = Activation(activ,dtype=dtype)(xx)
    
    # -------------------------------------------------------------------------------------------------------------------
    # Define the output
    # -------------------------------------------------------------------------------------------------------------------
    data_out = {"output":xx}
    return data_out

def invblock(data_in={"input":[],"nfil":16,"stride":1,"activ":"relu","kernel":3,"outpad":(0,0,0)}):
    """
    .....................................................................................................................
    # invblock: function for defining the inverse convolutional block: CNN transpose+BN+Activation.
    .....................................................................................................................
    Parameters
    ----------
    data_in : dict, optional
        Data for defining the block.
        The default is {"input":[],"nfil":16,"stride":1,"activ":"relu","kernel":3,"outpad":(0,0,0)}.
        Data:
            - input  : tensor with the input of the layer
            - nfil   : number of filters of the layer
            - stride : stride of the layer
            - activ  : activation function of the layer
            - kernel : kernel used for the convolution
            - outpad : padding to adjust the size of the output

    Returns
    -------
    data_out : dict
        Data of the output of the block.
        Data:
            - output : tensor with the output of the layer

    """
    # -------------------------------------------------------------------------------------------------------------------
    # Read packages
    # -------------------------------------------------------------------------------------------------------------------
    from tensorflow.keras.layers import Conv3DTranspose, BatchNormalization, Activation
    
    # -------------------------------------------------------------------------------------------------------------------
    # Read data
    # -------------------------------------------------------------------------------------------------------------------
    xx     = data_in["input"]
    nfil   = int(data_in["nfil"])
    stride = int(data_in["stride"])
    activ  = str(data_in["activ"])
    kern   = int(data_in["kernel"])
    kernel = (int(kern),int(kern),int(kern)) 
    outpad = data_in["outpad"]
    
    # -------------------------------------------------------------------------------------------------------------------
    # Define the block: Transposed Convolution+Batch Normalization+Activation Fuction
    # -------------------------------------------------------------------------------------------------------------------
    xx = Conv3DTranspose(nfil, kernel_size=kernel,strides=(stride,stride,stride),padding="valid",
                         output_padding=outpad)(xx)
    xx = BatchNormalization()(xx) 
    xx = Activation(activ)(xx)
    
    # -------------------------------------------------------------------------------------------------------------------
    # Define the output
    # -------------------------------------------------------------------------------------------------------------------
    data_out = {"output":xx}
    return data_out           

def architecture_Unet(data_in={"x_in":[],"flag_print":True}):
    """
    .................................................................................................................
    # architecture_Unet
    .................................................................................................................

    Parameters
    ----------
    data_in : dict, optional
        Data for define the architecture. The default is {"x_in":[],"flag_print":True}.
        Data:
            - x_in       : input of the model
            - flag_print : flag for printing the data type of the layers (True: print, False: do not print)

    Returns
    -------
    dict
        Output of the model
        Data:
            - x_out : output of the model
    """        
    # --------------------------------------------------------------------------------------------------------------
    # Read the data
    # --------------------------------------------------------------------------------------------------------------
    x_in       = data_in["x_in"]
    flag_print = bool(data_in["flag_print"])
    
    # --------------------------------------------------------------------------------------------------------------
    # Define the required packages
    # --------------------------------------------------------------------------------------------------------------
    from tensorflow.keras.layers import AveragePooling3D,Concatenate
    from py_bin.py_functions.CNNblock_definition import block,invblock
    
    # --------------------------------------------------------------------------------------------------------------
    # Define the number of filters of each layer
    # --------------------------------------------------------------------------------------------------------------
    nfil1 = nfil
    nfil2 = 2*nfil1
    nfil3 = 2*nfil2
    nfil4 = 2*nfil3
    
    # --------------------------------------------------------------------------------------------------------------
    # Define the Unet by layers in the following lines the fields are defined following the format:
    # xij_k: being i the index of the level (similar sizes of the unet) 
    #        and j the number of the field (increase after the convolutional neurons)
    #        k defines if the level is encoding (e) or decoding (d)
    # --------------------------------------------------------------------------------------------------------------
    
    # --------------------------------------------------------------------------------------------------------------
    # Definintion of the encoder first layer
    # --------------------------------------------------------------------------------------------------------------
    data_x11_e = {"input":x_in,"nfil":nfil1,"stride":stride,"activ":activation,"kernel":kernel,
                  "dtype":None}
    x11_e      = block(data_in=data_x11_e)["output"]
    data_x12_e = {"input":x11_e,"nfil":nfil1,"stride":stride,"activ":activation,"kernel":kernel,
                  "dtype":None}
    x12_e      = block(data_in=data_x12_e)["output"]
    # --------------------------------------------------------------------------------------------------------------
    # Add an average pooling to go to the second layer (reducing the size of the fields)
    # --------------------------------------------------------------------------------------------------------------
    x20_e = AveragePooling3D(pooling)(x12_e)
    
    # --------------------------------------------------------------------------------------------------------------
    # Definition of the encoder second layer
    # --------------------------------------------------------------------------------------------------------------
    data_x21_e = {"input":x20_e,"nfil":nfil2,"stride":stride,"activ":activation,"kernel":kernel,
                  "dtype":None}
    x21_e      = block(data_in=data_x21_e)["output"]
    data_x22_e = {"input":x21_e,"nfil":nfil2,"stride":stride,"activ":activation,"kernel":kernel,
                  "dtype":None}
    x22_e      = block(data_in=data_x22_e)["output"]
    # --------------------------------------------------------------------------------------------------------------
    # Add an average pooling to go to the third layer
    # --------------------------------------------------------------------------------------------------------------
    x30_e = AveragePooling3D(pooling)(x22_e)
    
    # --------------------------------------------------------------------------------------------------------------
    # Definition of the encoder third layer
    # --------------------------------------------------------------------------------------------------------------
    data_x31_e = {"input":x30_e,"nfil":nfil3,"stride":stride,"activ":activation,"kernel":kernel,
                  "dtype":None}
    x31_e      = block(data_in=data_x31_e)["output"]
    data_x32_e = {"input":x31_e,"nfil":nfil3,"stride":stride,"activ":activation,"kernel":kernel,
                  "dtype":None}
    x32_e      = block(data_in=data_x32_e)["output"]
    # --------------------------------------------------------------------------------------------------------------
    # Add an average pooling to go to the fourth layer
    # --------------------------------------------------------------------------------------------------------------
    x40_e = AveragePooling3D(pooling)(x32_e) 
    
    # --------------------------------------------------------------------------------------------------------------
    # Definition of the encoder fourth layer
    # --------------------------------------------------------------------------------------------------------------
    data_x41_e = {"input":x40_e,"nfil":nfil4,"stride":stride,"activ":activation,"kernel":kernel,
                  "dtype":None}
    x41_e      = block(data_in=data_x41_e)["output"]
    data_x42_e = {"input":x41_e,"nfil":nfil4,"stride":stride,"activ":activation,"kernel":kernel,
                  "dtype":None}
    x42_e      = block(data_in=data_x42_e)["output"]
    
    # --------------------------------------------------------------------------------------------------------------
    # Definition of the decoder third layer
    # Note: if modifiying the default values of the layer, the outpad and the size taken of x30_d 
    # may need to be modified
    # --------------------------------------------------------------------------------------------------------------
    data_x30_d = {"input":x42_e,"nfil":nfil3,"stride":pooling,"activ":activation,"kernel":kernel,
                  "outpad":(0,0,0)}
    x30_d      = invblock(data_in=data_x30_d)["output"]
    x31_d      = Concatenate()([x32_e,x30_d[:,:-1,:,:,:]]) 
    data_x32_d = {"input":x31_d,"nfil":nfil3,"stride":stride,"activ":activation,"kernel":kernel,
                  "dtype":None}
    x32_d      = block(data_in=data_x32_d)["output"]
    
    # --------------------------------------------------------------------------------------------------------------
    # Definition of the decoder second layer
    # Note: if modifiying the default values of the layer, the outpad and the size taken of x20_d 
    # may need to be modified
    # --------------------------------------------------------------------------------------------------------------
    data_x20_d = {"input":x32_d,"nfil":nfil2,"stride":pooling,"activ":activation,"kernel":kernel,
                  "outpad":(0,0,0)}
    x20_d      = invblock(data_in=data_x20_d)["output"]
    x21_d      = Concatenate()([x22_e,x20_d[:,:-1,:,:,:]]) 
    data_x22_d = {"input":x21_d,"nfil":nfil2,"stride":stride,"activ":activation,"kernel":kernel,
                  "dtype":None}
    x22_d      = block(data_in=data_x22_d)["output"]
    
    # --------------------------------------------------------------------------------------------------------------
    # Definition of the decoder first layer
    # Note: if modifiying the default values of the layer, the outpad and the size taken of x10_d 
    # may need to be modified
    # --------------------------------------------------------------------------------------------------------------
    data_x10_d = {"input":x22_d,"nfil":nfil1,"stride":pooling,"activ":activation,"kernel":kernel,
                  "outpad":(0,0,0)}
    x10_d      = invblock(data_in=data_x10_d)["output"] 
    x11_d      = Concatenate()([x12_e,x10_d[:,:,:-1,:-1,:]])
    data_x12_d = {"input":x11_d,"nfil":nfil1,"stride":stride,"activ":activation,"kernel":kernel,
                  "dtype":None}
    x12_d      = block(data_in=data_x12_d)["output"]
    if mean_norm:
        data_x13_d = {"input":x12_d,"nfil":3,"stride":stride,"activ":"tanh","kernel":kernel,
                      "dtype":data_type}
    else:
        data_x13_d = {"input":x12_d,"nfil":3,"stride":stride,"activ":"sigmoid","kernel":kernel,
                      "dtype":data_type}
    x13_d      = block(data_in=data_x13_d)["output"]
    
    # --------------------------------------------------------------------------------------------------------------
    # Crop the solution to delete the padding
    # --------------------------------------------------------------------------------------------------------------
    x_out    = x13_d[:,:,padding:-padding,padding:-padding,:]
    data_out = {"x_out":x_out}
    
    # --------------------------------------------------------------------------------------------------------------
    # Print data type
    # --------------------------------------------------------------------------------------------------------------
    if flag_print:
        print("x_in type:"+str(x_in.dtype),flush=True)
        print("x11_e type:"+str(x11_e.dtype),flush=True)
        print("x12_e type:"+str(x12_e.dtype),flush=True)
        print("x20_e type:"+str(x20_e.dtype),flush=True)
        print("x21_e type:"+str(x21_e.dtype),flush=True)
        print("x22_e type:"+str(x22_e.dtype),flush=True)
        print("x30_e type:"+str(x30_e.dtype),flush=True)
        print("x31_e type:"+str(x31_e.dtype),flush=True)
        print("x32_e type:"+str(x32_e.dtype),flush=True)      
        print("x40_e type:"+str(x40_e.dtype),flush=True)
        print("x41_e type:"+str(x41_e.dtype),flush=True)
        print("x42_e type:"+str(x42_e.dtype),flush=True)
        print("x30_d type:"+str(x30_d[:,:-1,:,:,:].dtype),flush=True) 
        print("x31_d type:"+str(x31_d.dtype),flush=True) 
        print("x32_d type:"+str(x32_d.dtype),flush=True)
        print("x20_d type:"+str(x20_d[:,:-1,:,:,:].dtype),flush=True) 
        print("x21_d type:"+str(x21_d.dtype),flush=True)
        print("x22_d type:"+str(x22_d.dtype),flush=True)
        print("x10_d type:"+str(x10_d[:,:,:-1,:-1,:].dtype),flush=True)
        print("x11_d type:"+str(x11_d.dtype),flush=True)
        print("x12_d type:"+str(x12_d.dtype),flush=True)
        print("x13_d type:"+str(x13_d.dtype),flush=True)
        print("x_out type:"+str(x_out.dtype),flush=True)
    
    # --------------------------------------------------------------------------------------------------------------
    # Return the output
    # --------------------------------------------------------------------------------------------------------------
    return data_out

def model_base():
    """
    .................................................................................................................
    # model_base
    .................................................................................................................
    Function to define the model used for the problem

    Returns
    -------
    None.

    """    
    # --------------------------------------------------------------------------------------------------------------
    # Define the required packages
    # --------------------------------------------------------------------------------------------------------------    
    from tensorflow.keras.layers import Input
    
    # --------------------------------------------------------------------------------------------------------------
    # The dimensions of the input field are selected from the size of the fields, adding the padding
    # --------------------------------------------------------------------------------------------------------------
    dim0 = shpy
    dim1 = shpz+2*padding
    dim2 = shpx+2*padding
    dim3 = 3
    shp = (dim0,dim1,dim2,dim3)
    
    # --------------------------------------------------------------------------------------------------------------
    # Define the input and the output of the model
    # --------------------------------------------------------------------------------------------------------------
    inputs  = Input(shape=shp)
    x_in         = inputs
    outputs = architecture_Unet(data_in={"x_in":x_in,"flag_print":True})["x_out"]
    return inputs,outputs



inputs,outputs=model_base()
optimizer  = RMSprop(learning_rate=5e-4,momentum=0.9) 
model = Model(inputs, outputs)
model.compile(loss=tf.keras.losses.MeanSquaredError(),optimizer=optimizer)
model.summary()

weights0 = model.get_weights()
print(len(weights0))



import h5py 
file = h5py.File(model_h5_weight,'r')
weights = [np.array(file["weights_"+str(ii)]) for ii in np.arange(len(file.keys()))]

model.set_weights(weights)
model.save(model_h5)
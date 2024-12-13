# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------------------------------------------------
calc_pred_error_lowmemory_restart_computemeans.py
-------------------------------------------------------------------------------------------------------------------------
Created on Thu Mar 28 13:38:39 2024

@author: Andres Cremades Botella

Calculates the error of the predictions. The file requires to set the following paths:
    - folder_def  : (str) name of the folder containing the files for configuring the case of analysis.
    - chd_str     : (str) name of the file containing the data of the channel.
    - folders_str : (str) name of the file containing the folders and files used in the problem.
    - sh_data_str : (str) name of the file containing the information required for calculating the SHAP values
"""
# ----------------------------------------------------------------------------------------------------------------------
# Define the names of the files containing the definitios of the parameters
# - folder_def : folder containing the files with the definitions required in the problem
# - chd_str    : file containing the data of the channel
# - folders    : file containing the folder and file structures
# - tr_data    : file containing the data of the training
# ----------------------------------------------------------------------------------------------------------------------
folder_def  = "d20240703_definitions" #"P125_83pi_240603_v0_definitions"
chd_str     = "channel_data"
folders_str = "folders" #"folders_local"
tr_data_str = "evaluate_data"
sh_data_str = "shap_data"
name_file   = "restart1S"

# ----------------------------------------------------------------------------------------------------------------------
# Load the packages
# ----------------------------------------------------------------------------------------------------------------------
import py_bin.py_class.ann_config as ann
import os
import numpy as np

# ----------------------------------------------------------------------------------------------------------------------
# Unlock the h5 files for avoiding problems in some clusters
# ----------------------------------------------------------------------------------------------------------------------
os.environ['HDF5_USE_FILE_LOCKING'] = 'FALSE'

# ----------------------------------------------------------------------------------------------------------------------
# Import information files
# ----------------------------------------------------------------------------------------------------------------------
exec("from "+folder_def+" import "+chd_str+" as chd")
exec("from "+folder_def+" import "+folders_str+" as folders")
exec("from "+folder_def+" import "+tr_data_str+" as tr_data")
exec("from "+folder_def+" import "+sh_data_str+" as sh_data")

# ----------------------------------------------------------------------------------------------------------------------
# Define the data of the model definition: data, padding, downsampling...
#     - data_folder     : Folder for storing the data of the model
# ----------------------------------------------------------------------------------------------------------------------
data_folder = folders.data_folder
error_file  = folders.error_file

# ----------------------------------------------------------------------------------------------------------------------
# Train the model
# ----------------------------------------------------------------------------------------------------------------------

file_error = data_folder+'/'+error_file
file_error = file_error.replace(".txt","_"+name_file+".txt")   
error_usum = 0
error_vsum = 0
error_wsum = 0
n_sum      = 0                
with open(file_error, "r")  as file:
    for line in file:
        line_array  = np.array(line.strip().replace('[','').replace(']','').split(','),dtype="float")
        error_u     = line_array[0]  
        error_v     = line_array[1] 
        error_w     = line_array[2]
        error_usum += error_u
        error_vsum += error_v
        error_wsum += error_w
        n_sum      += 1
file.close()
error_u_mean = error_usum/n_sum
error_v_mean = error_vsum/n_sum
error_w_mean = error_wsum/n_sum

print("Error u: "+str(error_u_mean))
print("Error v: "+str(error_v_mean))
print("Error w: "+str(error_w_mean))
      
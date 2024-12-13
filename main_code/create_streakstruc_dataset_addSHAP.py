# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------------------------------------------------
create_streakstruc_dataset.py
-------------------------------------------------------------------------------------------------------------------------
Created on Wed Mar 27 08:23:08 2024

@author: Andres Cremades Botella

Function to add the shap values to the streak structure dataset. In the function the grid-points containing the
structures. To lauch the file the following parameters need to be selected:
    - folder_def  : (str) name of the folder containing the files for configuring the case of analysis.
    - chd_str     : (str) name of the file containing the data of the channel.
    - folders_str : (str) name of the file containing the folders and files used in the problem.
    - st_data_str : (str) name of the file containing the information required for the statistics.
For more information about the tangential Reynolds stress structures:
    - Lozano-Durán, A., Flores, O., & Jiménez, J. (2012). The three-dimensional structure of momentum transfer in
      turbulent channels. Journal of Fluid Mechanics, 694, 100-130.
"""
# -----------------------------------------------------------------------------------------------------------------------
# Define the names of the files containing the definitios of the parameters
# - folder_def : folder containing the files with the definitions required in the problem
# - chd_str    : file containing the data of the channel
# - folders    : file containing the folder and file structures
# - st_data    : file containing the data of the statistics
# -----------------------------------------------------------------------------------------------------------------------
folder_def  = "d20240603_definitions"
chd_str     = "channel_data"
folders_str = "folders"
st_data_str = "stats_data"
sh_data_str = "shap_data"
tr_data_str = "training_data"

# -----------------------------------------------------------------------------------------------------------------------
# Import Packages
# -----------------------------------------------------------------------------------------------------------------------
from py_bin.py_class.streak_structure import streak_structure
import os

# -----------------------------------------------------------------------------------------------------------------------
# Unlock the h5 files for avoiding problems in some clusters
# -----------------------------------------------------------------------------------------------------------------------
os.environ['HDF5_USE_FILE_LOCKING'] = 'FALSE'

# -----------------------------------------------------------------------------------------------------------------------
# Import information files
# -----------------------------------------------------------------------------------------------------------------------
exec("from "+folder_def+" import "+chd_str+" as chd")
exec("from "+folder_def+" import "+folders_str+" as folders")
exec("from "+folder_def+" import "+st_data_str+" as st_data")
exec("from "+folder_def+" import "+sh_data_str+" as sh_data")
exec("from "+folder_def+" import "+tr_data_str+" as tr_data")

# -----------------------------------------------------------------------------------------------------------------------
# Data for the statistics:
#     - index_ini     : index of the initial field
#     - index_fin     : index of the final field
#     - index_delta   : increment in the index of the field
#     - Hperc         : percolation index
#     - uvw_folder    : folder of the flow field data
#     - uvw_file      : file of the flow field data
#     - umean_file    : file to save the mean velocity
#     - data_folder   : folder to store the calculated data
#     - dx            : downsampling in x
#     - dy            : downsampling in y
#     - dz            : downsampling in z
#     - L_x           : length of the channel in the streamwise direction
#     - L_y           : half-width of the channel in the wall-normal direction
#     - L_z           : length of the channel in the spanwise direction
#     - urms_file     : file to save the rms of the velocity
#     - rey           : Friction Reynolds number
#     - utau          : Friction velocity
#     - padding       : padding of the flow field
#     - sym_quad      : flag for using the symmetry in the direction 2 of the field for the quadrant selection
#     - filvol        : volume for filtering the structures+
#     - shap_folder   : folder of the shap values
#     - shap_folder   : file of the shap values
#     - streak_folder : folder of the streaks
#     - streak_file   : file of the streaks
#     - nsamples      : number of samples of the shap calculation
#     - padding       : padding of the field
#     - data_type     : type of data used by the model
# -----------------------------------------------------------------------------------------------------------------------
index_ini     = st_data.field_ini
index_fin     = st_data.field_fin
index_delta   = st_data.field_delta
Hperc         = 1.75
uvw_folder    = folders.uvw_folder
uvw_file      = folders.uvw_file
umean_file    = folders.umean_file
data_folder   = folders.data_folder
dx            = chd.dx
dy            = chd.dy
dz            = chd.dz
L_x           = chd.L_x
L_y           = chd.L_y
L_z           = chd.L_z
urms_file     = folders.urms_file
rey           = chd.rey
utau          = chd.utau
padding       = chd.padding
sym_quad      = True
filvol        = chd.filvol
shap_folder   = folders.shap_folder
shap_file     = folders.shap_file
streak_folder = folders.streak_folder
streak_file   = folders.streak_file
nsamples      = sh_data.nsamples
padding       = chd.padding
data_type     = tr_data.data_type

# -----------------------------------------------------------------------------------------------------------------------
# Create the data of the structure and define the indices to generate the structures
# -----------------------------------------------------------------------------------------------------------------------
data_struc  = {"uvw_folder":uvw_folder,"uvw_file":uvw_file,"Hperc":Hperc,"index":[],"dx":dx,"dy":dx,"dz":dz,
               "L_x":L_x,"L_y":L_y,"L_z":L_z,"rey":rey,"utau":utau,"padding":padding,"data_folder":data_folder,
               "umean_file":umean_file,"urms_file":urms_file,"sym_quad":sym_quad,"filvol":filvol,
               "shap_folder":shap_folder,"shap_file":shap_file,"folder":streak_folder,"file":streak_file,
               "padding":padding,"data_type":data_type}
index_range = range(index_ini,index_fin,index_delta)

# -----------------------------------------------------------------------------------------------------------------------
# Run the loop
# -----------------------------------------------------------------------------------------------------------------------
for ii in index_range:
    data_struc["index"] = ii
    streak_struc        = streak_structure(data_in=data_struc)
    
    # -------------------------------------------------------------------------------------------------------------------
    # Create the matrix containing the points of the structures
    # -------------------------------------------------------------------------------------------------------------------
    streak_struc.add_SHAP(data_in={"nsamples":nsamples})

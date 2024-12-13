# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------------------------------------------------
plot_urms.py
-------------------------------------------------------------------------------------------------------------------------
Created on Thu Mar 28 13:38:39 2024

@author:  Andres Cremades Botella

Create the plot of the root mean squared velocity. The file requires to set the following paths:
    - folder_def  : (str) name of the folder containing the files for configuring the case of analysis.
    - chd_str     : (str) name of the file containing the data of the channel.
    - folders_str : (str) name of the file containing the folders and files used in the problem.
    - st_data_str : (str) name of the file containing the information required for the statistics.
In addition the following variables need to be set:
    - xlabel      : label of the x axis
    - ylabel      : label of the y axis
    - fontsize    : size of the text in the figure
    - figsize_x   : size of the figure in axis x
    - figsize_y   : size of the figure in axis y
    - colormap    : colormap used in the plot
    - colornum    : number of levels required in the colormap
    - fig_name    : name of the figure after saving
    - dpi         : dots per inch of the figure
"""
# ----------------------------------------------------------------------------------------------------------------------
# Define the names of the files containing the definitios of the parameters
# - folder_def : folder containing the files with the definitions required in the problem
# - folders    : file containing the folder and file structures
# ----------------------------------------------------------------------------------------------------------------------
folder_def  = "d20240603_definitions"
chd_str     = "channel_data"
folders_str = "folders"
st_data_str = "stats_data"
pred        = True

# -----------------------------------------------------------------------------------------------------------------------
# Define the variables required for the plot
#     - xlabel      : label of the x axis
#     - ylabel      : label of the y axis
#     - fontsize    : size of the text in the figure
#     - figsize_x   : size of the figure in axis x
#     - figsize_y   : size of the figure in axis y
#     - colormap    : colormap used in the plot
#     - colornum    : number of levels required in the colormap
#     - fig_name    : name of the figure after saving
#     - dpi         : dots per inch of the figure
# -----------------------------------------------------------------------------------------------------------------------
xlabel      = "$y^+$"
ylabel      = "$u'^+$"
ylabel2     = "$|u_iu_j|^+$"
fontsize    = 18
figsize_x   = 7
figsize_y   = 5
colormap    = "viridis"
colornum    = 4
fig_name    = "urms"
fig_name2   = "uvabs"
dpi         = 200
# -----------------------------------------------------------------------------------------------------------------------
# Import packages
# -----------------------------------------------------------------------------------------------------------------------
from py_bin.py_plots.ploturms import ploturms
import os

# ----------------------------------------------------------------------------------------------------------------------
# Unlock the h5 files for avoiding problems in some clusters
# ----------------------------------------------------------------------------------------------------------------------
os.environ['HDF5_USE_FILE_LOCKING'] = 'FALSE'

# ----------------------------------------------------------------------------------------------------------------------
# Import information files
# ----------------------------------------------------------------------------------------------------------------------
exec("from "+folder_def+" import "+chd_str+" as chd")
exec("from "+folder_def+" import "+folders_str+" as folders")
exec("from "+folder_def+" import "+st_data_str+" as st_data")

# -----------------------------------------------------------------------------------------------------------------------
# Define the information of the data
#     - data_folder : folder containing the training data
#     - plot_folder : folder to save the figures
#     - file        : name of the file containing the rms velocity information
#     - dy          : downsampling of the wall-normal direction
#     - dx          : downsampling of the streamwise direction
#     - dz          : downsampling of the spanwise direction
#     - uvw_folder  : folder of the flow fields
#     - uvw_file    : file of the flow fields
#     - L_x         : dimension of the channel in the streamwise direction
#     - L_y         : dimension of the channel in the wall-normal direction
#     - L_z         : dimension of the channel in the spanwise direction
#     - file_trj    : file containing the data of Torroja
# -----------------------------------------------------------------------------------------------------------------------
data_folder   = folders.data_folder
plot_folder   = folders.plot_folder
if pred:
    file      = folders.urmspred_file
    fig_name  = fig_name+'_pred'
    fig_name2 = fig_name2+'_pred'
else:
    file      = folders.urms_file
dy            = chd.dy
dx            = chd.dx
dz            = chd.dz
uvw_folder    = folders.uvw_folder
uvw_file      = folders.uvw_file
L_x           = chd.L_x
L_y           = chd.L_y
L_z           = chd.L_z
file_trj      = st_data.file_trj
rey           = chd.rey
utau          = chd.utau

# -----------------------------------------------------------------------------------------------------------------------
# Create the plot
# -----------------------------------------------------------------------------------------------------------------------
plot_format_data = {"file":file,"folder":data_folder,"plot_folder":plot_folder,"xlabel":xlabel,
                    "ylabel":ylabel,"ylabel2":ylabel2,"fontsize":fontsize,"figsize_x":figsize_x,"figsize_y":figsize_y,
                    "colormap":colormap,"colornum":colornum,"fig_name":fig_name,"fig_name2":fig_name2,"dpi":dpi,
                    "dy":dy,"dx":dx,"dz":dz,"uvw_folder":uvw_folder,"uvw_file":uvw_file,"L_x":L_x,"L_y":L_y,"L_z":L_z,
                    "file_trj":file_trj,"rey":rey,"utau":utau}
ploturms(data_in=plot_format_data)
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------------------------------------------------
plot_chong_streak_3d.py
-------------------------------------------------------------------------------------------------------------------------
Created on Tue Jun 18 11:30:49 2024

@author: Andres Cremades Botella

Function to plot the chong vortices and shap structures:
    - folder_def  : (str) name of the folder containing the files for configuring the case of analysis.
    - chd_str     : (str) name of the file containing the data of the channel.
    - folders_str : (str) name of the file containing the folders and files used in the problem.
    - st_data_str : (str) name of the file containing the information required for the statistics.
For more information about the tangential Reynolds stress structures:
    - Lozano-Durán, A., Flores, O., & Jiménez, J. (2012). The three-dimensional structure of momentum transfer in
      turbulent channels. Journal of Fluid Mechanics, 694, 100-130.
"""
import matplotlib
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
xlabel      = "$x^+$"
ylabel      = "$z^+$"
zlabel      = "$y^+$"
fontsize    = 18
figsize_x   = 7
figsize_y   = 5
colornum    = 4
fig_name    = "chong_streak_3d"
dpi         = 200
colors_12   = matplotlib.cm.get_cmap('viridis',colornum).colors
colormap1   = colors_12[3,:]
colormap2   = colors_12[2,:]

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
# Import packages
# -----------------------------------------------------------------------------------------------------------------------
from py_bin.py_class.chong_structure import chong_structure
from py_bin.py_class.streak_structure import streak_structure
import os
from py_bin.py_plots.plotstruc3d_2struc import plotstruc3d_2struc,plotstruc3d_2struc_separate

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
#     - index         : index of the field
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
#     - chong_folder  : folder of the chong structures
#     - chong_file    : file of the chong structures
#     - padding       : padding of the field
#     - data_type     : type of data used by the model
#     - SHAPq_folder  : folder of the shap structures
#     - SHAPq_file    : file of the uv structures
#     - nsamples      : number of samples of the shap calculation
#     - SHAPrms_file  : file of the rms of the shap
# -----------------------------------------------------------------------------------------------------------------------
index         = 7000
Hperc         = 1.41
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
chong_folder  = folders.chong_folder
chong_file    = folders.chong_file
padding       = chd.padding
data_type     = tr_data.data_type
plot_folder   = folders.plot_folder
streak_folder  = folders.streak_folder
streak_file    = folders.streak_file
nsamples      = sh_data.nsamples
SHAPrms_file  = folders.SHAPrms_file

# -----------------------------------------------------------------------------------------------------------------------
# Create the data of the uv structure
# -----------------------------------------------------------------------------------------------------------------------
chong_struc = chong_structure(data_in={"uvw_folder":uvw_folder,"uvw_file":uvw_file,"Hperc":Hperc,"index":index,
                                       "dx":dx,"dy":dy,"dz":dz,"L_x":L_x,"L_y":L_y,"L_z":L_z,"rey":rey,"utau":utau,
                                       "padding":padding,"data_folder":data_folder,"umean_file":umean_file,
                                       "urms_file":urms_file,"sym_quad":True,"filvol":filvol,
                                       "shap_folder":shap_folder,"shap_file":shap_file,"folder":chong_folder,
                                       "file":chong_file,"padding":padding,"data_type":data_type})
chong_struc.read_struc()

# -----------------------------------------------------------------------------------------------------------------------
# Create the data of the shap structure
# -----------------------------------------------------------------------------------------------------------------------
streak_struc = streak_structure(data_in={"uvw_folder":uvw_folder,"uvw_file":uvw_file,"Hperc":Hperc,"index":index,
                                         "dx":dx,"dy":dy,"dz":dz,"L_x":L_x,"L_y":L_y,"L_z":L_z,"rey":rey,"utau":utau,
                                         "padding":padding,"data_folder":data_folder,"umean_file":umean_file,
                                         "urms_file":urms_file,"sym_quad":True,"filvol":filvol,
                                         "shap_folder":shap_folder,"shap_file":shap_file,"folder":streak_folder,
                                         "file":streak_file,"padding":padding,"data_type":data_type})
streak_struc.read_struc()

# -----------------------------------------------------------------------------------------------------------------------
# Plot the 3D field
# -----------------------------------------------------------------------------------------------------------------------
plotstruc3d_2struc(data_in={"struc1":chong_struc,"struc2":streak_struc,"plot_folder":plot_folder,"xlabel":xlabel,
                            "ylabel":ylabel,"zlabel":zlabel,"fontsize":fontsize,"figsize_x":figsize_x,
                            "figsize_y":figsize_y,"colormap1":colormap1,"colormap2":colormap2,"colornum":colornum,
                            "fig_name":fig_name,"dpi":dpi,"dy":dy,"dx":dx,"dz":dz,"uvw_folder":uvw_folder,
                            "uvw_file":uvw_file,"L_x":L_x,"L_y":L_y,"L_z":L_z,"rey":rey,"utau":utau,"cmap_flag":False})
plotstruc3d_2struc_separate(data_in={"struc1":chong_struc,"struc2":streak_struc,"plot_folder":plot_folder,
                                     "xlabel":xlabel,"ylabel":ylabel,"zlabel":zlabel,"fontsize":fontsize,
                                     "figsize_x":figsize_x,"figsize_y":figsize_y,"colormap1":colormap1,
                                     "colormap2":colormap2,"colornum":colornum,"fig_name":fig_name,"dpi":dpi,
                                     "dy":dy,"dx":dx,"dz":dz,"uvw_folder":uvw_folder,"uvw_file":uvw_file,
                                     "L_x":L_x,"L_y":L_y,"L_z":L_z,"rey":rey,"utau":utau,"cmap_flag":False})
# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------------------------------------------------
plot_figure4struct.py
-------------------------------------------------------------------------------------------------------------------------
Created on Tue Jun 18 09:52:56 2024

@author: Andres Cremades Botella

Visualization of a structure of each type
Requieres to set the following parameters
    - folder_def  : (str) name of the folder containing the files for configuring the case of analysis.
    - chd_str     : (str) name of the file containing the data of the channel.
    - folders_str : (str) name of the file containing the folders and files used in the problem.
    - st_data_str : (str) name of the file containing the information required for the statistics.
In addition the following variables need to be set:
    - fig2_xlabel      : label of the x axis for the figure 2
    - fig2_ylabel      : label of the y axis for the figure 2
    - fig2_zlabel      : label of the z axis for the figure 2
    - fig2_fontsize    : size of the text in the figure 2
    - fig2_figsize_x   : size of the figure 2 in axis x
    - fig2_figsize_y   : size of the figure 2 in axis y
    - fig2_colormap    : colormap used in the figure 2
    - fig2_colornum    : number of levels required in the colormap of figure 2
    - fig2_name        : name of the figure 2 after saving
    - fig2_dpi         : dots per inch of the figure 2
"""
# -----------------------------------------------------------------------------------------------------------------------
# Define the variables required for the plot
#     - fig2_xlabel      : label of the x axis for the figure 2
#     - fig2_ylabel      : label of the y axis for the figure 2
#     - fig2_zlabel      : label of the z axis for the figure 2
#     - fig2_fontsize    : size of the text in the figure 2
#     - fig2_figsize_x   : size of the figure 2 in axis x
#     - fig2_figsize_y   : size of the figure 2 in axis y
#     - fig2_colormap    : colormap used in the figure 2
#     - fig2_colornum    : number of levels required in the colormap of figure 2
#     - fig2_name        : name of the figure 2 after saving
#     - fig2_dpi         : dots per inch of the figure 2
# -----------------------------------------------------------------------------------------------------------------------
fig2_xlabel      = "$x^+$"
fig2_ylabel      = "$z^+$"
fig2_zlabel      = "$y^+$"
fig2_fontsize    = 18
fig2_figsize_x   = 7
fig2_figsize_y   = 5
fig2_colormap    = "viridis"
fig2_colornum    = 4
fig2_name        = "figure2"
fig2_dpi         = 200

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
from py_bin.py_class.shap_structure import shap_structure
from py_bin.py_class.uv_structure import uv_structure
from py_bin.py_class.streak_structure import streak_structure
from py_bin.py_class.chong_structure import chong_structure
import os
import matplotlib
from py_bin.py_plots.plotstruc3d_4struc import plotstruc3d, plotstruc3d_separe

# -----------------------------------------------------------------------------------------------------------------------
# Unlock the h5 files for avoiding problems in some clusters
# -----------------------------------------------------------------------------------------------------------------------
os.environ['HDF5_USE_FILE_LOCKING'] = 'FALSE'

# -----------------------------------------------------------------------------------------------------------------------
# Generate the colors
# -----------------------------------------------------------------------------------------------------------------------
fig2_colors_4 = matplotlib.cm.get_cmap(fig2_colormap,4).colors
fig2_colormap1 = fig2_colors_4[0,:]
fig2_colormap2 = fig2_colors_4[1,:]
fig2_colormap3 = fig2_colors_4[2,:]
fig2_colormap4 = fig2_colors_4[3,:]

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
#     - shap_file     : file of the shap values
#     - SHAPq_folder  : folder of the shap structures
#     - SHAPq_file    : file of the shap structures
#     - uv_folder     : folder of the uv structures
#     - uv_file       : file of the uv structures
#     - streak_folder : folder of the streaks structures
#     - streak_file   : file of the streaks structures
#     - chong_folder  : folder of the chong structures
#     - chong_file    : file of the chong structures
#     - padding       : padding of the field
#     - data_type     : type of data used by the model
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
SHAPq_folder  = folders.SHAPq_folder
SHAPq_file    = folders.SHAPq_file
uv_folder     = folders.uv_folder
uv_file       = folders.uv_file
streak_folder = folders.streak_folder
streak_file   = folders.streak_file
chong_folder  = folders.chong_folder
chong_file    = folders.chong_file
padding       = chd.padding
data_type     = tr_data.data_type
nsamples      = sh_data.nsamples
SHAPrms_file  = folders.SHAPrms_file
plot_folder   = folders.plot_folder


# -----------------------------------------------------------------------------------------------------------------------
# Create the data of the structure
# -----------------------------------------------------------------------------------------------------------------------
shap_struc = shap_structure(data_in={"uvw_folder":uvw_folder,"uvw_file":uvw_file,"Hperc":Hperc,"index":index,"dx":dx,
                                     "dy":dy,"dz":dz,"L_x":L_x,"L_y":L_y,"L_z":L_z,"rey":rey,"utau":utau,
                                     "padding":padding,"data_folder":data_folder,"umean_file":umean_file,
                                     "urms_file":urms_file,"sym_quad":True,"filvol":filvol,"shap_folder":shap_folder,
                                     "shap_file":shap_file,"folder":SHAPq_folder,"file":SHAPq_file,"padding":padding,
                                     "data_type":data_type,"nsamples":nsamples,"SHAPrms_file":SHAPrms_file})
shap_struc.read_struc()

# -----------------------------------------------------------------------------------------------------------------------
# Create the data of the structure
# -----------------------------------------------------------------------------------------------------------------------
uv_struc = uv_structure(data_in={"uvw_folder":uvw_folder,"uvw_file":uvw_file,"Hperc":Hperc,"index":index,"dx":dx,
                                 "dy":dy,"dz":dz,"L_x":L_x,"L_y":L_y,"L_z":L_z,"rey":rey,"utau":utau,
                                 "padding":padding,"data_folder":data_folder,"umean_file":umean_file,
                                 "urms_file":urms_file,"sym_quad":True,"filvol":filvol,"shap_folder":shap_folder,
                                 "shap_file":shap_file,"folder":uv_folder,"file":uv_file,"padding":padding,
                                 "data_type":data_type})
uv_struc.read_struc()

# -----------------------------------------------------------------------------------------------------------------------
# Create the data of the structure
# -----------------------------------------------------------------------------------------------------------------------
streak_struc = streak_structure(data_in={"uvw_folder":uvw_folder,"uvw_file":uvw_file,"Hperc":Hperc,"index":index,
                                         "dx":dx,"dy":dy,"dz":dz,"L_x":L_x,"L_y":L_y,"L_z":L_z,"rey":rey,"utau":utau,
                                         "padding":padding,"data_folder":data_folder,"umean_file":umean_file,
                                         "urms_file":urms_file,"sym_quad":True,"filvol":filvol,
                                         "shap_folder":shap_folder,"shap_file":shap_file,"folder":streak_folder,
                                         "file":streak_file,"padding":padding,"data_type":data_type})
streak_struc.read_struc()

# -----------------------------------------------------------------------------------------------------------------------
# Create the data of the structure
# -----------------------------------------------------------------------------------------------------------------------
chong_struc = chong_structure(data_in={"uvw_folder":uvw_folder,"uvw_file":uvw_file,"Hperc":Hperc,"index":index,
                                       "dx":dx,"dy":dy,"dz":dz,"L_x":L_x,"L_y":L_y,"L_z":L_z,"rey":rey,"utau":utau,
                                       "padding":padding,"data_folder":data_folder,"umean_file":umean_file,
                                       "urms_file":urms_file,"sym_quad":True,"filvol":filvol,
                                       "shap_folder":shap_folder,"shap_file":shap_file,"folder":chong_folder,
                                       "file":chong_file,"padding":padding,"data_type":data_type})
chong_struc.read_struc()

# -----------------------------------------------------------------------------------------------------------------------
# Plot the 3D field
# -----------------------------------------------------------------------------------------------------------------------
plotstruc3d(data_in={"struc1":shap_struc,"struc2":uv_struc,"struc3":streak_struc,"struc4":chong_struc,
                      "plot_folder":plot_folder,"xlabel":fig2_xlabel,"ylabel":fig2_ylabel,"zlabel":fig2_zlabel,
                      "fontsize":fig2_fontsize,"figsize_x":fig2_figsize_x,"figsize_y":fig2_figsize_y,
                      "colormap1":fig2_colormap1,"colormap2":fig2_colormap2,"colormap3":fig2_colormap3,
                      "colormap4":fig2_colormap4,"fig_name":fig2_name,"dpi":fig2_dpi,
                      "dy":dy,"dx":dx,"dz":dz,"uvw_folder":uvw_folder,"uvw_file":uvw_file,"L_x":L_x,"L_y":L_y,"L_z":L_z,
                      "rey":rey,"utau":utau,"cmap_flag":False})
plotstruc3d_separe(data_in={"struc1":shap_struc,"struc2":uv_struc,"struc3":streak_struc,"struc4":chong_struc,
                            "plot_folder":plot_folder,"xlabel":fig2_xlabel,"ylabel":fig2_ylabel,"zlabel":fig2_zlabel,
                            "fontsize":fig2_fontsize,"figsize_x":fig2_figsize_x,"figsize_y":fig2_figsize_y,
                            "colormap1":fig2_colormap1,"colormap2":fig2_colormap2,"colormap3":fig2_colormap3,
                            "colormap4":fig2_colormap4,"colornum":fig2_colornum,"fig_name":fig2_name,"dpi":fig2_dpi,
                            "dy":dy,"dx":dx,"dz":dz,"uvw_folder":uvw_folder,"uvw_file":uvw_file,"L_x":L_x,"L_y":L_y,
                            "L_z":L_z,"rey":rey,"utau":utau,"cmap_flag":False})

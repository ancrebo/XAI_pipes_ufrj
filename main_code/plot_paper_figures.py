# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------------------------------------------------
plot_paper_figures.py
-------------------------------------------------------------------------------------------------------------------------
Created on Tue Jun 18 09:52:56 2024

@author: Andres Cremades Botella

Creates all the plots required for the paper.
- Figure 1: (Not python, sketch powerpoint)
- Figure 2: Visualization of a structure of each type
- Figure 3: u+ vs y+
- Figure 4: Coincidence percentage
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
fig2_fontsize    = 12
fig2_figsize_x   = 7
fig2_figsize_y   = 5
fig2_colormap    = "viridis"
fig2_colornum    = 4
fig2a_name       = "figure2a"
fig2b_name       = "figure2b"
fig2c_name       = "figure2c"
fig2d_name       = "figure2d"
fig2_dpi         = 200
plot_folder      = "paper_figures"
index            = 7000

# -----------------------------------------------------------------------------------------------------------------------
# Define the variables required for the plot
#     - fig3_ylabel                   : label of the y axis in figure 3
#     - fig3_xlabelu                  : label of the x axis for the streamwise velocity in figure 3
#     - fig3_xlabelv                  : label of the x axis for the wall-normal velocity in figure 3
#     - fig3_xlabelw                  : label of the x axis for the spanwise velocity in figure 3
#     - fig3_fontsize                 : size of the text in the figure 3
#     - fig3_figsize_x                : size of the figure 3 in axis x
#     - fig3_figsize_y                : size of the figure 3 in axis y
#     - fig3_colormap                 : colormap used in the plot in figure 3
#     - fig3_colornum                 : number of levels required in the colormap in figure 3
#     - fig3_dpi                      : dots per inch of the figure 3
#     - fig3_plot_fileu               : name of the figure 3 of the streamwise velocity after saving
#     - fig3_plot_filev               : name of the figure 3 of the wall-normal velocity after saving
#     - fig3_plot_filew               : name of the figure 3 of the spanwise velocity after saving
#     - fig3_bins                     : bins used in the histograms in figure 3
#     - fig3_lev_min                  : minimum level of the histograms in figure 3
#     - fig3_lev_delta                : separation between the levels of the histograms in figure 3. If None equally 
#                                       distributed in the log scale.   
# -----------------------------------------------------------------------------------------------------------------------
fig3_ylabel           = "$y^+$"
fig3_xlabelu          = "$u^+$"
fig3_xlabelv          = "$v^+$"
fig3_xlabelw          = "$w^+$"
fig3_fontsize         = 18
fig3_figsize_x        = 7
fig3_figsize_y        = 5
fig3_colormap         = "viridis"
fig3_colornum         = 4
fig3_dpi              = 200
fig3_plot_fileu       = "figure3_uy"
fig3_plot_filev       = "figure3_vy"
fig3_plot_filew       = "figure3_wy"
fig3_bins             = 200
fig3_lev_min          = 1e-3
fig3_lev_delta        = None


# -----------------------------------------------------------------------------------------------------------------------
# Define the variables required for the plot
#     - fig4_xlabel      : label of the x axis in figure 4
#     - fig4_ylabel      : label of the y axis in figure 4
#     - fig4_ylabel2     : label of the second y axis in figure 4
#     - fig4_fontsize    : size of the text in the figure 4
#     - fig4_figsize_x   : size of the figure 4 in axis x
#     - fig4_figsize_y   : size of the figure 4 in axis y
#     - fig4_colormap    : colormap used in the plot in figure 4
#     - fig4_colornum    : number of levels required in the colormap in figure 4
#     - fig4_name        : name of the figure 4 after saving
#     - fig4_dpi         : dots per inch of the figure 4
#     - fig4_struc1_lab  : label of the structure 1 of the figure 4
#     - fig4_struc2_lab  : label of the structure 2 of the figure 4
# -----------------------------------------------------------------------------------------------------------------------
fig4_xlabel      = "$y^+$"
fig4_ylabel      = "$V/V_{tot}$"
fig4_ylabel2     = "$Coincidence (\%)$"
fig4_fontsize    = 24
fig4_figsize_x   = 16
fig4_figsize_y   = 5
fig4_colormap    = "viridis"
fig4_colornum    = 4
fig4_name        = "figure4"
fig4_dpi         = 400
fig4_struc1a_lab = "$Q_{SHAP}$"
fig4_struc1b_lab = "Qs"
fig4_struc2a_lab = "$Q_{SHAP}$"
fig4_struc2b_lab = "Streaks"
fig4_struc3a_lab = "$Q_{SHAP}$"
fig4_struc3b_lab = "Vortices"
fig4_linewidth   = 3



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
st_data_str = "stats_data_shap"
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
from py_bin.py_plots.plot_histuvw_y import plot_histuvw_y
from py_bin.py_plots.plotstruc3d import plotstruc3d, plotstruc3d_separe
from py_bin.py_class.flow_field import flow_field
from py_bin.py_plots.plot_coinc import plot_coinc_3coinc
from py_bin.py_functions.read_velocity import read_velocity
import numpy as np

try:
    os.mkdir(plot_folder)
except:
    print("Folder is created",flush=True)

# -----------------------------------------------------------------------------------------------------------------------
# Unlock the h5 files for avoiding problems in some clusters
# -----------------------------------------------------------------------------------------------------------------------
os.environ['HDF5_USE_FILE_LOCKING'] = 'FALSE'

# -----------------------------------------------------------------------------------------------------------------------
# Generate the colors
# -----------------------------------------------------------------------------------------------------------------------
# fig2_colors_4 = matplotlib.cm.get_cmap(fig2_colormap,4).colors
# fig2_colormap1 = fig2_colors_4[0,:]
# fig2_colormap2 = fig2_colors_4[1,:]
# fig2_colormap3 = fig2_colors_4[2,:]
# fig2_colormap4 = fig2_colors_4[3,:]

# -----------------------------------------------------------------------------------------------------------------------
# Import information files
# -----------------------------------------------------------------------------------------------------------------------
exec("from "+folder_def+" import "+chd_str+" as chd")
exec("from "+folder_def+" import "+folders_str+" as folders")
exec("from "+folder_def+" import "+st_data_str+" as st_data")
exec("from "+folder_def+" import "+sh_data_str+" as sh_data")
exec("from "+folder_def+" import "+tr_data_str+" as tr_data")

# # -----------------------------------------------------------------------------------------------------------------------
# # -----------------------------------------------------------------------------------------------------------------------
# # FIGURE 2
# # -----------------------------------------------------------------------------------------------------------------------
# # -----------------------------------------------------------------------------------------------------------------------

# # -----------------------------------------------------------------------------------------------------------------------
# # Data for the statistics:
# #     - index         : index of the field
# #     - Hperc         : percolation index
# #     - uvw_folder    : folder of the flow field data
# #     - uvw_file      : file of the flow field data
# #     - umean_file    : file to save the mean velocity
# #     - data_folder   : folder to store the calculated data
# #     - dx            : downsampling in x
# #     - dy            : downsampling in y
# #     - dz            : downsampling in z
# #     - L_x           : length of the channel in the streamwise direction
# #     - L_y           : half-width of the channel in the wall-normal direction
# #     - L_z           : length of the channel in the spanwise direction
# #     - urms_file     : file to save the rms of the velocity
# #     - rey           : Friction Reynolds number
# #     - utau          : Friction velocity
# #     - padding       : padding of the flow field
# #     - sym_quad      : flag for using the symmetry in the direction 2 of the field for the quadrant selection
# #     - filvol        : volume for filtering the structures+
# #     - shap_folder   : folder of the shap values
# #     - shap_file     : file of the shap values
# #     - SHAPq_folder  : folder of the shap structures
# #     - SHAPq_file    : file of the shap structures
# #     - uv_folder     : folder of the uv structures
# #     - uv_file       : file of the uv structures
# #     - streak_folder : folder of the streaks structures
# #     - streak_file   : file of the streaks structures
# #     - chong_folder  : folder of the chong structures
# #     - chong_file    : file of the chong structures
# #     - padding       : padding of the field
# #     - data_type     : type of data used by the model
# # -----------------------------------------------------------------------------------------------------------------------
# Hperc         = 1.41
# uvw_folder    = folders.uvw_folder
# uvw_file      = folders.uvw_file
# umean_file    = folders.umean_file
# data_folder   = folders.data_folder
# dx            = chd.dx
# dy            = chd.dy
# dz            = chd.dz
# L_x           = chd.L_x
# L_y           = chd.L_y
# L_z           = chd.L_z
# urms_file     = folders.urms_file
# rey           = chd.rey
# utau          = chd.utau
# padding       = chd.padding
# sym_quad      = True
# filvol        = chd.filvol
# shap_folder   = folders.shap_folder
# shap_file     = folders.shap_file
# SHAPq_folder  = folders.SHAPq_folder
# SHAPq_file    = folders.SHAPq_file
# uv_folder     = folders.uv_folder
# uv_file       = folders.uv_file
# streak_folder = folders.streak_folder
# streak_file   = folders.streak_file
# chong_folder  = folders.chong_folder
# chong_file    = folders.chong_file
# padding       = chd.padding
# data_type     = tr_data.data_type
# nsamples      = sh_data.nsamples
# SHAPrms_file  = folders.SHAPrms_file


# # -----------------------------------------------------------------------------------------------------------------------
# # Create the data of the structure
# # -----------------------------------------------------------------------------------------------------------------------
# shap_struc = shap_structure(data_in={"uvw_folder":uvw_folder,"uvw_file":uvw_file,"Hperc":Hperc,"index":index,"dx":dx,
#                                       "dy":dy,"dz":dz,"L_x":L_x,"L_y":L_y,"L_z":L_z,"rey":rey,"utau":utau,
#                                       "padding":padding,"data_folder":data_folder,"umean_file":umean_file,
#                                       "urms_file":urms_file,"sym_quad":True,"filvol":filvol,"shap_folder":shap_folder,
#                                       "shap_file":shap_file,"folder":SHAPq_folder,"file":SHAPq_file,"padding":padding,
#                                       "data_type":data_type,"nsamples":nsamples,"SHAPrms_file":SHAPrms_file})
# shap_struc.read_struc()

# # -----------------------------------------------------------------------------------------------------------------------
# # Create the data of the structure
# # -----------------------------------------------------------------------------------------------------------------------
# uv_struc = uv_structure(data_in={"uvw_folder":uvw_folder,"uvw_file":uvw_file,"Hperc":Hperc,"index":index,"dx":dx,
#                                   "dy":dy,"dz":dz,"L_x":L_x,"L_y":L_y,"L_z":L_z,"rey":rey,"utau":utau,
#                                   "padding":padding,"data_folder":data_folder,"umean_file":umean_file,
#                                   "urms_file":urms_file,"sym_quad":True,"filvol":filvol,"shap_folder":shap_folder,
#                                   "shap_file":shap_file,"folder":uv_folder,"file":uv_file,"padding":padding,
#                                   "data_type":data_type})
# uv_struc.read_struc()

# # -----------------------------------------------------------------------------------------------------------------------
# # Create the data of the structure
# # -----------------------------------------------------------------------------------------------------------------------
# streak_struc = streak_structure(data_in={"uvw_folder":uvw_folder,"uvw_file":uvw_file,"Hperc":Hperc,"index":index,
#                                           "dx":dx,"dy":dy,"dz":dz,"L_x":L_x,"L_y":L_y,"L_z":L_z,"rey":rey,"utau":utau,
#                                           "padding":padding,"data_folder":data_folder,"umean_file":umean_file,
#                                           "urms_file":urms_file,"sym_quad":True,"filvol":filvol,
#                                           "shap_folder":shap_folder,"shap_file":shap_file,"folder":streak_folder,
#                                           "file":streak_file,"padding":padding,"data_type":data_type})
# streak_struc.read_struc()

# # -----------------------------------------------------------------------------------------------------------------------
# # Create the data of the structure
# # -----------------------------------------------------------------------------------------------------------------------
# chong_struc = chong_structure(data_in={"uvw_folder":uvw_folder,"uvw_file":uvw_file,"Hperc":Hperc,"index":index,
#                                         "dx":dx,"dy":dy,"dz":dz,"L_x":L_x,"L_y":L_y,"L_z":L_z,"rey":rey,"utau":utau,
#                                         "padding":padding,"data_folder":data_folder,"umean_file":umean_file,
#                                         "urms_file":urms_file,"sym_quad":True,"filvol":filvol,
#                                         "shap_folder":shap_folder,"shap_file":shap_file,"folder":chong_folder,
#                                         "file":chong_file,"padding":padding,"data_type":data_type})
# chong_struc.read_struc()

# # -----------------------------------------------------------------------------------------------------------------------
# # Plot the 3D field
# # -----------------------------------------------------------------------------------------------------------------------
# plotstruc3d_separe(data_in={"struc":shap_struc,"plot_folder":plot_folder,"xlabel":fig2_xlabel,"ylabel":fig2_ylabel,
#                             "zlabel":fig2_zlabel,"fontsize":fig2_fontsize,"figsize_x":fig2_figsize_x,
#                             "figsize_y":fig2_figsize_y,"colormap":fig2_colormap,"colornum":0,"fig_name":fig2a_name,
#                             "dpi":fig2_dpi,"dy":dy,"dx":dx,"dz":dz,"uvw_folder":uvw_folder,"uvw_file":uvw_file,
#                             "L_x":L_x,"L_y":L_y,"L_z":L_z,"rey":rey,"utau":utau,"cmap_flag":True})
# plotstruc3d_separe(data_in={"struc":uv_struc,"plot_folder":plot_folder,"xlabel":fig2_xlabel,"ylabel":fig2_ylabel,
#                             "zlabel":fig2_zlabel,"fontsize":fig2_fontsize,"figsize_x":fig2_figsize_x,
#                             "figsize_y":fig2_figsize_y,"colormap":fig2_colormap,"colornum":0,"fig_name":fig2b_name,
#                             "dpi":fig2_dpi,"dy":dy,"dx":dx,"dz":dz,"uvw_folder":uvw_folder,"uvw_file":uvw_file,
#                             "L_x":L_x,"L_y":L_y,"L_z":L_z,"rey":rey,"utau":utau,"cmap_flag":True})
# plotstruc3d_separe(data_in={"struc":streak_struc,"plot_folder":plot_folder,"xlabel":fig2_xlabel,"ylabel":fig2_ylabel,
#                             "zlabel":fig2_zlabel,"fontsize":fig2_fontsize,"figsize_x":fig2_figsize_x,
#                             "figsize_y":fig2_figsize_y,"colormap":fig2_colormap,"colornum":0,"fig_name":fig2c_name,
#                             "dpi":fig2_dpi,"dy":dy,"dx":dx,"dz":dz,"uvw_folder":uvw_folder,"uvw_file":uvw_file,
#                             "L_x":L_x,"L_y":L_y,"L_z":L_z,"rey":rey,"utau":utau,"cmap_flag":True})
# plotstruc3d_separe(data_in={"struc":chong_struc,"plot_folder":plot_folder,"xlabel":fig2_xlabel,"ylabel":fig2_ylabel,
#                             "zlabel":fig2_zlabel,"fontsize":fig2_fontsize,"figsize_x":fig2_figsize_x,
#                             "figsize_y":fig2_figsize_y,"colormap":fig2_colormap,"colornum":0,"fig_name":fig2d_name,
#                             "dpi":fig2_dpi,"dy":dy,"dx":dx,"dz":dz,"uvw_folder":uvw_folder,"uvw_file":uvw_file,
#                             "L_x":L_x,"L_y":L_y,"L_z":L_z,"rey":rey,"utau":utau,"cmap_flag":True})


# # -----------------------------------------------------------------------------------------------------------------------
# # -----------------------------------------------------------------------------------------------------------------------
# # FIGURE 3
# # -----------------------------------------------------------------------------------------------------------------------
# # -----------------------------------------------------------------------------------------------------------------------


# # -----------------------------------------------------------------------------------------------------------------------
# # Data for the statistics:
# #     - index                  : index of the field
# #     - Hperc                  : percolation index
# #     - uvw_folder             : folder of the flow field data
# #     - uvw_file               : file of the flow field data
# #     - umean_file             : file to save the mean velocity
# #     - data_folder            : folder to store the calculated data
# #     - dx                     : downsampling in x
# #     - dy                     : downsampling in y
# #     - dz                     : downsampling in z
# #     - L_x                    : length of the channel in the streamwise direction
# #     - L_y                    : half-width of the channel in the wall-normal direction
# #     - L_z                    : length of the channel in the spanwise direction
# #     - urms_file              : file to save the rms of the velocity
# #     - rey                    : Friction Reynolds number
# #     - utau                   : Friction velocity
# #     - padding                : padding of the flow field
# #     - sym_quad               : flag for using the symmetry in the direction 2 of the field for the quadrant selection
# #     - filvol                 : volume for filtering the structures+
# #     - shap_folder            : folder of the shap values
# #     - shap_folder            : file of the shap values
# #     - padding                : padding of the field
# #     - data_type              : type of data used by the model
# #     - SHAPq_intensity_folder : folder of the intense shap structures
# #     - SHAPq_intensity_file   : file of the intense shap structures
# #     - nsamples               : number of samples of the shap calculation
# #     - SHAPrms_file           : file of the rms of the shap
# #     - SHAPmean_file          : file of the mean of the shap
# # -----------------------------------------------------------------------------------------------------------------------
# index_ini              = st_data.field_ini
# index_fin              = st_data.field_fin
# index_delta            = st_data.field_delta*10
# Hperc                  = 1.41
# uvw_folder             = folders.uvw_folder
# uvw_file               = folders.uvw_file
# umean_file             = folders.umean_file
# data_folder            = folders.data_folder
# dx                     = chd.dx
# dy                     = chd.dy
# dz                     = chd.dz
# L_x                    = chd.L_x
# L_y                    = chd.L_y
# L_z                    = chd.L_z
# urms_file              = folders.urms_file
# rey                    = chd.rey
# utau                   = chd.utau
# padding                = chd.padding
# sym_quad               = True
# filvol                 = chd.filvol
# shap_folder            = folders.shap_folder
# shap_file              = folders.shap_file
# padding                = chd.padding
# data_type              = tr_data.data_type
# SHAPq_intensity_folder = folders.SHAPq_folder
# SHAPq_intensity_file   = folders.SHAPq_file
# uv_folder              = folders.uv_folder
# uv_file                = folders.uv_file
# streak_folder          = folders.streak_folder
# streak_file            = folders.streak_file
# chong_folder           = folders.chong_folder
# chong_file             = folders.chong_file
# nsamples               = sh_data.nsamples
# SHAPrms_file           = folders.SHAPrms_file
# SHAPmean_file          = folders.SHAPmean_file
# streak_shap_file       = folders.streak_shap_file
# umax_file              = folders.umax_file


# # -----------------------------------------------------------------------------------------------------------------------
# # Read the channel characteristics
# # -----------------------------------------------------------------------------------------------------------------------
# Data_flow = {"folder":uvw_folder,"file":uvw_file,"down_x":dx,"down_y":dy,
#               "down_z":dz,"L_x":L_x,"L_y":L_y,"L_z":L_z,"rey":rey,"utau":utau,"umax_file":umax_file}
# flowfield = flow_field(data_in=Data_flow)
# flowfield.shape_tensor()
# flowfield.flow_grid()

# # -----------------------------------------------------------------------------------------------------------------------
# # Create the data of the shap structure and read where the structures exist
# # -----------------------------------------------------------------------------------------------------------------------
# shap_data  = {"uvw_folder":uvw_folder,"uvw_file":uvw_file,"Hperc":Hperc,"index":0,"dx":dx,
#               "dy":dy,"dz":dz,"L_x":L_x,"L_y":L_y,"L_z":L_z,"rey":rey,"utau":utau,
#               "padding":padding,"data_folder":data_folder,"umean_file":umean_file,
#               "urms_file":urms_file,"sym_quad":True,"filvol":filvol,"shap_folder":shap_folder,
#               "shap_file":shap_file,"folder":SHAPq_intensity_folder,"file":SHAPq_intensity_file,"padding":padding,
#               "data_type":data_type,"nsamples":nsamples,"SHAPrms_file":SHAPrms_file,"SHAPmean_file":SHAPmean_file}
# uv_data  = {"uvw_folder":uvw_folder,"uvw_file":uvw_file,"Hperc":Hperc,"index":0,"dx":dx,
#             "dy":dy,"dz":dz,"L_x":L_x,"L_y":L_y,"L_z":L_z,"rey":rey,"utau":utau,
#             "padding":padding,"data_folder":data_folder,"umean_file":umean_file,
#             "urms_file":urms_file,"sym_quad":True,"filvol":filvol,"shap_folder":shap_folder,
#             "shap_file":shap_file,"folder":uv_folder,"file":uv_file,"padding":padding,
#             "data_type":data_type}
# streak_data  = {"uvw_folder":uvw_folder,"uvw_file":uvw_file,"Hperc":Hperc,"index":0,"dx":dx,
#                 "dy":dy,"dz":dz,"L_x":L_x,"L_y":L_y,"L_z":L_z,"rey":rey,"utau":utau,
#                 "padding":padding,"data_folder":data_folder,"umean_file":umean_file,
#                 "urms_file":urms_file,"sym_quad":True,"filvol":filvol,"shap_folder":shap_folder,
#                 "shap_file":shap_file,"folder":streak_folder,"file":streak_file,"padding":padding,
#                 "data_type":data_type}
# chong_data  = {"uvw_folder":uvw_folder,"uvw_file":uvw_file,"Hperc":Hperc,"index":0,"dx":dx,
#                 "dy":dy,"dz":dz,"L_x":L_x,"L_y":L_y,"L_z":L_z,"rey":rey,"utau":utau,
#                 "padding":padding,"data_folder":data_folder,"umean_file":umean_file,
#                 "urms_file":urms_file,"sym_quad":True,"filvol":filvol,"shap_folder":shap_folder,
#                 "shap_file":shap_file,"folder":chong_folder,"file":chong_file,"padding":padding,
#                 "data_type":data_type}
# velo_data  = {"folder":uvw_folder,"file":uvw_file,"index":0,"dx":dx,"dy":dy,"dz":dz,
#               "shpx":flowfield.shpx,"shpy":flowfield.shpy,"shpz":flowfield.shpz,
#               "padding":0,"data_folder":data_folder,"umean_file":umean_file}



# # -----------------------------------------------------------------------------------------------------------------------
# # SHAP structures for all the fields
# # -----------------------------------------------------------------------------------------------------------------------
# index_range = range(index_ini,index_fin,index_delta)
# for ii in index_range:  
#     shap_data["index"] = ii
#     velo_data["index"] = ii
#     # -----------------------------------------------------------------------------------------------------------------------
#     # Read the velocity
#     # -----------------------------------------------------------------------------------------------------------------------
#     shap_struc    = shap_structure(data_in=shap_data)
#     shap_struc.read_struc()
#     mat_struc     = shap_struc.mat_struc
#     velocity_data = read_velocity(data_in=velo_data)
#     uu            = velocity_data["uu"]/utau
#     vv            = velocity_data["vv"]/utau
#     ww            = velocity_data["ww"]/utau
    
#     # -----------------------------------------------------------------------------------------------------------------------
#     # Velocities of the structues
#     # -----------------------------------------------------------------------------------------------------------------------
#     index_st    = np.where(mat_struc==1)
#     if ii == index_range[0]:
#         uu_struc    = uu[index_st]
#         vv_struc    = vv[index_st]
#         ww_struc    = ww[index_st]
#         y_h_struc   = flowfield.y_h[index_st[0]]
#         yplus_struc = (1-abs(y_h_struc))*rey
#     else:
#         uu_struc    = np.concatenate((uu_struc,uu[index_st]))
#         vv_struc    = np.concatenate((vv_struc,vv[index_st]))
#         ww_struc    = np.concatenate((ww_struc,ww[index_st]))
#         y_h_struc   = flowfield.y_h[index_st[0]]
#         yplus_struc = np.concatenate((yplus_struc,(1-abs(y_h_struc))*rey))
        
        

# # -----------------------------------------------------------------------------------------------------------------------
# # Plot the data
# # -----------------------------------------------------------------------------------------------------------------------
# plot_format_data = {"plot_folder":plot_folder,"plot_fileu":fig3_plot_fileu+"_shap","plot_filev":fig3_plot_filev+"_shap",
#                     "plot_filew":fig3_plot_filew+"_shap","ylabel":fig3_ylabel,"xlabelu":fig3_xlabelu,
#                     "xlabelv":fig3_xlabelv,"xlabelw":fig3_xlabelw,"fontsize":fig3_fontsize,
#                     "figsize_x":fig3_figsize_x,"figsize_y":fig3_figsize_y,"colormap":fig3_colormap,
#                     "colornum":fig3_colornum,"dpi":fig3_dpi,"uu_struc":uu_struc,"vv_struc":vv_struc,
#                     "ww_struc":ww_struc,"yplus_struc":yplus_struc,"yplusmesh":flowfield.yplus,
#                     "bins":fig3_bins,"lev_min":fig3_lev_min,"lev_delta":fig3_lev_delta}
# plot_histuvw_y(data_in=plot_format_data)


# # -----------------------------------------------------------------------------------------------------------------------
# # uv structures for all the fields
# # -----------------------------------------------------------------------------------------------------------------------
# index_range = range(index_ini,index_fin,index_delta)
# for ii in index_range:  
#     uv_data["index"]   = ii
#     velo_data["index"] = ii
#     # -----------------------------------------------------------------------------------------------------------------------
#     # Read the velocity
#     # -----------------------------------------------------------------------------------------------------------------------
#     uv_struc      = uv_structure(data_in=uv_data)
#     uv_struc.read_struc()
#     mat_struc     = uv_struc.mat_struc
#     velocity_data = read_velocity(data_in=velo_data)
#     uu            = velocity_data["uu"]/utau
#     vv            = velocity_data["vv"]/utau
#     ww            = velocity_data["ww"]/utau
    
#     # -----------------------------------------------------------------------------------------------------------------------
#     # Velocities of the structues
#     # -----------------------------------------------------------------------------------------------------------------------
#     index_st    = np.where(mat_struc==1)
#     if ii == index_range[0]:
#         uu_struc    = uu[index_st]
#         vv_struc    = vv[index_st]
#         ww_struc    = ww[index_st]
#         y_h_struc   = flowfield.y_h[index_st[0]]
#         yplus_struc = (1-abs(y_h_struc))*rey
#     else:
#         uu_struc    = np.concatenate((uu_struc,uu[index_st]))
#         vv_struc    = np.concatenate((vv_struc,vv[index_st]))
#         ww_struc    = np.concatenate((ww_struc,ww[index_st]))
#         y_h_struc   = flowfield.y_h[index_st[0]]
#         yplus_struc = np.concatenate((yplus_struc,(1-abs(y_h_struc))*rey))

# # -----------------------------------------------------------------------------------------------------------------------
# # Plot the data
# # -----------------------------------------------------------------------------------------------------------------------
# plot_format_data = {"plot_folder":plot_folder,"plot_fileu":fig3_plot_fileu+"_uv","plot_filev":fig3_plot_filev+"_uv",
#                     "plot_filew":fig3_plot_filew+"_uv","ylabel":fig3_ylabel,"xlabelu":fig3_xlabelu,
#                     "xlabelv":fig3_xlabelv,"xlabelw":fig3_xlabelw,"fontsize":fig3_fontsize,"figsize_x":fig3_figsize_x,
#                     "figsize_y":fig3_figsize_y,"colormap":fig3_colormap,"colornum":fig3_colornum,"dpi":fig3_dpi,
#                     "uu_struc":uu_struc,"vv_struc":vv_struc,"ww_struc":ww_struc,"yplus_struc":yplus_struc,
#                     "yplusmesh":flowfield.yplus,"bins":fig3_bins,"lev_min":fig3_lev_min,"lev_delta":fig3_lev_delta}
# plot_histuvw_y(data_in=plot_format_data)

# # -----------------------------------------------------------------------------------------------------------------------
# # Streaks for all the fields
# # -----------------------------------------------------------------------------------------------------------------------
# index_range = range(index_ini,index_fin,index_delta)
# for ii in index_range:  
#     streak_data["index"] = ii
#     velo_data["index"]   = ii
#     # -----------------------------------------------------------------------------------------------------------------------
#     # Read the velocity
#     # -----------------------------------------------------------------------------------------------------------------------
#     streak_struc  = streak_structure(data_in=streak_data)
#     streak_struc.read_struc()
#     mat_struc     = streak_struc.mat_struc
#     velocity_data = read_velocity(data_in=velo_data)
#     uu            = velocity_data["uu"]/utau
#     vv            = velocity_data["vv"]/utau
#     ww            = velocity_data["ww"]/utau
    
#     # -----------------------------------------------------------------------------------------------------------------------
#     # Velocities of the structues
#     # -----------------------------------------------------------------------------------------------------------------------
#     index_st    = np.where(mat_struc==1)
#     if ii == index_range[0]:
#         uu_struc    = uu[index_st]
#         vv_struc    = vv[index_st]
#         ww_struc    = ww[index_st]
#         y_h_struc   = flowfield.y_h[index_st[0]]
#         yplus_struc = (1-abs(y_h_struc))*rey
#     else:
#         uu_struc    = np.concatenate((uu_struc,uu[index_st]))
#         vv_struc    = np.concatenate((vv_struc,vv[index_st]))
#         ww_struc    = np.concatenate((ww_struc,ww[index_st]))
#         y_h_struc   = flowfield.y_h[index_st[0]]
#         yplus_struc = np.concatenate((yplus_struc,(1-abs(y_h_struc))*rey))

# # -----------------------------------------------------------------------------------------------------------------------
# # Plot the data
# # -----------------------------------------------------------------------------------------------------------------------
# plot_format_data = {"plot_folder":plot_folder,"plot_fileu":fig3_plot_fileu+"_streak",
#                     "plot_filev":fig3_plot_filev+"_streak","plot_filew":fig3_plot_filew+"_streak",
#                     "ylabel":fig3_ylabel,"xlabelu":fig3_xlabelu,"xlabelv":fig3_xlabelv,"xlabelw":fig3_xlabelw,
#                     "fontsize":fig3_fontsize,"figsize_x":fig3_figsize_x,"figsize_y":fig3_figsize_y,
#                     "colormap":fig3_colormap,"colornum":fig3_colornum,"dpi":fig3_dpi,
#                     "uu_struc":uu_struc,"vv_struc":vv_struc,"ww_struc":ww_struc,"yplus_struc":yplus_struc,
#                     "yplusmesh":flowfield.yplus,"bins":fig3_bins,"lev_min":fig3_lev_min,"lev_delta":fig3_lev_delta}
# plot_histuvw_y(data_in=plot_format_data)

# # -----------------------------------------------------------------------------------------------------------------------
# # Chong for all the fields
# # -----------------------------------------------------------------------------------------------------------------------
# index_range = range(index_ini,index_fin,index_delta)
# for ii in index_range:  
#     chong_data["index"] = ii
#     velo_data["index"]  = ii
#     # -----------------------------------------------------------------------------------------------------------------------
#     # Read the velocity
#     # -----------------------------------------------------------------------------------------------------------------------
#     chong_struc  = chong_structure(data_in=chong_data)
#     chong_struc.read_struc()
#     mat_struc     = chong_struc.mat_struc
#     velocity_data = read_velocity(data_in=velo_data)
#     uu            = velocity_data["uu"]
#     vv            = velocity_data["vv"]
#     ww            = velocity_data["ww"]
    
#     # -----------------------------------------------------------------------------------------------------------------------
#     # Velocities of the structues
#     # -----------------------------------------------------------------------------------------------------------------------
#     index_st    = np.where(mat_struc==1)
#     if ii == index_range[0]:
#         uu_struc    = uu[index_st]/utau
#         vv_struc    = vv[index_st]/utau
#         ww_struc    = ww[index_st]/utau
#         y_h_struc   = flowfield.y_h[index_st[0]]
#         yplus_struc = (1-abs(y_h_struc))*rey
#     else:
#         uu_struc    = np.concatenate((uu_struc,uu[index_st]))
#         vv_struc    = np.concatenate((vv_struc,vv[index_st]))
#         ww_struc    = np.concatenate((ww_struc,ww[index_st]))
#         y_h_struc   = flowfield.y_h[index_st[0]]
#         yplus_struc = np.concatenate((yplus_struc,(1-abs(y_h_struc))*rey))

# # -----------------------------------------------------------------------------------------------------------------------
# # Plot the data
# # -----------------------------------------------------------------------------------------------------------------------
# plot_format_data = {"plot_folder":plot_folder,"plot_fileu":fig3_plot_fileu+"_chong","plot_filev":fig3_plot_filev+"_chong",
#                     "plot_filew":fig3_plot_filew+"_chong","ylabel":fig3_ylabel,"xlabelu":fig3_xlabelu,
#                     "xlabelv":fig3_xlabelv,"xlabelw":fig3_xlabelw,"fontsize":fig3_fontsize,
#                     "figsize_x":fig3_figsize_x,"figsize_y":fig3_figsize_y,"colormap":fig3_colormap,
#                     "colornum":fig3_colornum,"dpi":fig3_dpi,"uu_struc":uu_struc,"vv_struc":vv_struc,
#                     "ww_struc":ww_struc,"yplus_struc":yplus_struc,"yplusmesh":flowfield.yplus,"bins":fig3_bins,
#                     "lev_min":fig3_lev_min,"lev_delta":fig3_lev_delta}
# plot_histuvw_y(data_in=plot_format_data)


# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# FIGURE 4
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

# -----------------------------------------------------------------------------------------------------------------------
# Define the information of the data
#     - data_folder : folder containing the training data
#     - plot_folder : folder to save the figures
#     - file        : name of the file containing the mean velocity information
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
data_folder = folders.data_folder
file_uv     = folders.uv_shap_file
file_streak = folders.streak_shap_file
file_chong  = folders.chong_shap_file

# -----------------------------------------------------------------------------------------------------------------------
# Create the plot
# -----------------------------------------------------------------------------------------------------------------------
plot_format_data = {"file_1":file_uv,"file_2":file_streak,"file_3":file_chong,"folder":data_folder,
                    "plot_folder":plot_folder,"xlabel":fig4_xlabel,"ylabel":fig4_ylabel,"ylabel2":fig4_ylabel2,
                    "fontsize":fig4_fontsize,"figsize_x":fig4_figsize_x,"figsize_y":fig4_figsize_y,
                    "colormap":fig4_colormap,"colornum":fig4_colornum,"fig_name":fig4_name,"dpi":fig4_dpi,
                    "struc1a_lab":fig4_struc1a_lab,"struc1b_lab":fig4_struc1b_lab,"struc2a_lab":fig4_struc2a_lab,
                    "struc2b_lab":fig4_struc2b_lab,"struc3a_lab":fig4_struc3a_lab,"struc3b_lab":fig4_struc3b_lab,
                    "linewidth":fig4_linewidth}
plot_coinc_3coinc(data_in=plot_format_data)


# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------------------------------------------------
plot_histuvw_ejection_sweeps_streakslow_streakshigh_vortices_vs_volume.py
-------------------------------------------------------------------------------------------------------------------------
Created on Mon Dec  2 08:56:03 2024

@author: Andres Cremades Botella

Function to plot the histogram of the ejections, sweeps, high and low velocity streaks and vortices against the volume:
    - folder_def  : (str) name of the folder containing the files for configuring the case of analysis.
    - chd_str     : (str) name of the file containing the data of the channel.
    - folders_str : (str) name of the file containing the folders and files used in the problem.
    - st_data_str : (str) name of the file containing the information required for the statistics.
"""
# -----------------------------------------------------------------------------------------------------------------------
# Define the names of the files containing the definitios of the parameters
# - folder_def : folder containing the files with the definitions required in the problem
# - chd_str    : file containing the data of the channel
# - folders    : file containing the folder and file structures
# - st_data    : file containing the data of the statistics
# -----------------------------------------------------------------------------------------------------------------------
folder_def  = "P125_83pi_240603_v0_definitions"
chd_str     = "channel_data"
folders_str = "folders_msi"
st_data_str = "stats_data_shap"
sh_data_str = "shap_data"
tr_data_str = "training_data"

# -----------------------------------------------------------------------------------------------------------------------
# Import packages
# -----------------------------------------------------------------------------------------------------------------------
from py_bin.py_class.uv_structure import uv_structure
from py_bin.py_class.shap_config import shap_config
import os
from py_bin.py_plots.plot_histstruc_5 import plot_histstruc_5_lowmem
from py_bin.py_class.flow_field import flow_field
from py_bin.py_functions.read_velocity import read_velocity
import numpy as np
import h5py

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
# Define the variables required for the plot
#     - xlabel                   : label of the x axis
#     - ylabelu                  : label of the y axis for the streamwise velocity
#     - ylabelv                  : label of the y axis for the wall-normal velocity
#     - ylabelw                  : label of the y axis for the spanwise velocity
#     - fontsize                 : size of the text in the figure
#     - figsize_x                : size of the figure in axis x
#     - figsize_y                : size of the figure in axis y
#     - colormap                 : colormap used in the plot
#     - colornum                 : number of levels required in the colormap
#     - fig_name                 : name of the figure after saving
#     - dpi                      : dots per inch of the figure
#     - struc1_lab               : label of the structure 1
#     - struc2_lab               : label of the structure 2
#     - plot_coin_folder_uv_shap : folder to save the coincidence plots between uv and shap structures
#     - plot_coin_file_uv_shap   : folder to save the coincidence plots between uv and shap structures
# -----------------------------------------------------------------------------------------------------------------------
ylabel           = "$\phi$"
xlabel           = "$V^+$"
fontsize         = 24
figsize_x        = 7
figsize_y        = 6
colormap1        = '#440154'
colormap2        = '#009E73'
colormap3        = '#F0E442'
colormap4        = '#0072B2'
colormap5        = '#E69F00' 
colornum         = 4
dpi              = 400
plot_file        = "hist_Q24_streak_vort_vs_vol_83pi"
bins             = 100
lev_min          = 1e-3
lev_delta        = None
linewidth        = 3
shapmin          = 0
shapmax          = 8
Vmin             = 0
Vmax             = 4
saveh5           = "save_histogram_Q24_streak_vort_vs_vol.h5"

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
#     - padding       : padding of the field
#     - data_type     : type of data used by the model
#     - chong_folder  : folder of the uv structures
#     - chong_file    : file of the uv structures
#     - nsamples      : number of samples of the shap calculation
#     - SHAPrms_file  : file of the rms of the shap
# -----------------------------------------------------------------------------------------------------------------------
index_ini        = st_data.field_ini
index_fin        = st_data.field_fin
index_delta      = st_data.field_delta
Hperc            = 1.41
uvw_folder       = folders.uvw_folder
uvw_file         = folders.uvw_file
umean_file       = folders.umean_file
data_folder      = folders.data_folder
dx               = chd.dx
dy               = chd.dy
dz               = chd.dz
L_x              = chd.L_x
L_y              = chd.L_y
L_z              = chd.L_z
urms_file        = folders.urms_file
rey              = chd.rey
utau             = chd.utau
padding          = chd.padding
sym_quad         = True
filvol           = chd.filvol
shap_folder      = folders.shap_folder
shap_file        = folders.shap_file
padding          = chd.padding
data_type        = tr_data.data_type
plot_folder      = folders.plot_folder
uv_folder        = folders.uv_folder
uv_file          = folders.uv_file
umax_file        = folders.umax_file
shapfolder       = folders.shapseg_uv_folder
shapfile         = folders.shapseg_uv_file
shapfolder_uv    = folders.shapseg_uv_folder
shapfile_uv      = folders.shapseg_uv_file



# -----------------------------------------------------------------------------------------------------------------------
# Read the channel characteristics
# -----------------------------------------------------------------------------------------------------------------------
Data_flow = {"folder":uvw_folder,"file":uvw_file,"down_x":dx,"down_y":dy,
             "down_z":dz,"L_x":L_x,"L_y":L_y,"L_z":L_z,"rey":rey,"utau":utau,"umax_file":umax_file}
flowfield = flow_field(data_in=Data_flow)
flowfield.shape_tensor()
flowfield.flow_grid()

# -----------------------------------------------------------------------------------------------------------------------
# Create the data of the structures and read where the structures exist
# -----------------------------------------------------------------------------------------------------------------------
uv_data    = {"uvw_folder":uvw_folder,"uvw_file":uvw_file,"Hperc":Hperc,"index":0,"dx":dx,
              "dy":dy,"dz":dz,"L_x":L_x,"L_y":L_y,"L_z":L_z,"rey":rey,"utau":utau,
              "padding":padding,"data_folder":data_folder,"umean_file":umean_file,
              "urms_file":urms_file,"sym_quad":True,"filvol":filvol,"shap_folder":shap_folder,
              "shap_file":shap_file,"folder":uv_folder,"file":uv_file,"padding":padding,
              "data_type":data_type}

# -----------------------------------------------------------------------------------------------------------------------
# Create the data for reading the shap values
# -----------------------------------------------------------------------------------------------------------------------
data_shap = {"uvw_folder":uvw_folder,"uvw_file":uvw_file,
             "padding":padding,"dx":dx,"dy":dy,"dz":dz,"data_folder":data_folder,"umean_file":umean_file,
             "unorm_file":"-","L_x":L_x,"L_z":L_z,"L_y":L_y,"rey":rey,"utau":utau,"ngpu":None,
             "field_ini":0,"field_fin":0,"field_delta":1,"model_folder":"-","model_read":"-",
             "nfil":0,"stride":0,"activation":"-","kernel":0,"pooling":0,"delta_pred":1,
             "nsamples":0,"nsamples_max":0,"data_type":"float32",
             "error_file":"-","umax_file":"-","urmspred_file":"-","mean_norm":False,"tfrecord_folder":'-',
             "nrep_field":None,"shap_batch":0,"repeat_exist":False,"flag_model":False,"read_model":False}

# -----------------------------------------------------------------------------------------------------------------------
# For all the fields
# -----------------------------------------------------------------------------------------------------------------------
index_range = range(index_ini,index_fin,index_delta)
grid_Q2     = np.zeros((bins-1,bins-1))
grid_Q4     = np.zeros((bins-1,bins-1))
binsshap    = np.linspace(shapmin,shapmax,bins)
binsV       = np.linspace(Vmin,Vmax,bins)

for ii in index_range:  
    uv_data["index"]    = ii
    # -----------------------------------------------------------------------------------------------------------------------
    # Read the velocity
    # -----------------------------------------------------------------------------------------------------------------------
    uv_struc                 = uv_structure(data_in=uv_data)
    uv_struc.read_struc()
    uv_struc.detect_quadrant()
    ind_vol                  = np.where(uv_struc.structures.vol>uv_struc.structures.filvol)
    vol_Q                    = uv_struc.structures.vol[ind_vol]
    vol_Q2                   = vol_Q[uv_struc.event[ind_vol]==2]
    vol_Q4                   = vol_Q[uv_struc.event[ind_vol]==4]
    data_shap["shap_folder"] = shapfolder_uv
    data_shap["shap_file"]   = shapfile_uv
    shconf                   = shap_config(data_in = data_shap)
    data_shap                = shconf.read_shap_kernel(data_in = {"index":ii})
    shap                     = abs(data_shap["SHAP"])
    shap_ind                 = np.array(data_shap["index_filtered"],dtype='int')
    shap_Q2                  = shap[uv_struc.event[ind_vol]==2]
    shap_Q4                  = shap[uv_struc.event[ind_vol]==4]
    
    # ----------------------------------------------------------------------------------------------------------------
    # Calculate the pdf for the Q2
    # ----------------------------------------------------------------------------------------------------------------
    hist_Q2,hist_vol,hist_shap = np.histogram2d(vol_Q2,shap_Q2,bins=(binsV,binsshap))
    hist_vol                   = hist_vol[:-1]+np.diff(hist_vol)/2
    hist_shap                  = hist_shap[:-1]+np.diff(hist_shap)/2
    grid_vol,grid_shap         = np.meshgrid(hist_vol,hist_shap)
    grid_Q2                   += hist_Q2.T.copy()
    
    
    # ----------------------------------------------------------------------------------------------------------------
    # Calculate the pdf for the Q4
    # ----------------------------------------------------------------------------------------------------------------
    hist_Q4,hist_vol,hist_shap = np.histogram2d(vol_Q4,shap_Q4,bins=(binsV,binsshap))
    hist_vol                   = hist_vol[:-1]+np.diff(hist_vol)/2
    hist_shap                  = hist_shap[:-1]+np.diff(hist_shap)/2
    grid_vol,grid_shap         = np.meshgrid(hist_vol,hist_shap)
    grid_Q4                   += hist_Q4.T.copy()
   
    # -----------------------------------------------------------------------------------------------------------------
    # Save the data
    # -----------------------------------------------------------------------------------------------------------------
    fileh5save = h5py.File(data_folder+'/'+saveh5,'w')
    fileh5save.create_dataset('grid_vol',data=grid_vol)
    fileh5save.create_dataset('grid_shap',data=grid_shap)
    fileh5save.create_dataset('grid_Q2',data=grid_Q2)
    fileh5save.create_dataset('grid_Q4',data=grid_Q4)
    fileh5save.create_dataset('index',data=ii)
    fileh5save.close()


# -----------------------------------------------------------------------------------------------------------------------
# Plot the data
# -----------------------------------------------------------------------------------------------------------------------
plot_format_data = {"plot_folder":plot_folder,"plot_file":plot_file,
                    "ylabel":ylabel,"xlabel":xlabel,"fontsize":fontsize,"figsize_x":figsize_x,"figsize_y":figsize_y,
                    "colormap1":colormap1,"colormap2":colormap2,"colormap3":colormap3,"colormap4":colormap4,
                    "colormap5":colormap5,"colornum":colornum,"dpi":dpi,"grid_1":grid_Q2,"grid_2":grid_Q4,"grid_3":[],
                    "grid_4":[],"grid_5":[],"grid_x":grid_vol,"grid_y":grid_shap,"lev_min":lev_min,"lev_delta":lev_delta,
                    "linewidth":linewidth,"xmin":Vmin,"xmax":Vmax,"ymin":shapmin,"ymax":shapmax}
plot_histstruc_5_lowmem(data_in=plot_format_data)
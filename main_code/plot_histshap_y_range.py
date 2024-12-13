# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------------------------------------------------
plot_histshap_y.py
-------------------------------------------------------------------------------------------------------------------------
Created on Tue Jun 18 11:30:49 2024

@author: Andres Cremades Botella

Function to plot the pdf of the SHAP values as a function of the wall-normal distance:
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
folder_def  = "d20240603_definitions"
chd_str     = "channel_data"
folders_str = "folders"
st_data_str = "stats_data_shap"
sh_data_str = "shap_data"
tr_data_str = "training_data"

# -----------------------------------------------------------------------------------------------------------------------
# Import packages
# -----------------------------------------------------------------------------------------------------------------------
import os
from py_bin.py_plots.plot_hist_y import plot_hist_y_withhist
from py_bin.py_class.flow_field import flow_field
from py_bin.py_functions.read_velocity import read_velocity
from py_bin.py_class.shap_config import shap_config
import numpy as np

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
#     - fac_shap                 : factor to scale the shap value
# -----------------------------------------------------------------------------------------------------------------------
ylabel           = "$y^+$"
xlabelu          = "$\phi_u$"
xlabelv          = "$\phi_v$"
xlabelw          = "$\phi_w$"
xlabelm          = "$|\phi|$"
fontsize         = 24
figsize_x        = 7
figsize_y        = 5
colormap         = "viridis"
colornum         = 4
dpi              = 200
plot_fileu       = "hist_shapu_y"
plot_filev       = "hist_shapv_y"
plot_filew       = "hist_shapw_y"
plot_filem       = "hist_shapm_y"
bins             = 1000
lev_min          = 1e-4
lev_delta        = None
fac_shap         = 1e5
str_facexp       = '{0:.1f}'.format(np.log10(fac_shap))
xlabelu          = xlabelu + r"$(\times 10^{"+str_facexp+"})$"
xlabelv          = xlabelv + r"$(\times 10^{"+str_facexp+"})$"
xlabelw          = xlabelw + r"$(\times 10^{"+str_facexp+"})$"
xlabelm          = xlabelm + r"$(\times 10^{"+str_facexp+"})$"
linewidth        = 3

# -----------------------------------------------------------------------------------------------------------------------
# Load the channel data to import the information regarding the channel size and the friction Reynolds number 
# and velocity
#     - L_x     : Channel size in the streamwise direction
#     - L_z     : Channel size in the spanwise direction
#     - L_y     : Half of the channel width
#     - rey     : Friction Reynolds number
#     - utau    : Friction velocity
#     - dx      : Downsampling in x
#     - dy      : Downsampling in y
#     - dz      : Downsampling in z
#     - padding : Number of nodes of the padding
# -----------------------------------------------------------------------------------------------------------------------
L_x     = chd.L_x
L_z     = chd.L_z
L_y     = chd.L_y
rey     = chd.rey
utau    = chd.utau
dx      = chd.dx
dy      = chd.dy
dz      = chd.dz
padding = chd.padding

# -----------------------------------------------------------------------------------------------------------------------
# Define the data of the model definition: data, padding, downsampling...
#     - uvw_folder      : Folder of the velocity data
#     - uvw_file        : This file does not contain the file index
#     - data_folder     : Folder for storing the data of the model
#     - umean_file      : File for the mean velocity
#     - unorm_file      : File for the normalization of the velocity
#     - umax_file       : File containing the maximum velocity
#     - plot_folder     : Folder to store the plots
# -----------------------------------------------------------------------------------------------------------------------
uvw_folder  = folders.uvw_folder
uvw_file    = folders.uvw_file
shap_folder = folders.shap_folder
shap_file   = folders.shap_file
data_folder = folders.data_folder
umean_file  = folders.umean_file
unorm_file  = folders.unorm_file
umax_file   = folders.umax_file
plot_folder = folders.plot_folder

# -----------------------------------------------------------------------------------------------------------------------
# Define the data for the shap.
#     - ngpu          : Number of gpus
#     - field_ini     : Initial field of the shaps
#     - field_fin     : Final field of the shaps
#     - field_delta   : Separation between the files
#     - read_model    : Flag to define or read the model (False=define, True=read)
#     - model_folder  : Folder of the trained model files
#     - model_name    : Name of the trained model file
#     - nfil          : Number of filters of the first layer of the Unet
#     - stride        : Stride of the Unet
#     - activation    : Activation function
#     - kernel        : Kernel size of the unet
#     - pooling       : Size of the poolings of the unet
#     - delta_pred    : Number of fields to advance the prediction
#     - data_type     : Format of the data of the training
#     - error_file    : file to store the error
#     - umax_file     : file to store the maximum and minimum velocity
#     - urmspred_file : file to store the rms predicted by the model 
#     - nrep_field      : number of repetitions of each field for calculating the SHAP values
#     - shap_batch      : batch size used for the shap
# -----------------------------------------------------------------------------------------------------------------------
index_ini       = st_data.field_ini
index_fin       = st_data.field_fin
index_delta     = st_data.field_delta
ngpu            = tr_data.ngpu
field_ini       = sh_data.field_ini
field_fin       = sh_data.field_fin
field_delta     = sh_data.field_delta
read_model      = tr_data.read_model
model_folder    = folders.model_folder
model_read      = folders.model_read
nfil            = tr_data.nfil
stride          = tr_data.stride
activation      = tr_data.activation
kernel          = tr_data.kernel
pooling         = tr_data.pooling
delta_pred      = tr_data.delta_pred
nsamples        = sh_data.nsamples
nsamples_max    = sh_data.nsamples_max
data_type       = tr_data.data_type
error_file      = folders.error_file
umax_file       = folders.umax_file
urmspred_file   = folders.urmspred_file
mean_norm       = tr_data.mean_norm
tfrecord_folder = folders.tfrecord_folder
nrep_field      = sh_data.nrep_field
shap_batch      = sh_data.shap_batch
repeat_exist    = sh_data.repeat_exist

# -----------------------------------------------------------------------------------------------------------------------
# Define dict containing the information needed for the shap model
# -----------------------------------------------------------------------------------------------------------------------
data_shap = {"shap_folder":shap_folder,"shap_file":shap_file,"uvw_folder":uvw_folder,"uvw_file":uvw_file,
             "padding":padding,"dx":dx,"dy":dy,"dz":dz,"data_folder":data_folder,"umean_file":umean_file,
             "unorm_file":unorm_file,"L_x":L_x,"L_z":L_z,"L_y":L_y,"rey":rey,"utau":utau,"ngpu":ngpu,
             "field_ini":field_ini,"field_fin":field_fin,"field_delta":field_delta,"model_folder":model_folder,
             "model_read":model_read,"nfil":nfil,"stride":stride,"activation":activation,"kernel":kernel,
             "pooling":pooling,"delta_pred":delta_pred,"nsamples":nsamples,"nsamples_max":nsamples,
             "data_type":data_type,"error_file":error_file,"umax_file":umax_file,"urmspred_file":urmspred_file,
             "mean_norm":mean_norm,"tfrecord_folder":tfrecord_folder,"nrep_field":nrep_field,"shap_batch":shap_batch,
             "repeat_exist":repeat_exist,"flag_model":False}
shap_model = shap_config(data_in=data_shap)


# -----------------------------------------------------------------------------------------------------------------------
# Read the channel characteristics
# -----------------------------------------------------------------------------------------------------------------------
Data_flow = {"folder":uvw_folder,"file":uvw_file,"down_x":dx,"down_y":dy,
             "down_z":dz,"L_x":L_x,"L_y":L_y,"L_z":L_z,"rey":rey,"utau":utau,"umax_file":umax_file}
flowfield = flow_field(data_in=Data_flow)
flowfield.shape_tensor()
flowfield.flow_grid()
yplusmesh = flowfield.yplus


    
# -------------------------------------------------------------------------------------------------------------------
# Create the mesh for the pdf
# -------------------------------------------------------------------------------------------------------------------
diffy = np.diff(yplusmesh)/2
binsy = np.concatenate(([-diffy[0]],yplusmesh[:-1]+diffy,[yplusmesh[-1]+diffy[-1]]))

index_range = range(index_ini,index_fin,index_delta)
binsxu      = bins
binsxv      = bins
binsxw      = bins
binsxm      = bins
for ii in index_range: 
    print("Field:"+str(ii),flush=True)
    shap_data  = shap_model.read_shap(data_in = {"index":ii})
    shap_u     = shap_data["SHAP_u"]
    shap_v     = shap_data["SHAP_v"]
    shap_w     = shap_data["SHAP_w"]
    
    
    shap_m      = np.sqrt(shap_u**2+shap_v**2+shap_w**2)
    shap_u_arr  = shap_u.flatten()*fac_shap
    shap_v_arr  = shap_v.flatten()*fac_shap
    shap_w_arr  = shap_w.flatten()*fac_shap
    shap_m_arr  = shap_m.flatten()*fac_shap
    y_h_struc   = flowfield.y_h.reshape(-1,1,1)
    yplus_struc = (1-abs(y_h_struc))*rey*np.ones_like(shap_u)
    yplus_arr   = yplus_struc.flatten()
    
    # -------------------------------------------------------------------------------------------------------------------
    # Histogram of shap_u
    # -------------------------------------------------------------------------------------------------------------------
    hist_uy,hist_u,hist_y = np.histogram2d(shap_u_arr,yplus_arr,bins=(binsxu,binsy))
    hist_y                = hist_y[:-1]+np.diff(hist_y)/2
    hist_u                = hist_u[:-1]+np.diff(hist_u)/2
    grid_u,grid_y         = np.meshgrid(hist_u,hist_y)
    grid_uy               = hist_uy.T.copy()
    # -------------------------------------------------------------------------------------------------------------------
    # Generate arrays
    # -------------------------------------------------------------------------------------------------------------------
    if ii==index_range[0]:
        umin             = np.min(shap_u_arr)
        if umin > 0:
            umin        *= 0.8
        else:
            umin        *= 1.2
        umax             = np.max(shap_u_arr)
        if umax < 0:
            umax        *= 0.8
        else:
            umax        *= 1.2 
        grid_tot_uy      = grid_uy
        binsxu           = np.linspace(umin,umax,bins+1)
    else:
        grid_tot_uy     += grid_uy
        
    
    # -------------------------------------------------------------------------------------------------------------------
    # Histogram of shap_v
    # -------------------------------------------------------------------------------------------------------------------
    hist_vy,hist_v,hist_y = np.histogram2d(shap_v_arr,yplus_arr,bins=(binsxv,binsy))
    hist_y                = hist_y[:-1]+np.diff(hist_y)/2
    hist_v                = hist_v[:-1]+np.diff(hist_v)/2
    grid_v,grid_y         = np.meshgrid(hist_v,hist_y)
    grid_vy               = hist_vy.T.copy()
    # -------------------------------------------------------------------------------------------------------------------
    # Generate arrays
    # -------------------------------------------------------------------------------------------------------------------
    if ii==index_range[0]:
        vmin             = np.min(shap_v_arr)
        if vmin > 0:
            vmin        *= 0.8
        else:
            vmin        *= 1.2
        vmax             = np.max(shap_v_arr)
        if vmax < 0:
            vmax        *= 0.8
        else:
            vmax        *= 1.2 
        grid_tot_vy      = grid_vy
        binsxv           = np.linspace(vmin,vmax,bins+1)
    else:
        grid_tot_vy     += grid_vy
       
    
    # -------------------------------------------------------------------------------------------------------------------
    # Histogram of shap_w
    # -------------------------------------------------------------------------------------------------------------------
    hist_wy,hist_w,hist_y = np.histogram2d(shap_w_arr,yplus_arr,bins=(binsxw,binsy))
    hist_y                = hist_y[:-1]+np.diff(hist_y)/2
    hist_w                = hist_w[:-1]+np.diff(hist_w)/2
    grid_w,grid_y         = np.meshgrid(hist_w,hist_y)
    grid_wy               = hist_wy.T.copy()
    # -------------------------------------------------------------------------------------------------------------------
    # Generate arrays
    # -------------------------------------------------------------------------------------------------------------------
    if ii==index_range[0]:
        wmin             = np.min(shap_w_arr)
        if wmin > 0:
            wmin        *= 0.8
        else:
            wmin        *= 1.2
        wmax             = np.max(shap_w_arr)
        if wmax < 0:
            wmax        *= 0.8
        else:
            wmax        *= 1.2 
        grid_tot_wy      = grid_wy
        binsxw           = np.linspace(wmin,wmax,bins+1)
    else:
        grid_tot_wy     += grid_wy
        
    # -------------------------------------------------------------------------------------------------------------------
    # Histogram of shap_m
    # -------------------------------------------------------------------------------------------------------------------
    hist_my,hist_m,hist_y = np.histogram2d(shap_m_arr,yplus_arr,bins=(binsxm,binsy))
    hist_y                = hist_y[:-1]+np.diff(hist_y)/2
    hist_m                = hist_m[:-1]+np.diff(hist_m)/2
    grid_m,grid_y         = np.meshgrid(hist_m,hist_y)
    grid_my               = hist_my.T.copy()
    # -------------------------------------------------------------------------------------------------------------------
    # Generate arrays
    # -------------------------------------------------------------------------------------------------------------------
    if ii==index_range[0]:
        mmin             = np.min(shap_m_arr)
        if vmin > 0:
            mmin        *= 0.8
        else:
            mmin        *= 1.2
        mmax             = np.max(shap_m_arr)
        if mmax < 0:
            mmax        *= 0.8
        else:
            mmax        *= 1.2 
        grid_tot_my      = grid_my
        binsxm           = np.linspace(mmin,mmax,bins+1)
    else:
        grid_tot_my     += grid_my
        
grid_tot_uy /= np.max(grid_tot_uy)
grid_tot_vy /= np.max(grid_tot_vy)
grid_tot_wy /= np.max(grid_tot_wy)
grid_tot_my /= np.max(grid_tot_my)


ucontent     = grid_u[np.where(grid_tot_uy>=lev_min)]
umin         = np.min(ucontent)
umax         = np.max(ucontent)
vcontent     = grid_v[np.where(grid_tot_vy>=lev_min)]
vmin         = np.min(vcontent)
vmax         = np.max(vcontent)
wcontent     = grid_w[np.where(grid_tot_wy>=lev_min)]
wmin         = np.min(wcontent)
wmax         = np.max(wcontent)
mcontent     = grid_m[np.where(grid_tot_my>=lev_min)]
mmin         = np.min(mcontent)
mmax         = np.max(mcontent)
print([umin,umax])
print([vmin,vmax])
print([wmin,wmax])
print([mmin,mmax])
# -----------------------------------------------------------------------------------------------------------------------
# Plot the data
# -----------------------------------------------------------------------------------------------------------------------
plot_format_data = {"plot_folder":plot_folder,"plot_file":plot_fileu,"ylabel":ylabel,"xlabel":xlabelu,
                    "fontsize":fontsize,"figsize_x":figsize_x,"figsize_y":figsize_y,
                    "colormap":colormap,"colornum":colornum,"dpi":dpi,"hist_data":grid_tot_uy,"hist_x":grid_u,
                    "hist_y":grid_y,"yplus_struc":yplus_arr,"yplusmesh":flowfield.yplus,
                    "lev_min":lev_min,"lev_delta":lev_delta,"linewidth":linewidth,"datamin":umin,"datamax":umax}
plot_hist_y_withhist(data_in=plot_format_data)

plot_format_data = {"plot_folder":plot_folder,"plot_file":plot_filev,"ylabel":ylabel,"xlabel":xlabelv,
                    "fontsize":fontsize,"figsize_x":figsize_x,"figsize_y":figsize_y,
                    "colormap":colormap,"colornum":colornum,"dpi":dpi,"hist_data":grid_tot_vy,"hist_x":grid_v,
                    "hist_y":grid_y,"yplus_struc":yplus_arr,"yplusmesh":flowfield.yplus,
                    "lev_min":lev_min,"lev_delta":lev_delta,"linewidth":linewidth,"datamin":vmin,"datamax":vmax}
plot_hist_y_withhist(data_in=plot_format_data)

plot_format_data = {"plot_folder":plot_folder,"plot_file":plot_filew,"ylabel":ylabel,"xlabel":xlabelw,
                    "fontsize":fontsize,"figsize_x":figsize_x,"figsize_y":figsize_y,
                    "colormap":colormap,"colornum":colornum,"dpi":dpi,"hist_data":grid_tot_wy,"hist_x":grid_w,
                    "hist_y":grid_y,"yplus_struc":yplus_arr,"yplusmesh":flowfield.yplus,
                    "lev_min":lev_min,"lev_delta":lev_delta,"linewidth":linewidth,"datamin":wmin,"datamax":wmax}
plot_hist_y_withhist(data_in=plot_format_data)

plot_format_data = {"plot_folder":plot_folder,"plot_file":plot_filem,"ylabel":ylabel,"xlabel":xlabelm,
                    "fontsize":fontsize,"figsize_x":figsize_x,"figsize_y":figsize_y,
                    "colormap":colormap,"colornum":colornum,"dpi":dpi,"hist_data":grid_tot_my,"hist_x":grid_m,
                    "hist_y":grid_y,"yplus_struc":yplus_arr,"yplusmesh":flowfield.yplus,
                    "lev_min":lev_min,"lev_delta":lev_delta,"linewidth":linewidth,"datamin":mmin,"datamax":mmax}
plot_hist_y_withhist(data_in=plot_format_data)
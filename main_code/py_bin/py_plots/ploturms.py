# -*- coding: utf-8 -*-
"""
-------------------------------------------------------------------------------------------------------------------------
ploturms.py
-------------------------------------------------------------------------------------------------------------------------
Created on Thu Mar 28 12:37:35 2024

@author: Andres Cremades Botella

File to plot training information
"""

# -----------------------------------------------------------------------------------------------------------------------
# Import packages for all functions
# -----------------------------------------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np
import os

# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------
# Define functions
# -----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------

def ploturms(data_in={"file":"Urms.txt","folder":"Data","plot_folder":"plots","xlabel":"$y^+$",
                      "ylabel":"$u'^+$","ylabel2":"$|u_iu_j|^+$","fontsize":18,"figsize_x":10,"figsize_y":8,
                      "colormap":"viridis","colornum":2,"fig_name":"urms","fig_name2":"uvabs","dpi":60,
                      "dy":1,"dx":1,"dz":1,"uvw_folder":"../../P125_21pi_vu/",
                      "uvw_file":"P125_21pi_vu.$INDEX$.h5.uvw","L_x":2*np.pi,"L_y":1,"L_z":np.pi,
                      "file_trj":"Re180.prof.txt","rey":125,"utau":0.060523258443963}):
    """
    .....................................................................................................................
    # ploturms: Function to generate the plot of the rms velocity
    .....................................................................................................................
    Parameters
    ----------
    data_in : dict, optional
        Data required for generating the plot. 
        The default is {"file":"hist.txt","folder":"Data","plot_folder":"plots","xlabel":"$y^+$",
                        "ylabel":"$\overline{U}$","fontsize":18,"figsize_x":10,
                        "figsize_y":8,"xscale":"linear","yscale":"log","colormap":"viridis","colornum":2,
                        "fig_name":"training_info","dpi":60,"dy":1,"L_x":2*np.pi,"L_y":1,"L_z":np.pi,
                        "file_trj":"Re180.prof.txt"}.
        Data:
            - file        : file of the training information
            - folder      : folder of the data generated during the training
            - plot_folder : folder to store the figures
            - fontsize    : font size used for the figure
            - xlabel      : label of the x axis
            - ylabel      : label of the y axis
            - ylabel2     : label of the y axis of the second figure
            - figsize_x   : size of the figure in x
            - figsize_y   : size of the figure in y
            - colormap    : colormap used for the figure
            - colornum    : number of colors of the colormap, two curves are used. The number of levels of the 
                            colormap needs to be higher than 2 
            - fig_name    : name of the saved figure
            - fig_name2   : name of the saved figure for the second plot
            - dpi         : dots per inch of the saved figure
            - dy          : downsampling in the wall-normal direction
            - dx          : downsampling in the streamwise direction
            - dz          : downsampling in the spanwise direction
            - uvw_folder  : folder of the flow fields
            - uvw_file    : file of the flow fields
            - L_x         : streamwise dimension of the channel
            - L_y         : wall-normal dimension of the channel
            - L_z         : spanwise dimension of the channel
            - file_trj    : file containing the statistics of Torroja
            - rey         : friction Reynolds number
            - utau        : friction velocity

    Returns
    -------
    None.

    """
    
    
    # -------------------------------------------------------------------------------------------------------------------
    # Import packages
    # -------------------------------------------------------------------------------------------------------------------
    from py_bin.py_class.plot_format import plot_format
    from py_bin.py_functions.urms import read_rms
    from py_bin.py_class.flow_field import flow_field
    
    # -------------------------------------------------------------------------------------------------------------------
    # Read the parameters of the plot
    # -------------------------------------------------------------------------------------------------------------------
    folder      = str(data_in["folder"])      # Folder to read the epoch data
    file        = str(data_in["file"])        # File to read for the epochs data
    plot_folder = str(data_in["plot_folder"]) # folder to save the plots
    xlabel      = str(data_in["xlabel"])      # label of the x axis
    ylabel      = str(data_in["ylabel"])      # label of the y axis
    ylabel2     = str(data_in["ylabel2"])     # label of the y axis of the second plot
    fontsize    = int(data_in["fontsize"])    # size of the text in the plot
    figsize_x   = int(data_in["figsize_x"])   # size of the figure in direction x
    figsize_y   = int(data_in["figsize_y"])   # size of the figure in direction y
    colormap    = str(data_in["colormap"])    # colormap of the figure
    colornum    = int(data_in["colornum"])    # number of colors of the colormap
    fig_name    = str(data_in["fig_name"])    # name of the figure to be saved
    fig_name2   = str(data_in["fig_name2"])   # name of the figure to be saved for the second plot
    dpi         = float(data_in["dpi"])       # dots per inch to save the figure
    dy          = int(data_in["dy"])          # downsampling in the wall-normal direction
    dx          = int(data_in["dx"])          # downsampling in the streamwise direction
    dz          = int(data_in["dz"])          # downsampling in the spanwise direction
    uvw_folder  = str(data_in["uvw_folder"])  # folder of the flow fields
    uvw_file    = str(data_in["uvw_file"])    # file of the flow fields
    L_x         = float(data_in["L_x"])       # streamwise dimension of the channel
    L_y         = float(data_in["L_y"])       # wall-normal dimension of the channel
    L_z         = float(data_in["L_z"])       # spanwise dimension of the channel
    file_trj    = str(data_in["file_trj"])    # file of the torroja statistics
    rey         = float(data_in["rey"])       # Friction reynolds number
    utau        = float(data_in["utau"])      # Friction velocity
    
    # -------------------------------------------------------------------------------------------------------------------
    # Read the file mean velocity
    # -------------------------------------------------------------------------------------------------------------------
    Data_flow  = {"folder":uvw_folder,"file":uvw_file,"down_x":dx,"down_y":dy,"down_z":dz,\
                  "L_x":L_x,"L_y":L_y,"L_z":L_z,"rey":rey,"utau":utau}
    flow_data  = flow_field(data_in=Data_flow)
    flow_data.shape_tensor()
    flow_data.flow_grid()
    data_urms  = read_rms(data_in={"folder":folder,"file":file,"dy":dy})
    uurms      = (data_urms["uurms"][:flow_data.yl_s]+np.flip(data_urms["uurms"][flow_data.yu_s:]))/2
    uurms     /= flow_data.utau
    vvrms      = (data_urms["vvrms"][:flow_data.yl_s]+np.flip(data_urms["vvrms"][flow_data.yu_s:]))/2
    vvrms     /= flow_data.utau
    wwrms      = (data_urms["wwrms"][:flow_data.yl_s]+np.flip(data_urms["wwrms"][flow_data.yu_s:]))/2
    wwrms     /= flow_data.utau
    uv         = (abs(data_urms["uv"][:flow_data.yl_s])+abs(np.flip(data_urms["uv"][flow_data.yu_s:])))/2
    uv        /= flow_data.utau**2
    uw         = (abs(data_urms["uw"][:flow_data.yl_s])+abs(np.flip(data_urms["uw"][flow_data.yu_s:])))/2
    uw        /= flow_data.utau**2
    vw         = (abs(data_urms["vw"][:flow_data.yl_s])+abs(np.flip(data_urms["vw"][flow_data.yu_s:])))/2
    vw        /= flow_data.utau**2
    
    # -------------------------------------------------------------------------------------------------------------------
    # Read the data of torroja
    # -------------------------------------------------------------------------------------------------------------------
    data_trj = folder+'/'+file_trj
    posy     = []
    u_trj    = []
    v_trj    = []
    w_trj    = []
    uv_trj   = []
    vw_trj   = []
    uw_trj   = []
    with open(data_trj) as f:
        line = f.readline()
        while line:
            if line[0] != '%':
                linesep = line.split()
                posy.append(float(linesep[1]))
                u_trj.append(float(linesep[3]))
                v_trj.append(float(linesep[4]))
                w_trj.append(float(linesep[5]))
                uv_trj.append(abs(float(linesep[10])))
                vw_trj.append(abs(float(linesep[12])))
                uw_trj.append(abs(float(linesep[11])))
            line = f.readline()
    posy_arr = np.array(posy)
    u_trj_arr = np.array(u_trj)
    v_trj_arr = np.array(v_trj)
    w_trj_arr = np.array(w_trj)
    uv_trj_arr = np.array(uv_trj)
    vw_trj_arr = np.array(vw_trj)
    uw_trj_arr = np.array(uw_trj)
    
    # -------------------------------------------------------------------------------------------------------------------
    # Create the plot
    # -------------------------------------------------------------------------------------------------------------------
    data_plot  = {"xlabel":xlabel,"ylabel":ylabel,"zlabel":[],"fontsize":fontsize,"figsize_x":figsize_x,
                  "figsize_y":figsize_y,"xscale":"linear","yscale":"linear","zscale":"linear","colormap":colormap,
                  "colornum":colornum,"legend":True,"fig_name":fig_name,"dpi":dpi,"plot_folder":plot_folder,
                  "xmin":None,"xmax":None,"ymin":None,"ymax":None,"zmin":None,"zmax":None}
    plot_train = plot_format(data_in=data_plot)
    plot_train.create_figure()
    plot_info1 = {"data_x":flow_data.yplus,"data_y":uurms,"label":"$u'^+$",\
                  "color":None,"linewidth":2,"plot_number":0,"style":"-"}
    plot_train.add_plot_2d(data_in=plot_info1)
    plot_info2 = {"data_x":flow_data.yplus,"data_y":vvrms,"label":"$v'^+$",\
                  "color":None,"linewidth":2,"plot_number":1,"style":"-"}
    plot_train.add_plot_2d(data_in=plot_info2)
    plot_info3 = {"data_x":flow_data.yplus,"data_y":wwrms,"label":"$w'^+$",\
                  "color":None,"linewidth":2,"plot_number":2,"style":"-"}
    plot_train.add_plot_2d(data_in=plot_info3)
    plot_info4 = {"data_x":posy_arr,"data_y":u_trj_arr,"label":"$u'^+_{torroja}$",\
                  "color":None,"linewidth":2,"plot_number":0,"style":"--"}
    plot_train.add_plot_2d(data_in=plot_info4)
    plot_info5 = {"data_x":posy_arr,"data_y":v_trj_arr,"label":"$v'^+_{torroja}$",\
                  "color":None,"linewidth":2,"plot_number":1,"style":"--"}
    plot_train.add_plot_2d(data_in=plot_info5)
    plot_info6 = {"data_x":posy_arr,"data_y":w_trj_arr,"label":"$w'^+_{torroja}$",\
                  "color":None,"linewidth":2,"plot_number":2,"style":"--"}
    plot_train.add_plot_2d(data_in=plot_info6)
    plot_train.plot_layout()
    plot_train.plot_save_png()
    plot_train.plot_save_pdf()
    
    # -------------------------------------------------------------------------------------------------------------------
    # Create the plot
    # -------------------------------------------------------------------------------------------------------------------
    data_plot  = {"xlabel":xlabel,"ylabel":ylabel2,"zlabel":[],"fontsize":fontsize,"figsize_x":figsize_x,
                  "figsize_y":figsize_y,"xscale":"linear","yscale":"linear","zscale":"linear","colormap":colormap,
                  "colornum":colornum,"legend":True,"fig_name":fig_name2,"dpi":dpi,"plot_folder":plot_folder,
                  "xmin":None,"xmax":None,"ymin":None,"ymax":None,"zmin":None,"zmax":None}
    plot_train = plot_format(data_in=data_plot)
    plot_train.create_figure()
    plot_info1 = {"data_x":flow_data.yplus,"data_y":uv,"label":"$|uv|^+$",\
                  "color":None,"linewidth":2,"plot_number":0,"style":"-"}
    plot_train.add_plot_2d(data_in=plot_info1)
    plot_info2 = {"data_x":flow_data.yplus,"data_y":uw,"label":"$|uw|^+$",\
                  "color":None,"linewidth":2,"plot_number":1,"style":"-"}
    plot_train.add_plot_2d(data_in=plot_info2)
    plot_info3 = {"data_x":flow_data.yplus,"data_y":vw,"label":"$|vw|^+$",\
                  "color":None,"linewidth":2,"plot_number":2,"style":"-"}
    plot_train.add_plot_2d(data_in=plot_info3)
    plot_info4 = {"data_x":posy_arr,"data_y":uv_trj_arr,"label":"$|uv|^+_{torroja}$",\
                  "color":None,"linewidth":2,"plot_number":0,"style":"--"}
    plot_train.add_plot_2d(data_in=plot_info4)
    plot_info5 = {"data_x":posy_arr,"data_y":uw_trj_arr,"label":"$|uw|^+_{torroja}$",\
                  "color":None,"linewidth":2,"plot_number":1,"style":"--"}
    plot_train.add_plot_2d(data_in=plot_info5)
    plot_info6 = {"data_x":posy_arr,"data_y":vw_trj_arr,"label":"$|vw|^+_{torroja}$",\
                  "color":None,"linewidth":2,"plot_number":2,"style":"--"}
    plot_train.add_plot_2d(data_in=plot_info6)
    plot_train.plot_layout()
    try:
        os.mkdir(plot_folder)
    except:
        print("Existing folder...",flush=True)
    plot_train.plot_save_png()
    plot_train.plot_save_pdf()
    
    
    
def ploturmssim_urmspred(data_in={"file_sim":"Urms.txt","file_pred":"Urms_pred.txt","folder":"Data",
                                  "plot_folder":"plots","xlabel":"$y^+$","ylabel":"$u'^+$","ylabel2":"$|u_iu_j|^+$",
                                  "fontsize":18,"figsize_x":10,"figsize_y":8,"colormap":"viridis","colornum":2,
                                  "fig_name":"urms","fig_name2":"uvabs","dpi":60,"dy":1,"dx":1,"dz":1,
                                  "uvw_folder":"../../P125_21pi_vu/","uvw_file":"P125_21pi_vu.$INDEX$.h5.uvw",
                                  "L_x":2*np.pi,"L_y":1,"L_z":np.pi,"file_trj":"Re180.prof.txt","rey":125,
                                  "utau":0.060523258443963}):
    """
    .....................................................................................................................
    # ploturmssim_urmspred: Function to generate the plot of the rms velocity simulated and predicted
    .....................................................................................................................
    Parameters
    ----------
    data_in : dict, optional
        Data required for generating the plot. 
        The default is {"file":"hist.txt","folder":"Data","plot_folder":"plots","xlabel":"$y^+$",
                        "ylabel":"$\overline{U}$","fontsize":18,"figsize_x":10,
                        "figsize_y":8,"xscale":"linear","yscale":"log","colormap":"viridis","colornum":2,
                        "fig_name":"training_info","dpi":60,"dy":1,"L_x":2*np.pi,"L_y":1,"L_z":np.pi,
                        "file_trj":"Re180.prof.txt"}.
        Data:
            - file_sim    : file of the simulated rms information
            - file_pred   : file of the predicted rms information
            - folder      : folder of the data generated during the training
            - plot_folder : folder to store the figures
            - fontsize    : font size used for the figure
            - xlabel      : label of the x axis
            - ylabel      : label of the y axis
            - ylabel2     : label of the y axis of the second figure
            - figsize_x   : size of the figure in x
            - figsize_y   : size of the figure in y
            - colormap    : colormap used for the figure
            - colornum    : number of colors of the colormap, two curves are used. The number of levels of the 
                            colormap needs to be higher than 2 
            - fig_name    : name of the saved figure
            - fig_name2   : name of the saved figure for the second plot
            - dpi         : dots per inch of the saved figure
            - dy          : downsampling in the wall-normal direction
            - dx          : downsampling in the streamwise direction
            - dz          : downsampling in the spanwise direction
            - uvw_folder  : folder of the flow fields
            - uvw_file    : file of the flow fields
            - L_x         : streamwise dimension of the channel
            - L_y         : wall-normal dimension of the channel
            - L_z         : spanwise dimension of the channel
            - file_trj    : file containing the statistics of Torroja
            - rey         : friction Reynolds number
            - utau        : friction velocity

    Returns
    -------
    None.

    """
    
    
    # -------------------------------------------------------------------------------------------------------------------
    # Import packages
    # -------------------------------------------------------------------------------------------------------------------
    from py_bin.py_class.plot_format import plot_format
    from py_bin.py_functions.urms import read_rms
    from py_bin.py_class.flow_field import flow_field
    
    # -------------------------------------------------------------------------------------------------------------------
    # Read the parameters of the plot
    # -------------------------------------------------------------------------------------------------------------------
    folder      = str(data_in["folder"])      # Folder to read the epoch data
    file_sim    = str(data_in["file_sim"])    # File to read for the epochs data
    file_pred   = str(data_in["file_pred"])   # File to read for the epochs data
    plot_folder = str(data_in["plot_folder"]) # folder to save the plots
    xlabel      = str(data_in["xlabel"])      # label of the x axis
    ylabel      = str(data_in["ylabel"])      # label of the y axis
    ylabel2     = str(data_in["ylabel2"])     # label of the y axis of the second plot
    fontsize    = int(data_in["fontsize"])    # size of the text in the plot
    figsize_x   = int(data_in["figsize_x"])   # size of the figure in direction x
    figsize_y   = int(data_in["figsize_y"])   # size of the figure in direction y
    colormap    = str(data_in["colormap"])    # colormap of the figure
    colornum    = int(data_in["colornum"])    # number of colors of the colormap
    fig_name    = str(data_in["fig_name"])    # name of the figure to be saved
    fig_name2   = str(data_in["fig_name2"])   # name of the figure to be saved for the second plot
    dpi         = float(data_in["dpi"])       # dots per inch to save the figure
    dy          = int(data_in["dy"])          # downsampling in the wall-normal direction
    dx          = int(data_in["dx"])          # downsampling in the streamwise direction
    dz          = int(data_in["dz"])          # downsampling in the spanwise direction
    uvw_folder  = str(data_in["uvw_folder"])  # folder of the flow fields
    uvw_file    = str(data_in["uvw_file"])    # file of the flow fields
    L_x         = float(data_in["L_x"])       # streamwise dimension of the channel
    L_y         = float(data_in["L_y"])       # wall-normal dimension of the channel
    L_z         = float(data_in["L_z"])       # spanwise dimension of the channel
    file_trj    = str(data_in["file_trj"])    # file of the torroja statistics
    rey         = float(data_in["rey"])       # Friction reynolds number
    utau        = float(data_in["utau"])      # Friction velocity
    
    # -------------------------------------------------------------------------------------------------------------------
    # Read the file mean velocity
    # -------------------------------------------------------------------------------------------------------------------
    Data_flow  = {"folder":uvw_folder,"file":uvw_file,"down_x":dx,"down_y":dy,"down_z":dz,\
                  "L_x":L_x,"L_y":L_y,"L_z":L_z,"rey":rey,"utau":utau}
    flow_data  = flow_field(data_in=Data_flow)
    flow_data.shape_tensor()
    flow_data.flow_grid()
    data_urms_sim  = read_rms(data_in={"folder":folder,"file":file_sim,"dy":dy})
    uurms_sim      = (data_urms_sim["uurms"][:flow_data.yl_s]+np.flip(data_urms_sim["uurms"][flow_data.yu_s:]))/2
    uurms_sim     /= flow_data.utau
    vvrms_sim      = (data_urms_sim["vvrms"][:flow_data.yl_s]+np.flip(data_urms_sim["vvrms"][flow_data.yu_s:]))/2
    vvrms_sim     /= flow_data.utau
    wwrms_sim      = (data_urms_sim["wwrms"][:flow_data.yl_s]+np.flip(data_urms_sim["wwrms"][flow_data.yu_s:]))/2
    wwrms_sim     /= flow_data.utau
    uv_sim         = (abs(data_urms_sim["uv"][:flow_data.yl_s])+abs(np.flip(data_urms_sim["uv"][flow_data.yu_s:])))/2
    uv_sim        /= flow_data.utau**2
    uw_sim         = (abs(data_urms_sim["uw"][:flow_data.yl_s])+abs(np.flip(data_urms_sim["uw"][flow_data.yu_s:])))/2
    uw_sim        /= flow_data.utau**2
    vw_sim         = (abs(data_urms_sim["vw"][:flow_data.yl_s])+abs(np.flip(data_urms_sim["vw"][flow_data.yu_s:])))/2
    vw_sim        /= flow_data.utau**2
    data_urms_pred = read_rms(data_in={"folder":folder,"file":file_pred,"dy":dy})
    uurms_pred     = (data_urms_pred["uurms"][:flow_data.yl_s]+np.flip(data_urms_pred["uurms"][flow_data.yu_s:]))/2
    uurms_pred    /= flow_data.utau
    vvrms_pred     = (data_urms_pred["vvrms"][:flow_data.yl_s]+np.flip(data_urms_pred["vvrms"][flow_data.yu_s:]))/2
    vvrms_pred    /= flow_data.utau
    wwrms_pred     = (data_urms_pred["wwrms"][:flow_data.yl_s]+np.flip(data_urms_pred["wwrms"][flow_data.yu_s:]))/2
    wwrms_pred    /= flow_data.utau
    uv_pred        = (abs(data_urms_pred["uv"][:flow_data.yl_s])+abs(np.flip(data_urms_pred["uv"][flow_data.yu_s:])))/2
    uv_pred       /= flow_data.utau**2
    uw_pred        = (abs(data_urms_pred["uw"][:flow_data.yl_s])+abs(np.flip(data_urms_pred["uw"][flow_data.yu_s:])))/2
    uw_pred       /= flow_data.utau**2
    vw_pred        = (abs(data_urms_pred["vw"][:flow_data.yl_s])+abs(np.flip(data_urms_pred["vw"][flow_data.yu_s:])))/2
    vw_pred       /= flow_data.utau**2
    
    
    # -------------------------------------------------------------------------------------------------------------------
    # Create the plot
    # -------------------------------------------------------------------------------------------------------------------
    data_plot  = {"xlabel":xlabel,"ylabel":ylabel,"zlabel":[],"fontsize":fontsize,"figsize_x":figsize_x,
                  "figsize_y":figsize_y,"xscale":"linear","yscale":"linear","zscale":"linear","colormap":colormap,
                  "colornum":colornum,"legend":True,"fig_name":fig_name,"dpi":dpi,"plot_folder":plot_folder,
                  "xmin":None,"xmax":None,"ymin":None,"ymax":None,"zmin":None,"zmax":None}
    plot_train = plot_format(data_in=data_plot)
    plot_train.create_figure()
    plot_info1 = {"data_x":flow_data.yplus,"data_y":uurms_sim,"label":"$u'_s^+$",\
                  "color":None,"linewidth":2,"plot_number":0,"style":"-"}
    plot_train.add_plot_2d(data_in=plot_info1)
    plot_info2 = {"data_x":flow_data.yplus,"data_y":vvrms_sim,"label":"$v'_s^+$",\
                  "color":None,"linewidth":2,"plot_number":1,"style":"-"}
    plot_train.add_plot_2d(data_in=plot_info2)
    plot_info3 = {"data_x":flow_data.yplus,"data_y":wwrms_sim,"label":"$w'_s^+$",\
                  "color":None,"linewidth":2,"plot_number":2,"style":"-"}
    plot_train.add_plot_2d(data_in=plot_info3)
    plot_info4 = {"data_x":flow_data.yplus,"data_y":uurms_pred,"label":"$u'_p^+$",\
                  "color":None,"linewidth":2,"plot_number":0,"style":"-."}
    plot_train.add_plot_2d(data_in=plot_info4)
    plot_info5 = {"data_x":flow_data.yplus,"data_y":vvrms_pred,"label":"$v'_p^+$",\
                  "color":None,"linewidth":2,"plot_number":1,"style":"-."}
    plot_train.add_plot_2d(data_in=plot_info5)
    plot_info6 = {"data_x":flow_data.yplus,"data_y":wwrms_pred,"label":"$w'_p^+$",\
                  "color":None,"linewidth":2,"plot_number":2,"style":"-."}
    plot_train.add_plot_2d(data_in=plot_info6)
    plot_train.plot_layout()
    plot_train.plot_save_png()
    plot_train.plot_save_pdf()
    
    # -------------------------------------------------------------------------------------------------------------------
    # Create the plot
    # -------------------------------------------------------------------------------------------------------------------
    data_plot  = {"xlabel":xlabel,"ylabel":ylabel2,"zlabel":[],"fontsize":fontsize,"figsize_x":figsize_x,
                  "figsize_y":figsize_y,"xscale":"linear","yscale":"linear","zscale":"linear","colormap":colormap,
                  "colornum":colornum,"legend":True,"fig_name":fig_name2,"dpi":dpi,"plot_folder":plot_folder,
                  "xmin":None,"xmax":None,"ymin":None,"ymax":None,"zmin":None,"zmax":None}
    plot_train = plot_format(data_in=data_plot)
    plot_train.create_figure()
    plot_info1 = {"data_x":flow_data.yplus,"data_y":uv_sim,"label":"$|uv|_s^+$",\
                  "color":None,"linewidth":2,"plot_number":0,"style":"-"}
    plot_train.add_plot_2d(data_in=plot_info1)
    plot_info2 = {"data_x":flow_data.yplus,"data_y":uw_sim,"label":"$|uw|_s^+$",\
                  "color":None,"linewidth":2,"plot_number":1,"style":"-"}
    plot_train.add_plot_2d(data_in=plot_info2)
    plot_info3 = {"data_x":flow_data.yplus,"data_y":vw_sim,"label":"$|vw|_s^+$",\
                  "color":None,"linewidth":2,"plot_number":2,"style":"-"}
    plot_train.add_plot_2d(data_in=plot_info3)
    plot_info4 = {"data_x":flow_data.yplus,"data_y":uv_pred,"label":"$|uv|_p^+$",\
                  "color":None,"linewidth":2,"plot_number":0,"style":"-."}
    plot_train.add_plot_2d(data_in=plot_info4)
    plot_info5 = {"data_x":flow_data.yplus,"data_y":uw_pred,"label":"$|uw|_p^+$",\
                  "color":None,"linewidth":2,"plot_number":1,"style":"-."}
    plot_train.add_plot_2d(data_in=plot_info5)
    plot_info6 = {"data_x":flow_data.yplus,"data_y":vw_pred,"label":"$|vw|_p^+$",\
                  "color":None,"linewidth":2,"plot_number":2,"style":"-."}
    plot_train.add_plot_2d(data_in=plot_info6)
    plot_train.plot_layout()
    try:
        os.mkdir(plot_folder)
    except:
        print("Existing folder...",flush=True)
    plot_train.plot_save_png()
    plot_train.plot_save_pdf()
# -*- coding: utf-8 -*-
"""
Welcome to the XAI_TurbulentChannel_optimized repository by Andres Cremades. 

This repository contains the files, functions and data required for training a Deep Learning model for predicting the 
evolution of a turbulent channel and then calculate the SHAP values or importance of each grid node.

The code module follows the structure below:
    main code
    |
    |
    |---#  1) check_data.py
    |         Function to check if the tensorflow data is corrupt
    |---#  2) create_uvstruc_dataset.py
    |         Function to create the dataset of tangential Reynolds stress structures.
    |---#  3) main_CNN.py
    |         Function for training the Deep Learning function.
    |---#  4) main_SHAP.py
    |         Function to calculate the SHAP values using Expected Gradients
    |---#  5) main_statistics.py
    |         Function to calculate the statistics of the flow
    |---#  6) main_uvstruc.py
    |         Function to calculate the Reynolds stress structures of a field of the flow
    |---#  7) plot_training_epoch.py
    |         Function to plot the results of the training process
    |---#  8) plot_umean.py
    |         Function to plot the results of the mean velocity
    |---#  9) plot_urms.py
    |         Function to plot the root mean square of the velocity
    |---# 10) prepare_data.py
    |         Function to prepare the data for the training with the tensorflow format
    |---# 11) [py_bin]
    |   |     Folder to store the python code
    |   |---# 11.1) [py_class]
    |   |   |       Folder to store the code relative to the classes      
    |   |   |---# 11.1.1) ann_config.py
    |   |   |             Function to generate the artificial neural network class. Defines strategy, models...
    |   |   |---# 11.1.2) flow_field.py
    |   |   |             Function to generate the flow field of the channel and the grid characteristics
    |   |   |---# 11.1.3) plot_format.py
    |   |   |             Function to generate a class for the plots
    |   |   |---# 11.1.4) shap_config.py
    |   |   |             Function to generate a class for the shap values model
    |   |   |---# 11.1.5) structures.py
    |   |   |             Function to define the structure properties
    |   |   |---# 11.1.6) uv_structure.py
    |   |                 Function to define the uv structures
    |   |---# 11.2) [py_functions]
    |   |   |       Folder to store the functions required by the calculations
    |   |   |---# 11.2.1) CNNblock_definition.py
    |   |   |             File containing the functions to define the neural network blocks
    |   |   |---# 11.2.2) multiworker_checkpoint.py
    |   |   |             File containing the functions to decide if the node in the multiworker are chief or worker
    |   |   |---# 11.2.3) norm_velocity.py
    |   |   |             File containing the functions for normalize and dimensionalize the velocities
    |   |   |---# 11.2.4) normalization.py
    |   |   |             File containing the functions for calculate the normalization
    |   |   |---# 11.2.5) read_norm_velocity.py
    |   |   |             File containing the function to read the velocity field and normalize it
    |   |   |---# 11.2.6) read_velocity.py
    |   |   |             File containing the function to read the velocity field
    |   |   |---# 11.2.7) trainvali_data.py
    |   |   |             File containing the functions to read and normalize the data for the training. Also prepares
    |   |   |             and read data with the tensorflow format.
    |   |   |---# 11.2.8) umean.py
    |   |   |             Function to calculate the mean velocity
    |   |   |---# 11.2.9) urms.py
    |   |                 Function to calculate the rms velocity
    |   |---# 11.3) [py_packages]
    |   |   |       Folder to store modified packages
    |   |   |---# 11.3.1) [shap]
    |   |                 Folder containing the shap module of python with modifications to save memory in the
    |   |                 calculation of the GradientExplainer.
    |   |---# 11.4) [py_plots]
    |   |   |       Folder containing the files for creating the plots
    |   |   |---# 11.4.1) plottrain.py
    |   |   |             File for plotting the training epochs
    |   |   |---# 11.4.2) plotumean.py
    |   |   |             File for plotting the mean velocity
    |   |   |---# 11.4.3) ploturms.py
    |   |                 File for plotting the rms velocity
    |   |---# 11.5) [py_remote]
    |   |   |       Folder containing the files required for reading the database in a ssh server
    |   |   |---# 11.5.1) read_remote.py
    |   |                 File containing functions for reading files via ssh
"""
# ------------------------------------------------------------------------------------------------------------------------
# Import packages
# ------------------------------------------------------------------------------------------------------------------------
import ast

# ------------------------------------------------------------------------------------------------------------------------
# Name of the documentation
# ------------------------------------------------------------------------------------------------------------------------
file_documentation = 'documentation/documentation.txt'

# ------------------------------------------------------------------------------------------------------------------------
# Define a function for reading the docstring of the files
# ------------------------------------------------------------------------------------------------------------------------
def get_docstring(script_path):
    with open(script_path, 'r') as file:
        tree = ast.parse(file.read())
        return ast.get_docstring(tree, clean=False)

# ------------------------------------------------------------------------------------------------------------------------
# Text to print in the documentation
# ------------------------------------------------------------------------------------------------------------------------
text_main = """
--------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------
[main_code]
    These functions are used to call the routines to the calculation of the models, structures or postprocess the
    information.
..........................................................................................................................
"""
text_bin = """
# 11):
--------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------
[py_bin]
    This folder is used for storing python code
..........................................................................................................................
"""
text_class = """
# 11.1):
--------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------
[py_class]
    This folder is used for storing python code related to generate classes in the code
..........................................................................................................................
"""
text_functions = """
# 11.2):
--------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------
[py_functions]
    This folder is used for storing python code related to the functions used in the calculations
..........................................................................................................................
"""
text_packages = """
# 11.3):
--------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------
[py_packages]
    This folder is used for storing python modules that have been modified
..........................................................................................................................

#  11.3.1)
--------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------
[shap]
    This folder contains a modification on the GradientExplainer to reduce the memory requirements
..........................................................................................................................
"""
text_plots = """
# 11.4):
--------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------
[py_plots]
    This folder is used for storing python code related to the functions used in the plots
..........................................................................................................................
"""
text_remote = """
# 11.5):
--------------------------------------------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------------------------------------------
[py_remote]
    This folder is used for storing python code using for reading the database in a ssh server
..........................................................................................................................
"""
# ------------------------------------------------------------------------------------------------------------------------
# Print the documentation
# ------------------------------------------------------------------------------------------------------------------------
docfile = open(file_documentation, 'w')
print(__doc__,file=docfile)
# -----------------------------------------------------------------------------------------------------------------------
# Functions of the main text folder
# -----------------------------------------------------------------------------------------------------------------------
print(text_main,file=docfile)
print("#  1)",file=docfile)
print(get_docstring('./check_data.py'),file=docfile)
print("#  2)",file=docfile)
print(get_docstring('./create_uvstruc_dataset.py'),file=docfile)
print("#  3)",file=docfile)
print(get_docstring('./main_CNN.py'),file=docfile)
print("#  4)",file=docfile)
print(get_docstring('./main_SHAP.py'),file=docfile)
print("#  5)",file=docfile)
print(get_docstring('./main_statistics.py'),file=docfile)
print("#  6)",file=docfile)
print(get_docstring('./main_uvstruc.py'),file=docfile)
print("#  7)",file=docfile)
print(get_docstring('./plot_training_epoch.py'),file=docfile)
print("#  8)",file=docfile)
print(get_docstring('./plot_umean.py'),file=docfile)
print("#  9)",file=docfile)
print(get_docstring('./plot_urms.py'),file=docfile)
print("#  10)",file=docfile)
print(get_docstring('./prepare_data.py'),file=docfile)
# -----------------------------------------------------------------------------------------------------------------------
# Folder containing python modules
# -----------------------------------------------------------------------------------------------------------------------
print(text_bin,file=docfile)
print(text_class,file=docfile)
# -----------------------------------------------------------------------------------------------------------------------
# ann_config.py
# -----------------------------------------------------------------------------------------------------------------------
print("#  11.1.1)",file=docfile)
print(get_docstring('./py_bin/py_class/ann_config.py'),file=docfile)
from py_bin.py_class.ann_config import deep_model
print(deep_model.__doc__,file=docfile)
print(deep_model.__init__.__doc__,file=docfile)
print(deep_model.define_model.__doc__,file=docfile)
print(deep_model.create_model.__doc__,file=docfile)
print(deep_model.model_base.__doc__,file=docfile)
print(deep_model.train_model.__doc__,file=docfile)
print(deep_model.prepare_data.__doc__,file=docfile)
print(deep_model.architecture_Unet.__doc__,file=docfile)
print(deep_model.check_data.__doc__,file=docfile)
del deep_model
# -----------------------------------------------------------------------------------------------------------------------
# flow_field.py
# -----------------------------------------------------------------------------------------------------------------------
print("#  11.1.2)",file=docfile)
print(get_docstring('./py_bin/py_class/flow_field.py'),file=docfile)
from py_bin.py_class.flow_field import flow_field
print(flow_field.__doc__,file=docfile)
print(flow_field.__init__.__doc__,file=docfile)
print(flow_field.shape_tensor.__doc__,file=docfile)
print(flow_field.flow_grid.__doc__,file=docfile)
del flow_field
# -----------------------------------------------------------------------------------------------------------------------
# plot_format.py
# -----------------------------------------------------------------------------------------------------------------------
print("#  11.1.3)",file=docfile)
print(get_docstring('./py_bin/py_class/plot_format.py'),file=docfile)
from py_bin.py_class.plot_format import plot_format
print(plot_format.__doc__,file=docfile)
print(plot_format.__init__.__doc__,file=docfile)
print(plot_format.create_figure.__doc__,file=docfile)
print(plot_format.add_plot_2d.__doc__,file=docfile)
print(plot_format.plot_layout.__doc__,file=docfile)
print(plot_format.plot_save_png.__doc__,file=docfile)
print(plot_format.plot_save_pdf.__doc__,file=docfile)
del plot_format
# -----------------------------------------------------------------------------------------------------------------------
# shap_config.py
# -----------------------------------------------------------------------------------------------------------------------
print("#  11.1.4)",file=docfile)
print(get_docstring('./py_bin/py_class/shap_config.py'),file=docfile)
from py_bin.py_class.shap_config import shap_config
print(shap_config.__doc__,file=docfile)
print(shap_config.__init__.__doc__,file=docfile)
print(shap_config.calc_gradientSHAP.__doc__,file=docfile)
print(shap_config.write_shap.__doc__,file=docfile)
print(shap_config.read_shap.__doc__,file=docfile)
print(shap_config.gradientSHAP_model.__doc__,file=docfile)
print(shap_config.model_base_shap.__doc__,file=docfile)
print(shap_config.background.__doc__,file=docfile)
del shap_config
# -----------------------------------------------------------------------------------------------------------------------
# structures.py
# -----------------------------------------------------------------------------------------------------------------------
print("#  11.1.5)",file=docfile)
print(get_docstring('./py_bin/py_class/structures.py'),file=docfile)
from py_bin.py_class.structures import structures
print(structures.__doc__,file=docfile)
print(structures.__init__.__doc__,file=docfile)
print(structures.separate_structures.__doc__,file=docfile)
print(structures.physicalproperties_structures.__doc__,file=docfile)
print(structures.detect_quadrant.__doc__,file=docfile)
print(structures.segmentation.__doc__,file=docfile)
print(structures.structure_u1u2.__doc__,file=docfile)
print(structures.structure_shap.__doc__,file=docfile)
del structures
# -----------------------------------------------------------------------------------------------------------------------
# uv_structure.py
# -----------------------------------------------------------------------------------------------------------------------
print("#  11.1.6)",file=docfile)
print(get_docstring('./py_bin/py_class/uv_structure.py'),file=docfile)
from py_bin.py_class.uv_structure import uv_structure
print(uv_structure.__doc__,file=docfile)
print(uv_structure.__init__.__doc__,file=docfile)
print(uv_structure.calculate_matstruc.__doc__,file=docfile)
print(uv_structure.segment_struc.__doc__,file=docfile)
print(uv_structure.save_struc.__doc__,file=docfile)
print(uv_structure.read_struc.__doc__,file=docfile)
del uv_structure
# -----------------------------------------------------------------------------------------------------------------------
# Functions for the calculation
# -----------------------------------------------------------------------------------------------------------------------
print(text_functions,file=docfile)
# -----------------------------------------------------------------------------------------------------------------------
# CNNblock_definition.py
# -----------------------------------------------------------------------------------------------------------------------
print("#  11.2.1)",file=docfile)
print(get_docstring('./py_bin/py_functions/CNNblock_definition.py'),file=docfile)
import py_bin.py_functions.CNNblock_definition as CNNblock_definition
print(CNNblock_definition.block.__doc__,file=docfile)
print(CNNblock_definition.invblock.__doc__,file=docfile)
del CNNblock_definition
# -----------------------------------------------------------------------------------------------------------------------
# multiworker_checkpoint.py
# -----------------------------------------------------------------------------------------------------------------------
print("#  11.2.2)",file=docfile)
print(get_docstring('./py_bin/py_functions/multiworker_checkpoint.py'),file=docfile)
# -----------------------------------------------------------------------------------------------------------------------
# norm_velocity.py
# -----------------------------------------------------------------------------------------------------------------------
print("#  11.2.3)",file=docfile)
print(get_docstring('./py_bin/py_functions/norm_velocity.py'),file=docfile)
import py_bin.py_functions.norm_velocity as norm_velocity
print(norm_velocity.norm_velocity.__doc__,file=docfile)
print(norm_velocity.dim_velocity.__doc__,file=docfile)
del norm_velocity
# -----------------------------------------------------------------------------------------------------------------------
# normalization.py
# -----------------------------------------------------------------------------------------------------------------------
print("#  11.2.4)",file=docfile)
print(get_docstring('./py_bin/py_functions/normalization.py'),file=docfile)
import py_bin.py_functions.normalization as normalization
print(normalization.save_norm.__doc__,file=docfile)
print(normalization.read_norm.__doc__,file=docfile)
print(normalization.calc_norm.__doc__,file=docfile)
del normalization
# -----------------------------------------------------------------------------------------------------------------------
# read_norm_velocity.py
# -----------------------------------------------------------------------------------------------------------------------
print("#  11.2.5)",file=docfile)
print(get_docstring('./py_bin/py_functions/read_norm_velocity.py'),file=docfile)
import py_bin.py_functions.read_norm_velocity as read_norm_velocity
print(read_norm_velocity.read_norm_velocity.__doc__,file=docfile)
del read_norm_velocity
# -----------------------------------------------------------------------------------------------------------------------
# read_velocity.py
# -----------------------------------------------------------------------------------------------------------------------
print("#  11.2.6)",file=docfile)
print(get_docstring('./py_bin/py_functions/read_velocity.py'),file=docfile)
import py_bin.py_functions.read_velocity as read_velocity
print(read_velocity.read_velocity.__doc__,file=docfile)
del read_velocity
# -----------------------------------------------------------------------------------------------------------------------
# trainvali_data.py
# -----------------------------------------------------------------------------------------------------------------------
print("#  11.2.7)",file=docfile)
print(get_docstring('./py_bin/py_functions/trainvali_data.py'),file=docfile)
import py_bin.py_functions.trainvali_data as trainvali_data
print(trainvali_data._read_datatf_function.__doc__,file=docfile)
print(trainvali_data.prepare_data_tf.__doc__,file=docfile)
print(trainvali_data.read_data_tf.__doc__,file=docfile)
print(trainvali_data.check_data_tf.__doc__,file=docfile)
print(trainvali_data.read_inout_notprepared.__doc__,file=docfile)
print(trainvali_data.data_traintest_tf.__doc__,file=docfile)
del trainvali_data
# -----------------------------------------------------------------------------------------------------------------------
# umean.py
# -----------------------------------------------------------------------------------------------------------------------
print("#  11.2.8)",file=docfile)
print(get_docstring('./py_bin/py_functions/umean.py'),file=docfile)
import py_bin.py_functions.umean as umean
print(umean.save_Umean.__doc__,file=docfile)
print(umean.read_Umean.__doc__,file=docfile)
print(umean.calc_Umean.__doc__,file=docfile)
del umean
# -----------------------------------------------------------------------------------------------------------------------
# urms.py
# -----------------------------------------------------------------------------------------------------------------------
print("#  11.2.9)",file=docfile)
print(get_docstring('./py_bin/py_functions/urms.py'),file=docfile)
import py_bin.py_functions.urms as urms
print(urms.read_rms.__doc__,file=docfile)
print(urms.save_rms.__doc__,file=docfile)
print(urms.calc_rms.__doc__,file=docfile)
del urms
# -----------------------------------------------------------------------------------------------------------------------
# Modified packages for the calculation
# -----------------------------------------------------------------------------------------------------------------------
print(text_packages,file=docfile)
# -----------------------------------------------------------------------------------------------------------------------
# Functions used for plotting the information
# -----------------------------------------------------------------------------------------------------------------------
print(text_plots,file=docfile)
# -----------------------------------------------------------------------------------------------------------------------
# plottrain.py
# -----------------------------------------------------------------------------------------------------------------------
print("#  11.4.1)",file=docfile)
print(get_docstring('./py_bin/py_plots/plottrain.py'),file=docfile)
import py_bin.py_plots.plottrain as plottrain
print(plottrain.plottrain.__doc__,file=docfile)
del plottrain
# -----------------------------------------------------------------------------------------------------------------------
# plotumean.py
# -----------------------------------------------------------------------------------------------------------------------
print("#  11.4.2)",file=docfile)
print(get_docstring('./py_bin/py_plots/plotumean.py'),file=docfile)
import py_bin.py_plots.plotumean as plotumean
print(plotumean.plotumean.__doc__,file=docfile)
del plotumean
# -----------------------------------------------------------------------------------------------------------------------
# ploturms.py
# -----------------------------------------------------------------------------------------------------------------------
print("#  11.4.3)",file=docfile)
print(get_docstring('./py_bin/py_plots/ploturms.py'),file=docfile)
import py_bin.py_plots.ploturms as ploturms
print(ploturms.ploturms.__doc__,file=docfile)
del ploturms
# -----------------------------------------------------------------------------------------------------------------------
# Functions used for connecting the ssh server
# -----------------------------------------------------------------------------------------------------------------------
print(text_remote,file=docfile)
print("#  11.5.1)",file=docfile)
print(get_docstring('./py_bin/py_remote/read_remote.py'),file=docfile)
import py_bin.py_remote.read_remote as read_remote
print(read_remote.recursivedelete.__doc__,file=docfile)
print(read_remote._get_r_portable.__doc__,file=docfile)
print(read_remote.read_from_server.__doc__,file=docfile)
del read_remote
docfile.close()
with open(file_documentation, 'r') as ff:
    print(ff.read())

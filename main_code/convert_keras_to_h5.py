# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 16:39:23 2024

@author: andre
"""

import tensorflow as tf
import h5py
import numpy as np

model_keras = "../../../scratch/P125/models/trained_model_5285.keras"
model_h5 = "../../../scratch/P125/models/trained_model_5285.weights.h5"

model0 = tf.keras.models.load_model(model_keras)
# model0.save(model_h5,save_format='h5')
weights = model0.get_weights()
print(len(weights))

ff=h5py.File(model_h5,'w')
for ii in np.arange(len(weights)):
    ff.create_dataset('weights_'+str(ii), data=weights[ii])
# model0.save_weights(model_h5)
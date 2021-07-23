# Import necessary librairies

import numpy as np

import sys
import os

import tensorflow as tf
import tensorflow.keras
from tensorflow.keras.layers import  Layer
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Conv2D, Input, Dense, Flatten,  Reshape, Cropping2D, Conv2DTranspose, PReLU, Lambda, BatchNormalization
import tensorflow_probability as tfp


def create_model_vae(input_shape, latent_dim, hidden_dim, filters, kernels, final_dim, conv_activation=None, dense_activation=None):
    input_layer_1 = Input(shape=(input_shape)) 
    input_layer_2 = Input(shape=(input_shape)) 

    h = BatchNormalization()(input_layer_1)
    h_2 = input_layer_2
    for i in range(len(filters)):
        h = Conv2D(filters[i], (kernels[i],kernels[i]), activation=None, padding='same')(h)
        h = PReLU()(h)
        h = Conv2D(filters[i], (kernels[i],kernels[i]), activation=None, padding='same', strides=(2,2))(h)
        h = PReLU()(h)

    h = Flatten()(h)
    h = PReLU()(h)
    h = Dense(tfp.layers.MultivariateNormalTriL.params_size(32),
                activation=None)(h)
    h = tfp.layers.MultivariateNormalTriL(32,activity_regularizer=tfp.layers.KLDivergenceRegularizer(prior, weight=0.01))(tf.cast(h,tf.float32))
    
    
    
    h = PReLU()(h)
    h = Dense(tfp.layers.MultivariateNormalTriL.params_size(32))(h)
    h = PReLU()(h)
    w = int(np.ceil(input_shape[0]/2**(len(filters))))
    h = Dense(w*w*filters[-1], activation=dense_activation)(tf.cast(h,tf.float32))
    h = PReLU()(h)
    h = Reshape((w,w,filters[-1]))(h)
    for i in range(len(filters)-1,-1,-1):
        h = Conv2DTranspose(filters[i], (kernels[i],kernels[i]), activation=conv_activation, padding='same', strides=(2,2))(h)
        h = PReLU()(h)
        h = Conv2DTranspose(filters[i], (kernels[i],kernels[i]), activation=conv_activation, padding='same')(h)
        h = PReLU()(h)
    h = Conv2D(input_shape[-1], (3,3), activation='relu', padding='same')(h)

    cropping = int(h.get_shape()[1]-input_shape[0])
    if cropping>0:
        print('in cropping')
        if cropping % 2 == 0:
            h = Cropping2D(cropping/2)(h)
        else:
            h = Cropping2D(((cropping//2,cropping//2+1),(cropping//2,cropping//2+1)))(h)


    model = Model([input_layer_1, input_layer_2],h)

    return model

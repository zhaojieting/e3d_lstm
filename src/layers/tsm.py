"""Module for constructing TSN layers Cells."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf
import tensorflow.contrib.layers as layers

def TSM_layer(inputs, output_channels, kernel_shape, padding='same'):
        with tf.variable_scope('generator'):
                input_shape = inputs.shape
                inputs = tf.unstack(inputs)
                out_puts = np.zeros(input_shape)

                for i in range(len(inputs)):
                        input = tf.unstack(inputs[i])
                        shift_input = np.zeros(input_shape[1:])
                        out_puts[i] = shift_input + inputs

                out_puts = tf.stack(out_puts)
                out_puts = out_puts.views(-1, input_shape[2], input_shape[3], input_shape[4])
                tf.layers.conv2d(out_puts, output_channels, [5, 5], padding=padding)
                out_puts = out_puts.views(input_shape[0], input_shape[1], input_shape[2], input_shape[3], input_shape[4])

                return out_puts
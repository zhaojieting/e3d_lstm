#2D lstm  卷积
"""
if self._conv_ndims == 2:
      inputs_shape = inputs.shape
      inputs = tf.reshape(inputs,[-1,inputs.shape[2].value,inputs.shape[3].value, inputs.shape[4].value] )
      if kernel_shape == [2, 5, 5]:
          kernel_shape = kernel_shape[1:]
      tmp = tf.layers.conv2d(inputs, output_channels, kernel_shape, padding="same")
      shape = tmp.shape
      return tf.reshape(tmp, (inputs_shape[0], inputs_shape[1], inputs_shape[2], inputs_shape[3], shape[3]))
"""


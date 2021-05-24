
#shift
"""
      input_shape = inputs.shape

      if kernel_shape == [2, 5, 5]:
          kernel_shape = kernel_shape[1:]
          shift_input_left = inputs[:,1:,:,:,:input_shape[4].value]
          shift_input_right = inputs[:,:1,:,:,:input_shape[4].value]
          shift_input = tf.concat([shift_input_left, shift_input_right], 1)
          out_puts_1 = tf.reshape(inputs, [-1, input_shape[2], input_shape[3], input_shape[4]])
          out_puts_1 = tf.layers.conv2d(out_puts_1, output_channels, kernel_shape, padding="same")

          out_puts_2 = tf.reshape(shift_input, [-1, input_shape[2], input_shape[3], input_shape[4]])
          out_puts_2 = tf.layers.conv2d(out_puts_2, output_channels, kernel_shape, padding="same")

          out_puts = tf.reshape(out_puts_1 + out_puts_2 ,[input_shape[0], input_shape[1], input_shape[2], input_shape[3], -1])
      else:
          out_puts = tf.layers.conv3d(inputs, output_channels, kernel_shape, padding="same")
      return out_puts
"""
# import tensorflow as tf

input_shape = inputs.shape

if kernel_shape == [2, 5, 5]:
  kernel_shape = kernel_shape[1:]
  shift_input_left = inputs[:, 1:, :, :, :input_shape[4].value/2]
  shift_input_left = tf.concat([shift_input_left, tf.zeros([input_shape[0], 1, input_shape[2], input_shape[3]], input_shape[4].value/2)], 4)
  shift_input_right = inputs[:, :1, :, :, :input_shape[4].value/2]
  shift_input_right = tf.concat([shift_input_right, tf.zeros([input_shape[0], 1, input_shape[2], input_shape[3]], input_shape[4].value/2)], 4)
  shift_input = tf.concat([shift_input_left, shift_input_right], 1)
  out_puts_1 = tf.reshape(inputs, [-1, input_shape[2], input_shape[3], input_shape[4]])
  out_puts_1 = tf.layers.conv2d(out_puts_1, output_channels, kernel_shape, padding="same")
  out_puts_2 = tf.reshape(shift_input, [-1, input_shape[2], input_shape[3], input_shape[4]])
  out_puts_2 = tf.layers.conv2d(out_puts_2, output_channels, kernel_shape, padding="same")
  out_puts = tf.reshape(out_puts_1 + out_puts_2, [input_shape[0], input_shape[1], input_shape[2], input_shape[3], -1])
else:
  out_puts = tf.layers.conv3d(inputs, output_channels, kernel_shape, padding="same")

return out_puts
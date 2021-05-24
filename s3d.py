input_shape = inputs.shape

if kernel_shape == [2, 5, 5]:
  tmp = tf.layers.conv3d(inputs, output_channels, [1, 5, 5], padding="same")
  out_puts = tf.layers.conv2d(tmp, output_channels, [2, 1, 1], padding="same")
else:
  out_puts = tf.layers.conv3d(inputs, output_channels, kernel_shape, padding="same")
return out_puts
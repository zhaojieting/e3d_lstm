# import numpy as np
# import tensorflow as tf
# # from torch.utils.data import Dataset
# # import torch
# # c = np.ones((2,2,5,1,64,64))
# # b = np.zeros((10,1,64,64))
# # b[:5,:] = c[0][0]
# # b[5:,:] = c[0][1]
# # print(b)
# FLAGS = tf.flags.FLAGS
# tf.flags.DEFINE_string('train_data_paths', '', 'test')
#
#
#
# def main(_):
#     print(FLAGS.train_data_paths)
#
# if __name__ == '__main__':
#   tf.app.run()

import random
a = range(10)
b = random.shuffle(a)
print a
print b

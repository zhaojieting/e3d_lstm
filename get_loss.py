import numpy as np
import tensorflow as tf
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

# import random
# a = range(10)
# b = random.shuffle(a)
# print a
# print b
# sess = tf.Session()
# with sess.as_default():
#     a = tf.ones((1,4,4,8))
#     shape = a.shape
#     b = tf.concat([a, tf.zeros((1, 4, 4, 8))], 0)
#     print b.shape
#     print b.eval()
# print a
# c = np.zeros(shape)
# c = a[:, :, 1:]
# print a.shape
# print c.shape
#
# s = 'hello world'
# for i in range(10):
#     with open('test.txt', 'a') as f:
#         f.write(s)
# a = tf.ones((1, 3, 3, 16))
# a = tf.layers.conv2d(a, 64, (3, 3))
# print a.shape
# print a.shape[0]
# gx = np.array([1, -2])
# gx = np.maximum(gx, 0)
# tf.variable_scope(self._layer_name)
# print gx
i = 0
with open('kth_tsk_lstm.txt', 'r') as f1:
    lines = f1.readlines()
    lines = lines[8000:]
    for line in lines:
        i += 1
        with open('kth_tsm_lstm.txt', 'a') as f2:
            f2.write(line)
import time
import numpy as np
import re
import matplotlib.pyplot as plt


x = np.linspace(0, 10000, 10000)
y1 = []
with open('tsm_lstm_a_loss.txt', 'r') as f1:
    lines = f1.readlines()
    pattern = re.compile(r'training loss: (\d+\.\d+)')
    i = 0
    for line in lines:
        loss = pattern.findall(line)
        loss = float(loss[0])
        y1.append(loss)
        if len(y1)==10000:
            break
y2 = []
with open('e3d_lstm_loss.txt', 'r') as f2:
    lines = f2.readlines()
    pattern = re.compile(r'training loss: (\d+\.\d+)')
    i = 0
    for line in lines:
        loss = pattern.findall(line)
        loss = float(loss[0])
        y2.append(loss)
        if len(y2)==10000:
            break

y3 = []
with open('e2d_lstm_loss.txt', 'r') as f3:
    lines = f3.readlines()
    pattern = re.compile(r'training loss: (\d+\.\d+)')
    i = 0
    for line in lines:
        loss = pattern.findall(line)
        loss = float(loss[0])
        y3.append(loss)
        if len(y3)==10000:
            break

y4 = []
with open('s3d_lstm_loss.txt', 'r') as f4:
    lines = f4.readlines()
    pattern = re.compile(r'training loss: (\d+\.\d+)')
    i = 0
    for line in lines:
        loss = pattern.findall(line)
        loss = float(loss[0])
        y4.append(loss)
        if len(y4)==10000:
            break

y5 = []
with open('tsm_b_lstm_loss.txt', 'r') as f5:
    lines = f5.readlines()
    pattern = re.compile(r'training loss: (\d+\.\d+)')
    for line in lines:
        loss = pattern.findall(line)
        loss = float(loss[0])
        y5.append(loss)
        if len(y5)==10000:
            break

plt.figure(figsize=(20, 10))
plt.plot(x,y3,color="yellow", label = 'e2d')
plt.plot(x,y2,color="blue", label = 'e3d')
plt.plot(x,y4,color="green", label = 's3d')
plt.plot(x,y5,color="black", label = 'tsm-b')
plt.plot(x,y1,color="red", label = 'tsm-a')

fontdict = {'size':16}
plt.xlabel("iteration", fontdict=fontdict)
plt.ylabel("loss",fontdict=fontdict)
plt.text(8500, 9400, 'TSM-LSTM-a: ', withdash=True)
plt.text(8500, 9000, 'TSM-LSTM-b: ', withdash=True)
plt.text(8500, 8600, 'S3D-LSTM: ', withdash=True)
plt.text(8500, 8200, 'E3D-LSTM: ', withdash=True)
plt.text(8500, 7800, 'E2D-LSTM: ', withdash=True)
fontdict = {'size':32}
plt.text(9300, 9300, '--------', withdash=True, color="red", fontdict=fontdict)
plt.text(9300, 8900, '--------', withdash=True, color="black", fontdict=fontdict)
plt.text(9300, 8500, '--------', withdash=True, color='green', fontdict=fontdict)
plt.text(9300, 8100, '--------', withdash=True, color='blue', fontdict=fontdict)
plt.text(9300, 7700, '--------', withdash=True, color='yellow', fontdict=fontdict)
plt.ylim(0, 10000)
plt.show()

# plt.savefig('quxiantu.png',dpi=120,bbox_inches='tight')
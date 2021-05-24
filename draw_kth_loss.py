import time
import numpy as np
import re
import matplotlib.pyplot as plt


x = np.linspace(0, 8000, 8000)
y1 = []
with open('kth_e3d.txt', 'r') as f1:
    lines = f1.readlines()
    pattern = re.compile(r'training loss: (\d+\.\d+)')
    i = 0
    for line in lines:
        loss = pattern.findall(line)
        loss = float(loss[0])
        y1.append(loss)
        if len(y1)==8000:
            break

y2 = []
with open('kth_tsm_lstm.txt', 'r') as f2:
    lines = f2.readlines()
    pattern = re.compile(r'training loss: (\d+\.\d+)')
    i = 0
    for line in lines:
        loss = pattern.findall(line)
        loss = float(loss[0])
        y2.append(loss)
        if len(y2)==8000:
            break

plt.figure(figsize=(20, 10))
plt.plot(x,y1,color="red", label = 'e3d')
plt.plot(x,y2,color="blue", label = 'tsm')

fontdict = {'size':16}
plt.xlabel("iteration", fontdict=fontdict)
plt.ylabel("loss",fontdict=fontdict)

plt.text(6800, 36500, 'TSM-LSTM-b: ', withdash=True)
plt.text(6800, 35500, 'E3D-LSTM: ', withdash=True)
fontdict = {'size':32}
plt.text(7500, 36000, '--------', withdash=True, color='blue', fontdict=fontdict)
plt.text(7500, 35000, '--------', withdash=True, color="red", fontdict=fontdict)
plt.ylim(0, 40000)
plt.show()
import matplotlib.pyplot as plt
import numpy as np
import io

path = '/Users/xiejiacheng/coding/result.csv'

train_loss = []
vailf_loss = []
x = []

with open(path, 'r') as file:
    for index, content in enumerate(file.readlines()):
        # print(index, co[]
        # # print(content)
        # if index == 0:
        #     continue

        x.append(index)
        # ACC
        # train_loss.append(float(content.split()[4]))
        # vailf_loss.append(float(content.split()[8]))

        # # loss
        train_loss.append(float(content.split()[2]))
        vailf_loss.append(float(content.split()[6]))
# for i in range(len(train_loss)-1):
#     x = train_loss[i]
#     y = vailf_loss[1]


plt.figure()
# ACC
# plt.plot(x, train_loss, label = 'tran_acc')
# plt.plot(x, vailf_loss,color = 'red', label = 'val_acc')

# loss
plt.plot(x, train_loss, label = 'train_loss')
plt.plot(x, vailf_loss,color = 'red', label = 'val_loss')

plt.legend(loc = 'best')
plt.show()
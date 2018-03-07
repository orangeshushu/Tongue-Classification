import torch
import torch.nn as nn
from torch.autograd import Variable
import torch.utils.data as Data
import torchvision
#import matplotlib.pyplot as plt
from torchvision import transforms, utils


# torch.manual_seed(1)    # reproducible
# Hyper Parameters
EPOCH = 100               # train the training data n times, to save time, we just train 1 epoch
BATCH_SIZE = 20
LR = 0.001              # learning rate

train_data = torchvision.datasets.ImageFolder('/Users/xiejiacheng/coding/Image_augmentation/train',
                                              transform=transforms.Compose([
                                                # transforms.Scale(256),
                                                # transforms.CenterCrop(224),
                                                transforms.ToTensor()]))
print(len(train_data))
train_loader = torch.utils.data.DataLoader(dataset=train_data, batch_size=BATCH_SIZE, shuffle=True)
print(len(train_loader))

test_data = torchvision.datasets.ImageFolder('/Users/xiejiacheng/coding/Image_augmentation/val',
                                             transform=transforms.Compose([
                                                # transforms.Scale(256),
                                                # transforms.CenterCrop(224),
                                                transforms.ToTensor()]))
print(len(test_data))
test_loader = torch.utils.data.DataLoader(dataset=test_data, batch_size=BATCH_SIZE, shuffle=True)
print(len(test_loader))

class Net(torch.nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = torch.nn.Sequential(
            torch.nn.Conv2d(3, 6, 5, 1, 1),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2))
        self.conv2 = torch.nn.Sequential(
            torch.nn.Conv2d(6, 16, 5, 1, 1),
            torch.nn.ReLU(),
            torch.nn.MaxPool2d(2)
        )
        self.dense = torch.nn.Sequential(
            torch.nn.Linear(46656, 150),
            torch.nn.ReLU(),
            torch.nn.Linear(150, 84),
            torch.nn.ReLU(),
            torch.nn.Linear(84, 10)
        )

    def forward(self, x):
        conv1_out = self.conv1(x)
        conv2_out = self.conv2(conv1_out)
        res = conv2_out.view(conv2_out.size(0), -1)
        out = self.dense(res)
        return out


model = Net()
print(model)

optimizer = torch.optim.Adam(model.parameters())
loss_func = torch.nn.CrossEntropyLoss()

for epoch in range(EPOCH):
    print('epoch {}'.format(epoch + 1))
    # training-----------------------------
    train_loss = 0.
    train_acc = 0.
    for batch_x, batch_y in train_loader:
        batch_x, batch_y = Variable(batch_x), Variable(batch_y)
        out = model(batch_x)
        loss = loss_func(out, batch_y)
        train_loss += loss.data[0]
        pred = torch.max(out, 1)[1]
        train_correct = (pred == batch_y).sum()
        train_acc += train_correct.data[0]
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
    print('Train Loss: {:.6f}, Acc: {:.6f}'.format(train_loss / (len(
        train_data)), train_acc / (len(train_data))))

    # evaluation--------------------------------
    model.eval()
    eval_loss = 0.
    eval_acc = 0.
    for batch_x, batch_y in test_loader:
        batch_x, batch_y = Variable(batch_x, volatile=True), Variable(batch_y, volatile=True)
        out = model(batch_x)
        loss = loss_func(out, batch_y)
        eval_loss += loss.data[0]
        pred = torch.max(out, 1)[1]
        num_correct = (pred == batch_y).sum()
        eval_acc += num_correct.data[0]
    print('Test Loss: {:.6f}, Acc: {:.6f}'.format(eval_loss / (len(
        test_data)), eval_acc / (len(test_data))))

torch.save(model, 'net0201.pkl')

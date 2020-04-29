import os
import random

trainval_percent = 0.8
train_percent = 0.7
xmlfilepath = r'D:\Code\Python\data\BITVehicle_Dataset\annotations'
txtsavepath = r'D:\Code\Python\data\BITVehicle_Dataset\train_test'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open(txtsavepath + '/trainval.txt', 'w')
ftest = open(txtsavepath + '/test.txt', 'w')
ftrain = open(txtsavepath + '/train.txt', 'w')
fval = open(txtsavepath + '/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    # print(len(total_xml[i][:-4]))
    if len(total_xml[i][:-4]) == 7:
        # name = total_xml[i][:-4][1:]+'\n'
        print(name)
    # if(len(total_xml[i][:-4])==6):
    # name=total_xml[i][:-4]+'\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftrain.write(name)
        else:
            fval.write(name)
    else:
        ftest.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()

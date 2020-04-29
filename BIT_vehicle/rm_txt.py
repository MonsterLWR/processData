import os

train_r = open('VOCdevkit2007/VOC2007/ImageSets/Main/train.txt', 'r')
test_r = open('VOCdevkit2007/VOC2007/ImageSets/Main/test.txt', 'r')
val_r = open('VOCdevkit2007/VOC2007/ImageSets/Main/val.txt', 'r')
train_val_r = open('VOCdevkit2007/VOC2007/ImageSets/Main/trainval.txt', 'r')

train = open('VOCdevkit2007/VOC2007/ImageSets/Main/trainw.txt', 'w')
test = open('VOCdevkit2007/VOC2007/ImageSets/Main/testw.txt', 'w')
val = open('VOCdevkit2007/VOC2007/ImageSets/Main/valw.txt', 'w')
train_val = open('VOCdevkit2007/VOC2007/ImageSets/Main/trainvalw.txt', 'w')

lines = train_r.readlines()
for line in lines:
    if not os.path.exists('VOCdevkit2007/VOC2007/JPEGImages/' + line.replace("\n", "") + '.jpg'):
        continue
    train.write(line)
os.system('mv VOCdevkit2007/VOC2007/ImageSets/Main/trainw.txt VOCdevkit2007/VOC2007/ImageSets/Main/train.txt')

lines = test_r.readlines()
for line in lines:
    if not os.path.exists('VOCdevkit2007/VOC2007/JPEGImages/' + line.replace("\n", "") + '.jpg'):
        continue
    test.write(line)
os.system('mv VOCdevkit2007/VOC2007/ImageSets/Main/testw.txt VOCdevkit2007/VOC2007/ImageSets/Main/test.txt')

lines = val_r.readlines()
for line in lines:
    if not os.path.exists('VOCdevkit2007/VOC2007/JPEGImages/' + line.replace("\n", "") + '.jpg'):
        continue
    val.write(line)
os.system('mv VOCdevkit2007/VOC2007/ImageSets/Main/valw.txt VOCdevkit2007/VOC2007/ImageSets/Main/val.txt')

lines = train_val_r.readlines()
for line in lines:
    if not os.path.exists('VOCdevkit2007/VOC2007/JPEGImages/' + line.replace("\n", "") + '.jpg'):
        continue
    train_val.write(line)
os.system('mv VOCdevkit2007/VOC2007/ImageSets/Main/trainvalw.txt VOCdevkit2007/VOC2007/ImageSets/Main/trainval.txt')

import xml.etree.ElementTree as ET
import pickle
import os
import glob
from os import listdir, getcwd
from os.path import join

classes = ["truck", "bus", "sedan", "microbus", "minivan", "suv"]


def convert(size, box):
    dw = 1. / (size[0])
    dh = 1. / (size[1])
    x = (box[0] + box[1]) / 2.0 - 1
    y = (box[2] + box[3]) / 2.0 - 1
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h


def convert_annotation(xml_file, out_file):
    # in_file = open('VOCdevkit/VOC%s/Annotations/%s.xml' % (year, image_id))
    # out_file = open('VOCdevkit/VOC%s/labels/%s.txt' % (year, image_id), 'w')
    out_file = open(out_file, 'w')
    tree = ET.parse(xml_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
             float(xmlbox.find('ymax').text))
        bb = convert((w, h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


# wd = getcwd()

data_dir = r'D:\Code\Python\data\BITVehicle_Dataset'
img_dir = 'imgs'
target_dir = 'yolo_labels'
# annotation_dir = 'annotations'
# xml_dir = 'annotations'

sets = [('trainval', 'train_test/trainval'), ('test', 'train_test/test')]

for dir_type, xml_dir in sets:
    if not os.path.exists(os.path.join(data_dir, target_dir)):
        os.makedirs(os.path.join(data_dir, target_dir))

    print('converting {}...'.format(dir_type))
    xml_files = glob.glob(os.path.join(data_dir, xml_dir, '*.xml'))
    image_names = [os.path.basename(file).split('.')[0] for file in xml_files]

    target_file = open(os.path.join(data_dir, target_dir, '%s.txt' % dir_type), 'w')
    count = 0
    for image_name in image_names:
        if count % 100 == 0:
            print('converting complete {} imgs'.format(count))
        target_file.write('%s/%s/%s.jpg\n' % (data_dir, img_dir, image_name))
        convert_annotation(os.path.join(data_dir, xml_dir, '%s.xml' % image_name),
                           os.path.join(data_dir, target_dir, '%s.txt' % image_name))
        count += 1
    target_file.close()

# os.system("cat 2007_train.txt 2007_val.txt 2012_train.txt 2012_val.txt > train.txt")
# os.system("cat 2007_train.txt 2007_val.txt 2007_test.txt 2012_train.txt 2012_val.txt > train.all.txt")

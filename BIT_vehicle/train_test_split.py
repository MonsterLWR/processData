import os
import random
import time
import shutil
from sklearn.model_selection import train_test_split

# bit data
# xmlfilepath = r'D:\Code\Python\data\BITVehicle_Dataset\annotations'
# saveBasePath = r"D:\Code\Python\data\BITVehicle_Dataset\train_test_split"

# self_made data
xmlfilepath = r'D:\Code\Python\data\toycar\xml_label'
saveBasePath = r"D:\Code\Python\data\toycar\csv"

for dir in ['test', 'train_val']:
    if not os.path.exists(os.path.join(saveBasePath, dir)):
        os.mkdir(os.path.join(saveBasePath, dir))

if __name__ == '__main__':
    xml_files = os.listdir(xmlfilepath)
    print(xml_files)
    train, test = train_test_split(xml_files, test_size=0.3, train_size=0.7)

    print('processing train_val set---')
    for img_label in train:
        origin_xml = os.path.join(xmlfilepath, img_label)
        target_xml = os.path.join(saveBasePath, 'train_val', img_label)
        shutil.copyfile(origin_xml, target_xml)

    print('processing test set---')
    for img_label in test:
        origin_xml = os.path.join(xmlfilepath, img_label)
        target_xml = os.path.join(saveBasePath, 'test', img_label)
        shutil.copyfile(origin_xml, target_xml)


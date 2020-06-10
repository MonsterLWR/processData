import os
import shutil

base_dir = r'D:\Code\Python\data\BITVehicle_Dataset'
test_imgs = os.path.join(base_dir, 'test_imgs')
imgs = os.path.join(base_dir, 'imgs')

test_xml = os.path.join(base_dir, 'train_test_split', 'test')
test_xmls = os.listdir(test_xml)

for xml in test_xmls:
    img_name = os.path.basename(xml)
    img_name = img_name.split('.')[0] + '.jpg'
    shutil.copy(os.path.join(imgs, img_name), os.path.join(test_imgs, img_name))

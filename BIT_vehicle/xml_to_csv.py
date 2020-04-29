import os
import glob
import pandas as pd
import xml.etree.ElementTree as ET


def xml_to_csv(path):
    xml_list = []
    for xml_file in glob.glob(path + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        # print(root)
        print(root.find('filename').text)
        for member in root.findall('object'):
            value = (root.find('filename').text,
                     int(root.find('size').find('width').text),  # width
                     int(root.find('size').find('height').text),  # height
                     member[0].text,
                     int(member[4][0].text),
                     int(float(member[4][1].text)),
                     int(member[4][2].text),
                     int(member[4][3].text)
                     )
            xml_list.append(value)
    column_name = ['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax']
    xml_df = pd.DataFrame(xml_list, columns=column_name)
    return xml_df


def main(xml_path, csv_dir, csv_name='bit_label'):
    xml_df = xml_to_csv(xml_path)
    if not os.path.exists(csv_dir):
        os.mkdir(csv_dir)
    xml_df.to_csv(os.path.join(csv_dir, '{}.csv'.format(csv_name)), index=False)
    print('Successfully converted xml to csv.')


if __name__ == '__main__':
    # raw bit data
    # main(r'D:\Code\Python\data\BITVehicle_Dataset\train_test_split\train_val',
    #      r'D:\Code\Python\data\BITVehicle_Dataset\label_csv', 'train_val')
    # main(r'D:\Code\Python\data\BITVehicle_Dataset\train_test_split\test',
    #      r'D:\Code\Python\data\BITVehicle_Dataset\label_csv', 'test')

    # self-made data
    main(r'D:\Code\Python\data\toycar\train_test_split\train_val',
         r'D:\Code\Python\data\toycar\csv', 'train_val')
    main(r'D:\Code\Python\data\toycar\train_test_split\test',
         r'D:\Code\Python\data\toycar\csv', 'test')

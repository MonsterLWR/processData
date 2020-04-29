import pandas as pd
import os
import numpy as np

# def split_train_test(label):
#     train = label.sample(frac=0.85)
#     test = label[~label.index.isin(train.index)]
dir = r'D:\Code\Python\data\BITVehicle_Dataset\all_label_csv'


def split_single_class(train, max_num_samples=500):
    cls_set = set(train['class'])
    for cls in cls_set:
        cls_data = train[train['class'] == cls]
        num_samples = len(cls_data) if len(cls_data) < max_num_samples else max_num_samples
        samples = train[train['class'] == cls].sample(num_samples)
        samples.to_csv(os.path.join(dir, 'train{}_{}.csv'.format(max_num_samples, cls)))


if __name__ == '__main__':
    csv_dir = r'D:\Code\Python\data\BITVehicle_Dataset\label_csv'
    train_val = pd.read_csv(os.path.join(csv_dir, 'train_val.csv'))
    test = pd.read_csv(os.path.join(csv_dir, 'test.csv'))

    fine_grained_tarin_path = r'D:\Code\Python\data\BITVehicle_Dataset\label_csv\fine_grained_train'
    class_set = set(train_val['class'])

    for cls in class_set:
        # one image may have several labels, so this code sample from the file rather than the label
        cls_label = train_val[train_val['class'] == cls]
        no_cls_label = train_val[train_val['class'] != cls]

        cls_file = list(set(cls_label['filename']))
        no_cls_file = list(set(train_val[~train_val['filename'].isin(cls_file)]['filename']))

        print(cls)
        print(len(cls_file))
        print(len(no_cls_file))

        np.random.shuffle(cls_file)
        cls_file_50 = cls_file[:50]
        np.random.shuffle(no_cls_file)
        no_cls_file_500 = no_cls_file[:500]

        cls_label_50 = train_val[train_val['filename'].isin(cls_file_50)]
        no_cls_label_500 = train_val[train_val['filename'].isin(no_cls_file_500)]

        cls_label.to_csv(os.path.join(fine_grained_tarin_path, '{}_{}.csv'.format(cls, 'cls_label')), index=False)
        cls_label_50.to_csv(os.path.join(fine_grained_tarin_path, '{}_{}.csv'.format(cls, 'cls_label_50')), index=False)
        no_cls_label.to_csv(os.path.join(fine_grained_tarin_path, '{}_{}.csv'.format(cls, 'no_cls_label')), index=False)
        no_cls_label_500.to_csv(os.path.join(fine_grained_tarin_path, '{}_{}.csv'.format(cls, 'no_cls_label_500')), index=False)

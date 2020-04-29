import pandas as pd
import numpy as np
import os

base_path = r'D:\Code\Python\data\BITVehicle_Dataset\train_test\csv_dir'


def remove_suv():
    val_table = pd.read_csv(os.path.join(base_path, 'validation_labels.csv'))
    train_table = pd.read_csv(os.path.join(base_path, 'train_labels.csv'))
    table = pd.concat([train_table, val_table])

    table_without_suv = table[table['class'] != 'suv']
    table_with_suv = table[table['class'] == 'suv']

    table_with_suv.to_csv(os.path.join(base_path, 'test_suv.csv'), index=None)
    table_without_suv.to_csv(os.path.join(base_path, 'test_without_suv.csv'), index=None)


def sample_data():
    train_without_suv = pd.read_csv(os.path.join(base_path, 'train_without_suv.csv'))

    classes = train_without_suv['class'].unique()
    sampled_train = []

    for cls in classes:
        train_one_class = train_without_suv[train_without_suv['class'] == cls]
        sampled_train.append(train_one_class.sample(200))

    sampled_train = pd.concat(sampled_train)

    # index = np.random.permutation(500)
    # sampled_train.take(index)

    train_suv = pd.read_csv(os.path.join(base_path, 'train_suv.csv'))
    samples_suv = train_suv.sample(50)

    sampled_bit = pd.concat([sampled_train, samples_suv], ignore_index=True)
    index = np.random.permutation(1050)
    sampled_bit = sampled_bit.take(index)

    sampled_bit.to_csv(os.path.join(base_path, 'sampled_bit.csv'), index=None)


if __name__ == '__main__':
    sample_data()

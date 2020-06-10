"""
Usage:
  # From tensorflow/models/
  # Create train data:
  python generate_tfrecord.py --csv_input=data/train_labels.csv  --output_path=train.record

  # Create test data:
  python generate_tfrecord.py --csv_input=data/test_labels.csv  --output_path=test.record
"""
from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import os
import io

import contextlib2
import pandas as pd
import tensorflow as tf

from PIL import Image
from object_detection.dataset_tools import tf_record_creation_util
from object_detection.utils import dataset_util
from collections import namedtuple, OrderedDict


# flags = tf.app.flags
# flags.DEFINE_string('csv_input', '', 'Path to the CSV input')
# flags.DEFINE_string('image_dir', '', 'Path to the image directory')
# flags.DEFINE_string('output_path', '', 'Path to output TFRecord')
# FLAGS = flags.FLAGS


# TO-DO replace this with label map
def class_text_to_int(row_label):
    if row_label == 'minivan':
        return 1
    elif row_label == 'microbus':
        return 2
    elif row_label == 'sedan':
        return 3
    elif row_label == 'bus':
        return 4
    elif row_label == 'truck':
        return 5
    elif row_label == 'suv':
        return 6
    # toycar
    elif row_label == 'toycar':
        return 7
    else:
        return None


def split(df, group):
    data = namedtuple('data', ['filename', 'object'])
    gb = df.groupby(group)
    return [data(filename, gb.get_group(x)) for filename, x in zip(gb.groups.keys(), gb.groups)]


def create_tf_example(group, path):
    with tf.gfile.GFile(os.path.join(path, '{}'.format(group.filename)), 'rb') as fid:
        encoded_jpg = fid.read()
    encoded_jpg_io = io.BytesIO(encoded_jpg)
    image = Image.open(encoded_jpg_io)
    width, height = image.size

    filename = group.filename.encode('utf8')
    image_format = b'jpg'
    xmins = []
    xmaxs = []
    ymins = []
    ymaxs = []
    classes_text = []
    classes = []

    for index, row in group.object.iterrows():
        xmins.append(row['xmin'] / width)
        xmaxs.append(row['xmax'] / width)
        ymins.append(row['ymin'] / height)
        ymaxs.append(row['ymax'] / height)
        classes_text.append(row['class'].encode('utf8'))
        classes.append(class_text_to_int(row['class']))

    tf_example = tf.train.Example(features=tf.train.Features(feature={
        'image/height': dataset_util.int64_feature(height),
        'image/width': dataset_util.int64_feature(width),
        'image/filename': dataset_util.bytes_feature(filename),
        'image/source_id': dataset_util.bytes_feature(filename),
        'image/encoded': dataset_util.bytes_feature(encoded_jpg),
        'image/format': dataset_util.bytes_feature(image_format),
        'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
        'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
        'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
        'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
        'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
        'image/object/class/label': dataset_util.int64_list_feature(classes),
    }))
    return tf_example


def main(image_dir, csv_input, output_path, num_shards=1):
    # writer = tf.python_io.TFRecordWriter(output_path)
    path = image_dir
    examples = pd.read_csv(csv_input)
    grouped = split(examples, 'filename')
    num = 0
    # for group in grouped:
    #     num += 1
    #     tf_example = create_tf_example(group, path)
    #     writer.write(tf_example.SerializeToString())
    #     if num % 100 == 0:  # 每完成100个转换，打印一次
    #         print(num)

    # num_shards = 10
    # output_filebase = os.path.join(output_path,'record')

    with contextlib2.ExitStack() as tf_record_close_stack:
        output_tfrecords = tf_record_creation_util.open_sharded_output_tfrecords(
            tf_record_close_stack, output_path, num_shards)
        for index, group in enumerate(grouped):
            num += 1
            tf_example = create_tf_example(group, path)
            output_shard_index = index % num_shards
            output_tfrecords[output_shard_index].write(tf_example.SerializeToString())
            if num % 100 == 0:  # 每完成100个转换，打印一次
                print(num)

    # writer.close()
    # output_path = os.path.join(os.getcwd(), FLAGS.output_path)
    print('Successfully created the TFRecords: {}'.format(output_path))


if __name__ == '__main__':
    # # used for bit
    # image_dir = r'D:\Code\Python\data\BITVehicle_Dataset\imgs'
    #
    # csv_dir = r'D:\Code\Python\data\BITVehicle_Dataset\label_csv'
    # tf_record_dir = r'D:\Code\Python\data\BITVehicle_Dataset\tf_record'
    # #
    # # # cls_set = ['suv', 'truck', 'bus', 'sedan', 'microbus', 'minivan']
    # #
    # # file_names = ['train_val.csv', 'test.csv']
    # file_names = ['train_val_500.csv']
    #
    # for file in file_names:
    #     print('processing', file)
    #     csv_input = os.path.join(csv_dir, file)
    #     output_path = os.path.join(tf_record_dir, '{}.record'.format(file.split('.')[0]))
    #     num_shards = 1
    #     main(image_dir, csv_input, output_path, num_shards)

    # fine_grained_csv_dir = r'D:\Code\Python\data\BITVehicle_Dataset\label_csv\fine_grained_train'
    # file_names = os.listdir(fine_grained_csv_dir)
    # for file in file_names:
    #     print('processing', file)
    #     csv_input = os.path.join(fine_grained_csv_dir, file)
    #     output_path = os.path.join(tf_record_dir, '{}.record'.format(file.split('.')[0]))
    #     num_shards = 5 if 'no_cls_label' in file and '500' not in file else 1
    #     main(image_dir, csv_input, output_path, num_shards)

    # self-made data
    base_dir = r'D:\Code\Python\data\toycar'
    image_dir = os.path.join(base_dir, 'image')

    csv_dir = os.path.join(base_dir, 'csv')
    tf_record_dir = os.path.join(base_dir, 'tf_record')

    if not os.path.exists(tf_record_dir):
        os.mkdir(tf_record_dir)

    for file in os.listdir(csv_dir):
        print('processing', file)
        csv_input = os.path.join(csv_dir, file)
        output_path = os.path.join(tf_record_dir, '{}.record'.format(file.split('.')[0]))
        num_shards = 1
        main(image_dir, csv_input, output_path, num_shards)

from PIL import Image
import glob
import os
import cv2

if __name__ == '__main__':
    image_dir = r'D:\Code\Python\data\toycar\image'
    target_dir = r'D:\Code\Python\data\toycar\image'

    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    imgs = glob.glob(os.path.join(image_dir, '*.jpg'))
    for img_file in imgs:
        img = cv2.imread(img_file)
        height, width = img.shape[:2]

        if not (height > 3000 or width > 3000):
            continue

        down_sampled_img = cv2.resize(img, (width // 4, height // 4))

        print(down_sampled_img.shape)

        print(os.path.basename(img_file))
        cv2.imwrite(os.path.join(target_dir, os.path.basename(img_file)), down_sampled_img)
        # cv2.imshow('test', down_sampled_img)
        # cv2.waitKey()


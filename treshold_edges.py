# write me python scrip that will take all files in directory, and filter only images from them. On each image it will use numpy to threshold grayscale image. Pixels that has value below 40 set to 0, and pixels that has value above 40 set to 255. The directory path is passed as a cli argument to this python script.


import os
import cv2
import numpy as np
import argparse

def threshold_images_in_directory(directory_path):
    for filename in os.listdir(directory_path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(directory_path, filename)
            img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            ret, thresh = cv2.threshold(img, 40, 255, cv2.THRESH_BINARY)
            cv2.imwrite(image_path, thresh)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Threshold images in a directory')
    parser.add_argument('directory', type=str, help='Path to directory containing images')
    args = parser.parse_args()
    threshold_images_in_directory(args.directory)
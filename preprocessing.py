import os
from PIL import Image
import numpy as np
from tqdm import tqdm

import util

def remove_empty_images(root_path, dataset_name):
    if util.check_augmented_dataset_exist(root_path):
        root_path = root_path + '/' + dataset_name
        os.chdir(root_path)

        path_to_images = os.getcwd() + '/images'
        path_to_masks = os.getcwd() + '/masks'

        os.chdir(path_to_masks)
        masks = os.listdir()

        for mask_name in tqdm(masks, desc='Removing...'):
            mask = Image.open(mask_name)

            mask_arr = np.array(mask)

            if not np.any(mask_arr != 255):
                os.remove(path_to_masks + '/' + mask_name)
                os.remove(path_to_images + '/' + mask_name.replace('mask','original'))

root_path = os.getcwd()

remove_empty_images(root_path, 'Augmented Dataset')
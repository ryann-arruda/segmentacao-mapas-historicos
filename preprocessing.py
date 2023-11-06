import os
from PIL import Image
import numpy as np
from tqdm import tqdm
from random import shuffle
import shutil

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

def create_folder_from_dataset(root_path, dataset_path, folder_name, image_names):
    if os.path.exists(root_path + '/' + folder_name):
        shutil.rmtree(root_path + '/' + folder_name)
    
    folder_path = root_path +  '/' + folder_name

    print(f"Creating {folder_name}...")
    os.mkdir(folder_path)
    os.mkdir(folder_path + '/images')
    os.mkdir(folder_path + '/masks')

    for image_name in tqdm(image_names, desc=f'Populating the {folder_name} folder...'):
        shutil.move(dataset_path + '/images/' + image_name, folder_path + '/images/')
        shutil.move(dataset_path + '/masks/' + image_name.replace('original', 'mask'), folder_path + '/masks/')

def train_test_val(root_path, dataset_name='Augmented Dataset', train=0.7, test=0.2):
    dataset_path = root_path + '/' + dataset_name

    if util.check_augmented_dataset_exist(root_path):
        image_names = os.listdir(dataset_path + '/images')

        dataset_size = len(image_names)
        train_size = int(round(dataset_size * train, 0))
        test_size = int(round(dataset_size * test, 0))

        shuffle(image_names)

        name_training_images = image_names[:train_size]
        image_names = image_names[train_size:]
        create_folder_from_dataset(root_path, dataset_path, 'training', name_training_images)

        name_testing_images = image_names[:test_size]
        image_names = image_names[test_size:]
        create_folder_from_dataset(root_path, dataset_path, 'testing', name_testing_images)


        create_folder_from_dataset(root_path, dataset_path, 'validation', image_names)

        shutil.rmtree(dataset_path)
        

root_path = os.getcwd()

remove_empty_images(root_path, 'Augmented Dataset')
train_test_val(root_path)
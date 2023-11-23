import os
from PIL import Image
import shutil

def check_dataset_exist(root_path):
    if not os.path.exists(root_path + '/Dataset'):
        raise FileNotFoundError(f"The path to the dataset doesn't exist! Path used: {root_path + '/Dataset'}")
    
    if not os.path.exists(root_path + '/Dataset/images'):
        raise FileNotFoundError(f"The path to the dataset doesn't exist! Path used: {root_path + '/Dataset/images'}")

    if not os.path.exists(root_path + '/Dataset/masks'):
        raise FileNotFoundError(f"The path to the dataset doesn't exist! Path used: {root_path + '/Dataset/masks'}")
    
    if not os.listdir(root_path + '/Dataset/images'):
        raise FileNotFoundError(f"Images not found! Path used: {root_path + '/Dataset/images'}")
    
    if not os.listdir(root_path + '/Dataset/masks'):
        raise FileNotFoundError(f"Masks not found! Path used: {root_path + '/Dataset/masks'}")

    return True

def check_augmented_dataset_exist(root_path):
    if not os.path.exists(root_path + '/Augmented Dataset'):
        raise FileNotFoundError(f"The path to the dataset doesn't exist! Path used: {root_path + '/Augmented Dataset'}")

    if not os.path.exists(root_path + '/Augmented Dataset/images'):
        raise FileNotFoundError(f"The path to the dataset doesn't exist! Path used: {root_path + '/Augmented Dataset/images'}")

    if not os.path.exists(root_path + '/Augmented Dataset/masks'):
        raise FileNotFoundError(f"The path to the dataset doesn't exist! Path used: {root_path + '/Augmented Dataset/masks'}")

    if not os.listdir(root_path + '/Augmented Dataset/images'):
        raise FileNotFoundError(f"Images not found! Path used: {root_path + '/Augmented Dataset/images'}")

    if not os.listdir(root_path + '/Augmented Dataset/masks'):
        raise FileNotFoundError(f"Masks not found! Path used: {root_path + '/Augmented Dataset/masks'}")

    return True

def remove_unnecessary_border(image):
    img = image.convert('RGBA')

    aux_image = Image.new('RGBA', img.size, (255,)*4)

    borderless_image = Image.composite(img, aux_image, img)

    return borderless_image.convert('RGB')

def check_save_path(root_path):

    if os.path.exists(root_path + '/Augmented Dataset'):
        shutil.rmtree(root_path + '/Augmented Dataset')

    path = root_path + '/Augmented Dataset'
    os.mkdir(path)
    os.mkdir(path + '/images')
    os.mkdir(path + '/masks')
    
    return True
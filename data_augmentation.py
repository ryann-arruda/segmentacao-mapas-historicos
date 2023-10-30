import os
from PIL import Image, ImageEnhance
from tqdm import tqdm

import util

def crop_save_image(image, image_name, path_to_save, cut_size):
    index = 0
    for i in tqdm(range(0, image.height, cut_size), desc=f'Cropping [image: {image_name}]'):
        for j in range(0, image.width, cut_size):
            image_name_aux = image_name.replace('.png', str(index) + '.png')
            index += 1
            
            cropped_image = image.crop((j, i, j + cut_size, i + cut_size))
            
            cropped_borderless_image = util.remove_unnecessary_border(cropped_image)
            cropped_borderless_image.save(path_to_save + image_name_aux)

def resize(image, size):
    return image.resize((size, size))

def rotate(image, angle):
    return image.rotate(angle, expand=True)

def flipHorizontal(image):
    return image.transpose(method=Image.Transpose.FLIP_LEFT_RIGHT)

def brightness(image, factor):
    brightener = ImageEnhance.Brightness(image)

    if  1 + factor < 0:
        factor = 0

    return brightener.enhance(1 + factor)

def contrast(image, factor):
    contraster = ImageEnhance.Contrast(image)

    if 1 + factor < 0:
        factor = 0

    return contraster.enhance(1 + factor)

def greyscale(image):
    return image.convert("L")


root_path = os.getcwd()

if util.check_dataset_exist(root_path):
    os.chdir(root_path + '/Dataset/images')
    images = os.listdir()

    if util.check_save_path(root_path):
        path_to_save_image = root_path + '/Augmented Dataset/images/'
        path_to_save_mask = root_path + '/Augmented Dataset/masks/'

        for image_name in tqdm(images, desc='Image cropping total completed...', leave=False):
            image = Image.open(image_name)

            mask_name = image_name.replace('original', 'mask')
            mask = Image.open(os.path.dirname(os.getcwd()) + '/masks/' + mask_name)

            crop_save_image(image, image_name, path_to_save_image, 256)
            crop_save_image(mask, mask_name, path_to_save_mask, 256)

        os.chdir(root_path + '/Augmented Dataset/images')
        images = os.listdir()

        for image_name in tqdm(images, desc='Total transformations...'):
            image = Image.open(image_name)

            mask_name = image_name.replace('original', 'mask')
            mask = Image.open(os.path.dirname(os.getcwd()) + '/masks/' + mask_name)

            image_rot = rotate(image, -45)
            image_rot = resize(image_rot, 256)
            borderless_rot_image = util.remove_unnecessary_border(image_rot)
            borderless_rot_image.save(path_to_save_image + image_name.replace('.png', 'r.png'))

            mask_rot = rotate(mask, -45)
            mask_rot = resize(mask_rot, 256)
            borderless_rot_mask = util.remove_unnecessary_border(mask_rot)
            borderless_rot_mask.save(path_to_save_mask + mask_name.replace('.png', 'r.png'))

            flipHorizontal(image).save(path_to_save_image + image_name.replace('.png', 'f.png'))
            flipHorizontal(mask).save(path_to_save_mask + mask_name.replace('.png', 'f.png'))

            brightness(image, 0.5).save(path_to_save_image + image_name.replace('.png', 'bi.png'))
            mask.copy().save(path_to_save_mask + mask_name.replace('.png', 'bi.png'))

            brightness(image, -0.5).save(path_to_save_image + image_name.replace('.png', 'bd.png'))
            mask.copy().save(path_to_save_mask + mask_name.replace('.png', 'bd.png'))

            contrast(image, 0.5).save(path_to_save_image + image_name.replace('.png', 'ci.png'))
            mask.copy().save(path_to_save_mask + mask_name.replace('.png', 'ci.png'))

            contrast(image, -0.5).save(path_to_save_image + image_name.replace('.png', 'cd.png'))
            mask.copy().save(path_to_save_mask + mask_name.replace('.png', 'cd.png'))

            greyscale(image).save(path_to_save_image + image_name.replace('.png', 'g.png'))
            mask.copy().save(path_to_save_mask + mask_name.replace('.png', 'g.png'))
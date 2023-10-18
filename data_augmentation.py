import os
from PIL import Image, ImageEnhance

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
os.chdir(root_path + '/Dataset/images')

images = os.listdir()

path_to_save_image = root_path + '/Augmented Dataset/images/'
path_to_save_mask = root_path + '/Augmented Dataset/masks/'

for i in images:
    image = Image.open(i)

    mask_name = i.replace('original', 'mask')
    mask = Image.open(os.path.dirname(os.getcwd()) + '/masks/' + mask_name)

    resize(image, 256).save(path_to_save_image + i.replace('.png', 'a.png'))
    resize(mask, 256).save(path_to_save_mask + mask_name.replace('.png', 'a.png'))


os.chdir(root_path + '/Augmented Dataset/images')

images = os.listdir()

for i in images:
    image = Image.open(i)

    mask_name = i.replace('originala', 'maska')
    mask = Image.open(os.path.dirname(os.getcwd()) + '/masks/' + mask_name)

    rotate(image, -45).save(path_to_save_image + i.replace('a.png', 'b.png'))
    rotate(mask, -45).save(path_to_save_mask + mask_name.replace('a.png', 'b.png'))

    flipHorizontal(image).save(path_to_save_image + i.replace('a.png', 'c.png'))
    flipHorizontal(mask).save(path_to_save_mask + mask_name.replace('a.png', 'c.png'))

    brightness(image, 0.5).save(path_to_save_image + i.replace('a.png', 'd.png'))
    mask.copy().save(path_to_save_mask + mask_name.replace('a.png', 'd.png'))

    brightness(image, -0.5).save(path_to_save_image + i.replace('a.png', 'e.png'))
    mask.copy().save(path_to_save_mask + mask_name.replace('a.png', 'e.png'))

    contrast(image, 0.5).save(path_to_save_image + i.replace('a.png', 'f.png'))
    mask.copy().save(path_to_save_mask + mask_name.replace('a.png', 'f.png'))

    contrast(image, -0.5).save(path_to_save_image + i.replace('a.png', 'g.png'))
    mask.copy().save(path_to_save_mask + mask_name.replace('a.png', 'g.png'))

    greyscale(image).save(path_to_save_image + i.replace('a.png', 'h.png'))
    mask.copy().save(path_to_save_mask + mask_name.replace('a.png', 'h.png'))
from os import listdir
from typing import List, Tuple
from PIL import Image
import numpy as np
from tqdm import tqdm

def get_images_names_in_folder(folder_path:str) -> List[str]:
  image_names: List[str] = []
  print('> Getting images in ' + folder_path)

  for file_name in tqdm(listdir(folder_path), "Getting...", ncols=100):
    image_names.append(file_name)

  return image_names

def get_images_ndarray_in_folder(folder_path:str) -> List[np.ndarray]:
    return np.asarray([np.asarray(Image.open(folder_path + image_name)) for image_name in get_images_names_in_folder(folder_path)])

def get_maps_augmented() -> List[Image.Image]:
  return get_images_ndarray_in_folder('Augmented Dataset/images/') 

def get_masks_augmented() -> List[Image.Image]:
    return get_images_ndarray_in_folder('Augmented Dataset/masks/')

# (Normalization) scale from [0,255] to [-1,1] 
def downscale_image_pixels(image:np.ndarray) -> np.ndarray:
  return (image - 127.5) / 127.5

# Image and mask normalization
def downscale_pair_image_pixels(pair_image:Tuple[np.ndarray, np.ndarray]) -> Tuple[np.ndarray, np.ndarray]:
  return (downscale_image_pixels(pair_image[0]), downscale_image_pixels(pair_image[1]))
import os

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
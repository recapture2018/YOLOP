import random
import shutil
import os

def split(path, mask_path, lane_path):
    os.mkdir(f'{path}train')
    os.mkdir(f'{path}val')
    os.mkdir(f'{mask_path}train')
    os.mkdir(f'{mask_path}val')
    os.mkdir(f'{lane_path}train')
    os.mkdir(f'{lane_path}val')
    val_index = random.sample(range(660), 200)
    for i in range(660):
        if i in val_index:
            shutil.move(f'{path}{i}.png', f'{path}val')
            shutil.move(f'{mask_path}{i}.png', f'{mask_path}val')
            shutil.move(f'{lane_path}{i}.png', f'{lane_path}val')
        else:
            shutil.move(f'{path}{i}.png', f'{path}train')
            shutil.move(f'{mask_path}{i}.png', f'{mask_path}train')
            shutil.move(f'{lane_path}{i}.png', f'{lane_path}train')


if __name__ == '__main__':
    path = "/home/wqm/bdd/data_hust/"
    mask_path = "/home/wqm/bdd/hust_area/"
    lane_path = "/home/wqm/bdd/hust_lane/"
    split(path, mask_path, lane_path)



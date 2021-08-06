import os
import cv2
from tqdm import tqdm
import numpy as np
from random import shuffle

folder = './Dataframes/'
NUM_FRAME = 10
IMG_SIZE = 100

def create_dataset(folder, output_name):
    dataset = []
    image = []
    limit = 0
    count = 0

    for folders in os.listdir(folder):
        print(folders)
        folder_path = os.path.join(folder, folders)
        for i in tqdm(os.listdir(folder_path)):
            path = os.path.join(folder_path, i)
            img = cv2.resize(cv2.imread(path), (IMG_SIZE, IMG_SIZE))
            image.append(np.array(img))
            limit += 1
            count += 1

            if limit == NUM_FRAME:
                limit = 0
                if i[0] == 'V' or i[0] == 'v' or i[0] == 'f':
                    dataset.append([image, np.array([1,0])])
                elif i[0] == 'N' or i[0] == 'n':
                    dataset.append([image, np.array([0,1])])
                image = []

    shuffle(dataset)
    np.save(output_name, dataset)

create_dataset(folder, 'data.npy')
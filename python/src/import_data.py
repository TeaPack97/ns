import glob
from os.path import basename
import numpy as np
from tqdm import tqdm
import random as ra
from cv2 import *

MUZ = 0
ZENA = 1
HEIGHT = 64
WIDTH = 64
DIM = (HEIGHT, WIDTH)


def prep_img(file):
    image = imread(file)
    image = resize(image, DIM)
    image = image / 255.0
    image = np.array(image)
    return image


def decide_age(age):
    age = int(age)
    if age < 5:
        return 0
    if age < 10:
        return 1
    if age < 18:
        return 2
    if age < 26:
        return 3
    if age < 40:
        return 4
    if age < 60:
        return 5
    if age < 75:
        return 6
    return 7


def decide_gender(number):
    number = int(number)
    if number < 7381:
        return ZENA
    return MUZ


def get_gender(file):
    if file[1] == '_':
        gender = int(file[2])
    elif file[2] == '_':
        gender = int(file[3])
    else:
        gender = int(file[4])
    return gender


def get_age(file):
    if file[1] == '_':
        age = int(file[0])
    elif file[2] == '_':
        age = int(file[0] + file[1])
    else:
        age = int(file[0] + file[1] + file[2])
    return decide_age(age=age)


def prepare_data(images, age_labels, gender_labels):
    train_images = []
    train_age_labels = []
    train_gender_labels = []
    test_images = []
    test_age_labels = []
    test_gender_labels = []

    pom = list(zip(images, age_labels, gender_labels))
    ra.shuffle(pom)
    images, age_labels, gender_labels = zip(*pom)

    for x in tqdm(range(len(images))):
        if x < int(len(images) * 4 / 5):
            train_images.append(images[x])
            train_age_labels.append(age_labels[x])
            train_gender_labels.append(gender_labels[x])
        else:
            test_images.append(images[x])
            test_age_labels.append(age_labels[x])
            test_gender_labels.append(gender_labels[x])

    train_images = np.array(train_images)
    train_age_labels = np.array(train_age_labels)
    train_gender_labels = np.array(train_gender_labels)
    test_images = np.array(test_images)
    test_age_labels = np.array(test_age_labels)
    test_gender_labels = np.array(test_gender_labels)

    return train_images, train_age_labels, train_gender_labels, test_images, test_age_labels, test_gender_labels


def process_dataset3():
    images = []
    age_labels = []
    gender_labels = []

    for file in tqdm(glob.glob("..\\photos\\dataset3\\*.jpg")):
        filename = basename(file)
        images.append(prep_img(file=file))
        age_labels.append(get_age(file=filename))
        gender_labels.append(get_gender(file=filename))

    return images, age_labels, gender_labels


def process_dataset2():
    images = []
    age_labels = []
    gender_labels = []

    for file in tqdm(glob.glob("..\\photos\\dataset2\\*.jpg")):
        filename = basename(file)
        images.append(prep_img(file=file))
        age_labels.append(get_age(file=filename))
        gender_labels.append(get_gender(file=filename))

    return images, age_labels, gender_labels


def process_dataset1():
    images = []
    age_labels = []
    gender_labels = []

    for file in tqdm(glob.glob("..\\photos\\dataset1\\*.jpg")):
        filename = basename(file)
        images.append(prep_img(file=file))
        age_labels.append(decide_age(age=filename[6:8]))
        gender_labels.append(decide_gender(number=filename[0:5]))

    return images, age_labels, gender_labels


def get_data():
    print("Preparing dataset...")
    images1, age_labels1, gender_labels1 = process_dataset1()
    images2, age_labels2, gender_labels2 = process_dataset2()
    images3, age_labels3, gender_labels3 = process_dataset3()

    images = np.concatenate((images1, images2, images3))
    age_labels = np.concatenate((age_labels1, age_labels2, age_labels3))
    gender_labels = np.concatenate((gender_labels1, gender_labels2, gender_labels3))

    print("Preparing train and test data...")
    return prepare_data(images, age_labels, gender_labels)

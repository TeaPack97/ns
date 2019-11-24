import glob
from os.path import basename
import numpy as np
import random as ra
from cv2 import *

HEIGHT = 85
WIDTH = 75
DIM = (HEIGHT, WIDTH)


def prep_img(image):
    image = resize(image, DIM)
    image = image / 255.0
    image = np.array(image)
    return image


def decide_age(age):
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


def prep_label(age, number):
    number = int(number)
    age = int(age)
    if number < 7381:
        return decide_age(age=age)
    return decide_age(age=age) + 8


def get_age_gender(name):
    name = basename(name)
    if name[1] == '_':
        age = int(name[0])
        gender = int(name[2])
    elif name[2] == '_':
        age = int(name[0] + name[1])
        gender = int(name[3])
    else:
        age = int(name[0] + name[1] + name[2])
        gender = int(name[4])
    if gender == 1:
        age = decide_age(age=age)
    else:
        age = decide_age(age=age) + 8
    return age


def get_photos(file, images, labels):
    f = open(file, "r")

    for x in f:
        img = imread("D:\\Nastavenia\\Dokumenty\\STU\\4rocnik\\neu\\ns\\python\\photos\\original_images\\" + x[0:12])
        images.append(prep_img(image=img))
        labels.append(prep_label(age=x[6:8], number=x[0:5]))
    f.close()
    return


def get_data():
    print("loading first dataset...")
    train_images1, train_labels1, test_images1, test_labels1 = get_data1()
    print("loading second dataset...")
    train_images2, train_labels2, test_images2, test_labels2 = get_data2()

    print("preparing dataset...")
    train_images = np.concatenate((train_images1, train_images2))
    train_labels = np.concatenate((train_labels1, train_labels2))
    test_images = np.concatenate((test_images1, test_images2))
    test_labels = np.concatenate((test_labels1, test_labels2))

    train_images = np.array(train_images)
    train_labels = np.array(train_labels)
    test_images = np.array(test_images)
    test_labels = np.array(test_labels)

    return train_images, train_labels, test_images, test_labels


def get_data1():
    train_labels = []
    train_images = []
    test_images = []
    test_labels = []

    get_photos(file="D:\\Nastavenia\\Dokumenty\\STU\\4rocnik\\neu\\ns\\python\\photos\\image_sets\\train.txt",
               images=train_images, labels=train_labels)
    get_photos(file="D:\\Nastavenia\\Dokumenty\\STU\\4rocnik\\neu\\ns\\python\\photos\\image_sets\\val.txt",
               images=test_images, labels=test_labels)

    train_images = np.array(train_images)
    train_labels = np.array(train_labels)
    test_images = np.array(test_images)
    test_labels = np.array(test_labels)

    return train_images, train_labels, test_images, test_labels


def get_data2():
    train_labels = []
    train_images = []
    test_images = []
    test_labels = []

    # DIMENSION (200,200,3)
    images = [prep_img(imread(file)) for file in glob.glob("..\\photos\\mixed\\UTKFace\\*.jpg")]
    labels = [get_age_gender(file) for file in glob.glob("..\\photos\\mixed\\UTKFace\\*.jpg")]

    pom = list(zip(images, labels))
    ra.shuffle(pom)
    images, labels = zip(*pom)

    for x in range(0, int(len(images) * 3 / 4)):
        train_images.append(images[x])
        train_labels.append(labels[x])
    for x in range(int(len(images) * 3 / 4), len(images)):
        test_images.append(images[x])
        test_labels.append(labels[x])

    train_images = np.array(train_images)
    train_labels = np.array(train_labels)
    test_images = np.array(test_images)
    test_labels = np.array(test_labels)

    return train_images, train_labels, test_images, test_labels

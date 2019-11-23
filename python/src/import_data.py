import numpy as np
from cv2 import *

HEIGHT = 85
WIDTH = 75
DIM = (HEIGHT, WIDTH)


def prep_img(image):
    image = cvtColor(image, COLOR_BGR2RGB)
    image = resize(image, DIM)
    image = np.array(image)
    return image


def prep_label(number):
    number = int(number)
    if number < 3:
        return 0
    if number < 7:
        return 1
    if number < 13:
        return 2
    if number < 21:
        return 3
    if number < 33:
        return 4
    if number < 44:
        return 5
    if number < 55:
        return 6
    return 7


def get_data():
    train_labels = []
    train_images = []
    test_images = []
    test_labels = []
    print("loading training images...")
    f = open("D:\\Nastavenia\\Dokumenty\\STU\\4rocnik\\neu\\ns\\python\\photos\\image_sets\\train.txt", "r")

    for x in f:
        img = imread("D:\\Nastavenia\\Dokumenty\\STU\\4rocnik\\neu\\ns\\python\\photos\\original_images\\" + x[0:12])
        train_images.append(prep_img(image=img))
        train_labels.append(prep_label(number=x[6:8]))
    f.close()

    print("loading testing images...")
    f = open("D:\\Nastavenia\\Dokumenty\\STU\\4rocnik\\neu\\ns\\python\\photos\\image_sets\\val.txt", "r")

    for x in f:
        img = imread("D:\\Nastavenia\\Dokumenty\\STU\\4rocnik\\neu\\ns\\python\\photos\\original_images\\" + x[0:12])
        test_images.append(prep_img(image=img))
        test_labels.append(prep_label(number=x[6:8]))
    f.close()

    train_images = np.array(train_images)
    train_labels = np.array(train_labels)
    test_images = np.array(test_images)
    test_labels = np.array(test_labels)
    return train_images, train_labels, test_images, test_labels





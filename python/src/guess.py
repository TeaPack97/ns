from src.import_data import *
from keras.models import load_model

FILE = "D:\\Nastavenia\\Dokumenty\\STU\\4rocnik\\neu\\ns\\21_0_1594562.jpg"


def max_idx(array):
    idx = 0
    for x in range(len(array)):
        if array[idx] < array[x]:
            idx = x
    return idx


def guess(file):
    img = [prep_img(imread(file)), prep_img(imread(file))]
    img = np.array(img)

    model = load_model("model.h5", compile=True)
    score = model.predict(img, verbose=0)

    print("REALNA HODNOTA: ", get_age_gender(file))
    print("PREDICT: ", max_idx(array=score[0]))


guess(file=FILE)

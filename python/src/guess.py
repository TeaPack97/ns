from src.import_data import *
from keras.models import load_model

FILE = "D:\\Nastavenia\\Dokumenty\\STU\\4rocnik\\neu\\ns\\21_0_1594562.jpg"

img = prep_img(imread(FILE))
label = get_age_gender(FILE)

model = load_model("model.h5", compile=True)
score = model.evaluate(img, label, verbose=1)
print("%s: %.2f%%" % (model.metrics_names[1], score[1]*100))

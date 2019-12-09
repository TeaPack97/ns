from src.import_data import *
from keras.models import load_model
from keras.utils import plot_model

plot_model(load_model("model.h5", compile=True), to_file='model.png', show_layer_names=True, show_shapes=True)


def guess():
    images = []
    age_labels = []
    gender_labels = []

    for file in tqdm(glob.glob("../photos/guess/*.jpg")):
        filename = basename(file)
        images.append(prep_img(file=file))
        age_labels.append(get_age(file=filename))
        gender_labels.append(get_gender(file=filename))

    images = np.array(images)
    age_labels = np.array(age_labels)
    gender_labels = np.array(gender_labels)

    model = load_model("model.h5", compile=True)
    predict = model.predict(images)

    for x in range(len(images)):
        print("FOTKA C: ", x)
        print("Age: ", age_labels[x], " Gender: ", gender_labels[x])
        print("Predicted Age: ", np.argmax(predict[0][x]), " Gender: ", np.argmax(predict[1][x]))


guess()

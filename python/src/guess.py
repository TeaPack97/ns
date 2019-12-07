from src.import_data import *
from keras.models import load_model


def guess():
    images = []
    age_labels = []
    gender_labels = []

    for file in tqdm(glob.glob("..\\photos\\guess\\*.jpg")):
        filename = basename(file)
        images.append(prep_img(file=file))
        age_labels.append(get_age(file=filename))
        gender_labels.append(get_gender(file=filename))

    images = np.array(images)
    age_labels = np.array(age_labels)
    gender_labels = np.array(gender_labels)

    model = load_model("model.h5", compile=True)
    metrics = model.metrics_names
    score = model.evaluate(images, {"age": age_labels, "gender": gender_labels})
    s = model.predict(images)

    print(metrics)
    print(score)
    print(s)

    for m in range(len(metrics)):
        print(metrics[m], ": %1.2f " % score[m])


guess()

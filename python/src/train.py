from keras.callbacks import TensorBoard, EarlyStopping
from datetime import datetime
from src.model import create_model
from keras.optimizers import Adam
from src.import_data import *
import matplotlib.pyplot as plt

BATCH_SIZE = 64
EPOCHS = 30

train_images, train_age_labels, train_gender_labels, test_images, test_age_labels, test_gender_labels = get_data()

model = create_model(HEIGHT, WIDTH, 8)

model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss={"age": "sparse_categorical_crossentropy", "gender": "binary_crossentropy"},
    metrics={"age": "accuracy", "gender": "accuracy"}
)

callbacks = [
    EarlyStopping(monitor='val_loss', mode="min", verbose=1, patience=5),
    TensorBoard(
        log_dir=os.path.join("..\\logs\\", str(datetime.now().strftime("%b_%d_%Y_%H_%M_%S"))),
        histogram_freq=1,
        profile_batch=0)
]

history = model.fit(
    x=train_images,
    y={"age": train_age_labels, "gender": train_gender_labels},
    batch_size=BATCH_SIZE,
    shuffle=True,
    validation_data=(test_images, {"age": test_age_labels, "gender": test_gender_labels}),
    callbacks=callbacks,
    epochs=EPOCHS
)

model.save("model.h5")
model.summary()
plt.plot(history.history['age_accuracy'])
plt.plot(history.history['val_age_accuracy'])
plt.title('Model Age Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()
plt.savefig('model_age_accuracy.png')
plt.clf()

plt.plot(history.history['gender_accuracy'])
plt.plot(history.history['val_gender_accuracy'])
plt.title('Model Gender Accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()
plt.savefig('model_gender_accuracy.png')
plt.clf()

plt.plot(history.history['age_loss'])
plt.plot(history.history['val_age_loss'])
plt.title('Model Age Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()
plt.savefig('model_age_loss.png')
plt.clf()

plt.plot(history.history['gender_loss'])
plt.plot(history.history['val_gender_loss'])
plt.title('Model Gender Loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()
plt.savefig('model_gender_loss.png')
plt.clf()

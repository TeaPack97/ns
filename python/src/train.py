from src.model import MyNeuralNetwork
from keras.optimizers import Adam
from src.import_data import *
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

BATCH_SIZE = 64
EPOCHS = 1

train_images, train_labels, test_images, test_labels = get_data()

model = MyNeuralNetwork(HEIGHT, WIDTH)

model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'])

callbacks = []

model.fit(
    x=train_images,
    y=train_labels,
    batch_size=BATCH_SIZE,
    shuffle=True,
    validation_data=(test_images, test_labels),
    callbacks=callbacks,
    epochs=EPOCHS)

model.summary()

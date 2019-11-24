from src.model import MyNeuralNetwork
from keras.optimizers import Adam
from src.import_data import *

BATCH_SIZE = 16
EPOCHS = 30

train_images, train_labels, test_images, test_labels = get_data()

model = MyNeuralNetwork(HEIGHT, WIDTH)

model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'])

callbacks = [
    # TensorBoard(
    #     log_dir="logs/" + timestamp(),
    #     histogram_freq=1,
    #     profile_batch=0)
]

model.fit(
    x=train_images,
    y=train_labels,
    batch_size=BATCH_SIZE,
    shuffle=True,
    validation_data=(test_images, test_labels),
    callbacks=callbacks,
    epochs=EPOCHS)

model.save("model.h5")
model.summary()

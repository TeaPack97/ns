from keras.models import Sequential
from keras.layers import Conv2D, Dense, MaxPooling2D, Flatten


class MyNeuralNetwork(Sequential):
    def __init__(self, height, width):
        super(MyNeuralNetwork, self).__init__(name='neural_network')
        self.add(
            Conv2D(
                input_shape=(width, height, 3),
                filters=16,
                kernel_size=3,
                padding='valid',
                activation='relu')
        )
        self.add(
            MaxPooling2D(pool_size=(2, 2))
        )
        self.add(
            Conv2D(
                filters=16,
                kernel_size=3,
                padding='valid',
                activation='relu')
        )
        self.add(
            MaxPooling2D(pool_size=(2, 2))
        )
        self.add(
            Conv2D(
                filters=16,
                kernel_size=3,
                padding='valid',
                activation='relu')
        )
        self.add(
            MaxPooling2D(pool_size=(2, 2))
        )
        self.add(
            Flatten()
        )
        self.add(
            Dense(
                units=512,
                activation='relu')
        )
        self.add(
            Dense(
                units=8,
                activation='softmax')
        )

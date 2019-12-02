from keras.models import Model
from keras.layers import Conv2D, Dense, MaxPooling2D, Flatten, Input, Dropout, BatchNormalization


def create_model(height, width, pocet_vekovych_kategorii):
    input_layer = Input(shape=(width, height, 3))

    con1 = Conv2D(filters=96, kernel_size=7, padding='same', activation='relu')(input_layer)
    con11 = Conv2D(filters=96, kernel_size=7, padding='same', activation='relu')(con1)
    max1 = MaxPooling2D(pool_size=(2, 2))(con11)
    batch1 = BatchNormalization()(max1)

    con2 = Conv2D(filters=256, kernel_size=5, padding='same', activation='relu')(batch1)
    con22 = Conv2D(filters=256, kernel_size=5, padding='same', activation='relu')(con2)
    max2 = MaxPooling2D(pool_size=(2, 2))(con22)
    batch2 = BatchNormalization()(max2)

    con3 = Conv2D(filters=384, kernel_size=3, padding='same', activation='relu')(batch2)
    con33 = Conv2D(filters=384, kernel_size=3, padding='same', activation='relu')(con3)
    max3 = MaxPooling2D(pool_size=(2, 2))(con33)
    batch3 = BatchNormalization()(max3)

    flat = Flatten()(batch3)

    dense1 = Dense(units=512, activation='relu')(flat)
    dense2 = Dense(units=512, activation='relu')(dense1)

    y = Dropout(rate=0.5)(dense2)

    age = Dense(units=pocet_vekovych_kategorii, activation='softmax', name="age")(y)
    gender = Dense(units=2, activation='softmax', name="gender")(y)

    model = Model(inputs=input_layer, outputs=[age, gender])

    return model


class MyNeuralNetwork:
    def __init__(self):
        super(MyNeuralNetwork, self).__init__(name='MyNeuralNetwork')


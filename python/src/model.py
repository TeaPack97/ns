from keras.models import Model
from keras.layers import Conv2D, Dense, MaxPooling2D, Flatten, Input, Dropout, BatchNormalization
from keras.regularizers import l2

def create_model(height, width, pocet_vekovych_kategorii):
    input_layer = Input(shape=(width, height, 3))

    con1 = Conv2D(filters=32, kernel_size=3, padding='same', activation='relu')(input_layer)
    con11 = Conv2D(filters=32, kernel_size=3, padding='same', activation='relu')(con1)
    batch1 = BatchNormalization()(con11)
    max1 = MaxPooling2D(pool_size=(2, 2))(batch1)

    con2 = Conv2D(filters=64, kernel_size=3, padding='same', activation='relu')(max1)
    con22 = Conv2D(filters=64, kernel_size=3, padding='same', activation='relu')(con2)
    batch2 = BatchNormalization()(con22)
    max2 = MaxPooling2D(pool_size=(2, 2))(batch2)

    con3 = Conv2D(filters=128, kernel_size=3, padding='same', activation='relu')(max2)
    con33 = Conv2D(filters=128, kernel_size=3, padding='same', activation='relu')(con3)
    batch3 = BatchNormalization()(con33)
    max3 = MaxPooling2D(pool_size=(2, 2))(batch3)

    con4 = Conv2D(filters=256, kernel_size=3, padding='same', activation='relu')(max3)
    con44 = Conv2D(filters=256, kernel_size=3, padding='same', activation='relu')(con4)
    batch4 = BatchNormalization()(con44)
    max4 = MaxPooling2D(pool_size=(2, 2))(batch4)

    flat = Flatten()(max4)

    # age
    age_dense1 = Dense(units=256, kernel_regularizer=l2(l=0.005), activation='relu')(flat)
    age_drop1 = Dropout(rate=0.5)(age_dense1)
    age_dense2 = Dense(units=256, kernel_regularizer=l2(l=0.005), activation='relu')(age_drop1)
    age_drop2 = Dropout(rate=0.5)(age_dense2)
    age = Dense(units=pocet_vekovych_kategorii, activation='softmax', name="age")(age_drop2)

    # gender
    gender_dense1 = Dense(units=256, kernel_regularizer=l2(0.025), activation='relu')(flat)
    gender_drop1 = Dropout(rate=0.5)(gender_dense1)
    gender_dense2 = Dense(units=256, kernel_regularizer=l2(0.025), activation='relu')(gender_drop1)
    gender_drop2 = Dropout(rate=0.5)(gender_dense2)
    gender = Dense(units=1, activation='sigmoid', name="gender")(gender_drop2)

    model = Model(inputs=input_layer, outputs=[age, gender])

    return model


class MyNeuralNetwork:
    def __init__(self):
        super(MyNeuralNetwork, self).__init__(name='MyNeuralNetwork')

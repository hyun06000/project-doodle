import os
import pickle
from datetime import datetime

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from tensorflow.keras import utils
from tensorflow.keras.callbacks import TensorBoard
from tensorflow.keras.layers import (Conv2D, Dense, Dropout, Flatten,
                                     MaxPooling2D)
from tensorflow.keras.models import Sequential


def loadFromPickle(feature_data_path):
    with open(f"{feature_data_path}/features", "rb") as f:
        features = np.array(pickle.load(f))
    with open(f"{feature_data_path}/labels", "rb") as f:
        labels = np.array(pickle.load(f))

    return features, labels


def postprocess_labels(labels):
    labels = utils.to_categorical(labels)
    return labels


def keras_model(x_shape, y_shape):
    num_of_classes = 15
    model = Sequential()
    model.add(Conv2D(32, (5, 5), input_shape=(x_shape, y_shape, 1), activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding="same"))
    model.add(Conv2D(64, (5, 5), activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2), padding="same"))

    model.add(Flatten())
    model.add(Dense(512, activation="relu"))
    model.add(Dropout(0.6))
    model.add(Dense(128, activation="relu"))
    model.add(Dropout(0.6))
    model.add(Dense(num_of_classes, activation="softmax"))

    model.compile(
        loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"]
    )

    return model


if __name__ == "__main__":
    feature_data_path = "../../data/feature"
    features, labels = loadFromPickle(feature_data_path)
    features, labels = shuffle(features, labels)
    labels = postprocess_labels(labels)

    train_X, test_X, train_y, test_y = train_test_split(
        features, labels, random_state=0, test_size=0.1
    )
    train_X = train_X.reshape(train_X.shape[0], 28, 28, 1)
    test_X = test_X.reshape(test_X.shape[0], 28, 28, 1)

    model = keras_model(28, 28)
    model.summary()

    logdir = "logs/" + datetime.now().strftime("%Y%m%d-%H%M%S")
    model.fit(
        train_X,
        train_y,
        validation_data=(test_X, test_y),
        epochs=3,
        batch_size=64,
        callbacks=[TensorBoard(log_dir=logdir)],
    )

    model_path = "../../model"
    if not os.path.exists(model_path):
        os.makedirs(model_path)
    model.save(f"{model_path}/CNN.h5")

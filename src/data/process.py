import os
import pickle

import numpy as np


def load_data(data_path):
    files = sorted(os.listdir(data_path))
    X_data, y_data = [], []
    count = 0
    for file in files:
        file = data_path + file
        X = np.load(file, encoding="latin1", allow_pickle=True)
        X = X.astype("float32") / 255.0
        X = X[0:120230, :]
        X_data.append(X)
        y = [count for _ in range(120230)]
        count += 1
        y = np.array(y).astype("float32")
        y = y.reshape(y.shape[0], 1)
        y_data.append(y)

    return X_data, y_data


if __name__ == "__main__":
    data_path = "../../data/raw/"
    features, labels = load_data(data_path)

    features = np.array(features).astype("float32")
    labels = np.array(labels).astype("float32")

    features = features.reshape(
        features.shape[0] * features.shape[1], features.shape[2]
    )
    labels = labels.reshape(labels.shape[0] * labels.shape[1], labels.shape[2])

    feature_data_path = "../../data/feature"
    if not os.path.exists(feature_data_path):
        os.makedirs(feature_data_path)
    with open(f"{feature_data_path}/features", "wb") as f:
        pickle.dump(features, f, protocol=4)
    with open(f"{feature_data_path}/labels", "wb") as f:
        pickle.dump(labels, f, protocol=4)

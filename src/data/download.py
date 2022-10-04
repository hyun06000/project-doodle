import os
import urllib.request


def download(data_path, categories):
    # base link
    base = "https://storage.googleapis.com/quickdraw_dataset/full/"

    # download each category as npy file
    for category in categories:
        path = f"{base}numpy_bitmap/{category}.npy"
        print(path)
        urllib.request.urlretrieve(path, f"{data_path}/{category}.npy")


if __name__ == "__main__":
    data_path = "../../data/raw"
    if not os.path.exists(data_path):
        os.makedirs(data_path)

    categories = [
        "hat",
        "moon",
    ]
    download(data_path, categories)

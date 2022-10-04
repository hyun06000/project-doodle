import cv2
from PIL import Image
import numpy as np
from keras.models import load_model


def process_image(img):
    x_shape, y_shape = 28, 28
    img = img.resize((x_shape, y_shape))
    img = np.array(img, dtype=np.float32)
    img = np.reshape(img, (-1, x_shape, y_shape, 1))
    return img


def model_predict(image):
    categories = [
        "모자",
        "달",
    ]
    model = load_model("../../model/CNN.h5")
    processed = process_image(image)
    pred_probab = model.predict(processed)[0]
    print("pred_probab", pred_probab, pred_probab.argmax())
    pred_class = categories[pred_probab.argmax()]
    return pred_class

if __name__=="__main__":
    file_path = "/Users/haeunoh/project-doodle/frontend/app/image_draw.png"
    image = Image.open(file_path)
    print(model_predict(image))
import cv2
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
        "사과",
        "나비 넥타이",
        "초",
        "문",
        "봉투",
        "물고기",
        "기타",
        "아이스크림",
        "번개",
        "달",
        "산",
        "별",
        "텐트",
        "칫솔",
        "손목시계",
    ]
    model = load_model("../../model/CNN.h5")
    processed = process_image(image)
    pred_probab = model.predict(processed)[0]
    print("pred_probab", pred_probab, pred_probab.argmax())
    pred_class = categories[pred_probab.argmax()]
    return pred_class

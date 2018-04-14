from cv2 import imread as im
import numpy as np
import cv2

def load_data():
    path = 'data\\art\\'
    ext = '.bmp'
    X = []

    for i in range(1, 650):
        x = im(path+str(i)+ext, 0)
        x = cv2.resize(x, (28, 28))
        X.append(x)

    X = np.array(X)
    return X


print(load_data().shape)

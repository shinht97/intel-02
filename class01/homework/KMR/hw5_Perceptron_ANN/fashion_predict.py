import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import *
from tensorflow.keras.optimizers import Adam
from keras.utils import to_categorical
from tensorflow.keras import datasets

num = 5
(image_train, label_train), (image_test, label_test) = datasets.fashion_mnist.load_data()
model = tf.keras.models.load_model('fashion_MNIST.h5')
predict = model.predict(image_test[0:num])
print(predict)

print(" * Prediction,", np.argmax(predict, axis=1))

plt.figure(figsize=(15,15))
for idx in range(num):
    sp = plt.subplot(1, 5, idx+1)
    plt.title(label_test[idx])
    plt.imshow(image_test[idx])
plt.show()
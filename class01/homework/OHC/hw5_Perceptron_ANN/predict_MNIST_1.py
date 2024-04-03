import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

model = tf.keras.models.load_model("./model/model_1.h5")

mnist = tf.keras.datasets.mnist
(image_train, label_train), (image_test, label_test) = mnist.load_data()

num = 5
predict = model.predict(image_test[0:num])
print(predict)

print(" *Prediction, ", np.argmax(predict, axis = 1))

plt.figure(figsize=(15, 15))
for idx in range(num):
    sp = plt.subplot(1,5,idx+1)
    plt.imshow(image_test[idx])
plt.show()
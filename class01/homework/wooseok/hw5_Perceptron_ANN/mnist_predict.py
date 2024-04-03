import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from keras.models import Sequential
from keras.layers import Flatten
from keras.layers import Dense

model = tf.keras.models.load_model('mnist_model.h5')
mnist = tf.keras.datasets.mnist
(image_train,label_train),(image_test,label_test) = mnist.load_data()

NUM = 5
predict = model.predict(image_test[0:NUM])
print(predict)

print("* Prediction,",np.argmax(predict,axis=1))
plt.figure(figsize=(15,15))
for idx in range (NUM):
    sp = plt.subplot(1,5,idx+1)
    plt.imshow(image_test[idx])
plt.show()
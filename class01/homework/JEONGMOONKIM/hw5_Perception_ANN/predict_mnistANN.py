import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras.models import *
from tensorflow.keras.layers import *

model=tf.keras.models.load_model('mnist_ANN.h5')

mnist=tf.keras.datasets.mnist
(image_train, label_train), (image_test, label_test)=\
mnist.load_data()

num=5
predict=model.predict(image_test[0:num])
print(predict)

print(" * Presiction, ", np.argmax(predict, axis=1))

plt.figure(figsize=(15,15))
for idx in range(num):
    sp=plt.subplot(1,5,idx+1)
    plt.imshow(image_test[idx])
plt.show()
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from keras.models import Sequential
from keras.layers import Flatten
from keras.layers import Dense

f_mnist = tf.keras.datasets.fashion_mnist

(image_train, label_train), (image_test, label_test) = f_mnist.load_data()

print("Train Image shape : " , image_train.shape)
# print("Train Labe : ", label_train, '\n')
# print(image_train[0])

# NUM = 20
# plt.figure(figsize = (15, 15))
# for idx in range(NUM):
#     sp = plt.subplot(5, 5, idx+1)
#     plt.imshow(image_train[idx])
#     plt.title(f'Label: {label_train[idx]}')
    
# # plt.show()

# model = Sequential([
#     Flatten(), 
#     Dense(128, activation = 'sigmoid'), 
#     Dense(64, activation='sigmoid'), 
#     Dense(10, activation='softmax'),
#     ], 
#     name="Simple_ANN")

# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'],)
# model.fit(image_train, label_train, epochs=10, batch_size=10)
# model.summary()
# model.save('f_mnist_model.h5')
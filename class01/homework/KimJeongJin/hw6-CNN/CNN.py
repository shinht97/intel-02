import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import *
from tensorflow.keras.optimizers import Adam
from keras.utils import to_categorical
from tensorflow.keras import datasets

mnist = datasets.mnist

(image_train, label_train), (image_test, label_test) = mnist.load_data()
print("Train Image shape: ", image_train.shape)
print("Train Label: ", label_train, "\n")
print(image_train[0])

NUM=20
plt.figure(figsize=(15,15))
for idx in range(NUM):
    sp = plt.subplot(5,5,idx+1)
    plt.imshow(image_train[idx])
    plt.title(f'Label: {label_train[idx]}')
plt.show()

model = Sequential() 
model.add(Conv2D(64,(3,3),activation='relu',input_shape=(28,28,1)))
model.add(MaxPooling2D((2,2)))
model.add(Conv2D(64,(3,3),activation='relu'))
model.add(MaxPooling2D((2,2)))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(10))
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',
              metrics=['accuracy'],)
model.fit(image_train, label_train, epochs=10, batch_size=10)
model.summary()
model.save('mnist_cnn.h5')
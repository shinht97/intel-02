# 훈련
import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np


#handwriten digit
mnist = tf.keras.datasets.mnist
(image_train, label_train), (image_test,
label_test) = mnist.load_data()
print("Train Image shape : ",image_train.shape)
print("Train Labe : ",label_train,"\n")
print(image_train[0])
# draw test images with predicted value


model = tf.keras.Sequential([
    
    tf.keras.layers.Conv2D(64, (3,3), activation='relu',input_shape=(28,28,1)), 
    tf.keras.layers.MaxPool2D((2,2)),
    tf.keras.layers.Conv2D(64,(3,3), activation='relu'),
    tf.keras.layers.MaxPool2D((2,2)),
    tf.keras.layers.Conv2D(64,(3,3), activation='relu'),
    tf.keras.layers.Dense(128, activation='sigmoid'),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(64, activation='sigmoid'),
    tf.keras.layers.Dense(10, activation='softmax'),
], name="Simple-ANN")
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'],
)
model.fit(image_train, label_train,
epochs=10, batch_size=10)
model.summary()
model.save('mnist_CNN.h5')
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
NUM=20
for idx in range(NUM):
    sp = plt.subplot(5,5,idx+1)
    plt.imshow(image_test[idx])
plt.show()

model = tf.keras.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='sigmoid'),
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
model.save('mnist_ANN.h5')
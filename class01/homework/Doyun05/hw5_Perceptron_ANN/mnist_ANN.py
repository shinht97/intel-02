import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

mnist = tf.keras.datasets.mnist

(img_train, label_train), (img_test, label_test) = mnist.load_data()

print(f"Train Image shape : {img_train.shape}")
print(f"Train Label : {label_train.shape}")

# print(img_train[0])

num = 20

plt.figure(figsize = (15, 15))

for idx in range(num):
    sp = plt.subplot(5, 5, idx + 1)
    plt.imshow(img_train[idx], cmap = "gray")
    plt.title(f"label : {label_train[idx]}")
    
plt.show()

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape = (28, 28)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation = "sigmoid"),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(64, activation = "sigmoid"),
    tf.keras.layers.Dropout(0.15),
    tf.keras.layers.Dense(16, activation = "sigmoid"),
    tf.keras.layers.Dropout(0.1),
    tf.keras.layers.Dense(10, activation = "softmax")
], name = "Simple_ANN")

model.compile(optimizer = "adam", loss = "sparse_categorical_crossentropy", metrics = ["accuracy"])

model.summary()

model.fit(img_train, label_train, epochs = 10, batch_size = 10, validation_split = 0.2, verbose = 1)

model.save("/home/ubuntu/workdir/practice_python/mnist.h5")



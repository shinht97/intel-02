import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

fashion = tf.keras.datasets.fashion_mnist

(img_train, label_train), (img_test, label_test) = fashion.load_data()

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape = (28, 28)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation = "sigmoid"),
    tf.keras.layers.Dense(64, activation = "sigmoid"),
    tf.keras.layers.Dense(16, activation = "sigmoid"),
    tf.keras.layers.Dense(10, activation = "softmax")
], name = "fashion_ANN")

model.compile(optimizer = "adam", loss = "sparse_categorical_crossentropy", metrics = ["accuracy"])

model.summary()

model.fit(img_train, label_train, epochs = 10, batch_size = 10, validation_split = 0.2, verbose = 1)

model.save("/home/ubuntu/workdir/practice_python/fashion_mnist.h5")

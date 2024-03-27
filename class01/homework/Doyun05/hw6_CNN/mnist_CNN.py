import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

fashion = tf.keras.datasets.fashion_mnist

(img_train, label_train), (img_test, label_test) = fashion.load_data()

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape = (28, 28, 1)),
    tf.keras.layers.Conv2D(32, (3, 3), padding = "same", activation = "relu", input_shape = (28, 28, 1)),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), padding = "same", activation = "relu"),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Conv2D(64, (3, 3), padding = "same", activation = "relu"),
    tf.keras.layers.MaxPooling2D((2, 2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation = "relu"),
    tf.keras.layers.Dense(64, activation = "relu"),
    tf.keras.layers.Dense(16, activation = "relu"),
    tf.keras.layers.Dense(10, activation = "softmax")
], name = "fashion_ANN")

model.compile(optimizer = "adam", loss = "sparse_categorical_crossentropy", metrics = ["accuracy"])

model.summary()

model.fit(img_train, label_train, epochs = 10, batch_size = 10, validation_split = 0.2, verbose = 1)

model.save("/home/ubuntu/workdir/practice_python/fashion_mnist_cnn.h5")

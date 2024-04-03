import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Flatten, Dense

mnist = tf.keras.datasets.fashion_mnist

(image_train, label_train), (image_test, label_test) = mnist.load_data()
# print("Train Image shape :", image_train.shape)
# print("Train Label :", label_train, "\n")
# print(image_train[0])

# NUM = 20
# plt.figure(figsize=(15,15))
# for idx in range(NUM):
#     sp = plt.subplot(5, 5, idx+1)
#     plt.imshow(image_train[idx])
#     plt.title(f'Label: {label_train[idx]}')
# plt.show()


model = Sequential([
    Flatten(),
    Dense(128, activation='sigmoid'),
    Dense(64, activation='sigmoid'),
    Dense(10, activation='softmax'),
], name="Simple-ANN")

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'],
)

model.fit(image_train, label_train,
          epochs=10, batch_size=10)

model.summary()
model.save("fashion_mnist_ANN.h5")

NUM = 5
predict = model.predict(image_test[10:10+NUM])
print(predict)

print(" * prediction,",
      np.argmax(predict, axis = 1))

labels = ['T-Shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal',
          'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

plt.figure(figsize=(15,15))
for idx in range(NUM):
    sp = plt.subplot(1,5,idx+1)
    plt.imshow(image_test[10+idx])
    plt.title(f'Label: {labels[label_test[10+idx]]}')
plt.show()

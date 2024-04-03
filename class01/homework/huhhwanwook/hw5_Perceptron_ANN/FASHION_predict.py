import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

model = tf.keras.models.load_model('f_mnist_model.h5')

f_mnist = tf.keras.datasets.fashion_mnist

(image_train, label_train), (image_test, label_test) = f_mnist.load_data()


NUM=5
predict = model.predict(image_test[0:NUM])
print(predict)

print(" * Prediction,", np.argmax(predict, axis=1))

plt.figure(figsize=(15, 15))
for idx in range(NUM):
    sp = plt.subplot(1, 5, idx+1)
    plt.title(label_test[idx])
    plt.imshow(image_test[idx])
plt.show()
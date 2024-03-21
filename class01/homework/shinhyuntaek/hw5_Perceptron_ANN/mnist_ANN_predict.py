import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

model = tf.keras.models.load_model("./mnist.h5")

mnist = tf.keras.datasets.mnist

(img_train, label_train), (img_test, label_test) = mnist.load_data()

num = 5

predict = model.predict(img_test[0:num])

print(predict)

print(f"* predict {np.argmax(predict, axis = 1)}")

plt.figure(figsize = (15, 15))

for idx in range(num):
    sp = plt.subplot(1, 5, idx + 1)
    plt.imshow(img_test[idx])
    plt.title(f"predict : {np.argmax(predict, axis = 1)[idx]}")
    
plt.show()

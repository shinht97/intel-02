import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

model = tf.keras.models.load_model("./fashion_mnist_cnn.h5")

fashion = tf.keras.datasets.fashion_mnist

(img_train, label_train), (img_test, label_test) = fashion.load_data()

num = 5

fashion = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankel boot"]

predict = model.predict(img_test[0:num])

print(predict)

print(f"* predict {np.argmax(predict, axis = 1)}")

plt.figure(figsize = (15, 15))

for idx in range(num):
    sp = plt.subplot(1, 5, idx + 1)
    plt.imshow(img_test[idx], cmap = "gray")
    plt.title(f"predict : {fashion[np.argmax(predict, axis = 1)[idx]]} \n real : {fashion[label_test[idx]]}")
    
plt.show()
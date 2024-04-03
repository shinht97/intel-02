import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

model = tf.keras.models.load_model('/home/jsum/workdir/model/mnist.h5')

mnist = tf.keras.datasets.mnist


(image_train, label_train),(image_test,label_test) = mnist.load_data()

num = 5

predict = model.predict(image_test[0:num])
print(predict)

print(" * Predict, ", np.argmax(predict,axis=1))

plt.figure(figsize=(15,15))
for idx in range(num):
    sp = plt.subplot(1,5,idx+1)
    plt.title(np.argmax(predict,axis=1)[idx])
    plt.imshow(image_test[idx])

plt.show()
                        
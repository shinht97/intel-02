import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

model = tf.keras.models.load_model('/home/jsum/workdir/mnist/CNN_mnist.h5')

CNN_mnist = tf.keras.datasets.mnist


(image_train, label_train),(image_test,label_test) = CNN_mnist.load_data()

num = 5

predict = model.predict(image_test[0:num])
print(predict)

print(" * Predict, ", np.argmax(predict,axis=1))

plt.figure(figsize=(15,15))
for idx in range(num):
    sp = plt.subplot(1,5,idx+1)
    plt.title("result:{}  label : {}".format(np.argmax(predict,axis=1)[idx],label_test[idx]))
    plt.imshow(image_test[idx])

plt.show()
                        
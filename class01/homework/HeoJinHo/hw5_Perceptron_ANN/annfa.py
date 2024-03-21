import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

model = tf.keras.models.load_model('fashion_mnist_ANN.h5')
#handwriten digit
mnist = tf.keras.datasets.mnist
(image_train, label_train), (image_test,
label_test) = mnist.load_data()
print("Train Image shape : ",image_train.shape)
print("Train Labe : ",label_train,"\n")
print(image_train[0])

#MODEL INFERENCING
#• tf.model.predict()
# draw test images with predicted value
NUM = 5
predict = model.predict(image_test[0:NUM])
print(predict)
print(" * Prediction,",np.argmax(predict, axis =1))
plt.figure(figsize=(15,15))
for idx in range(NUM):
    sp = plt.subplot(1,5,idx+1)
    plt.title(label_test[idx])
    plt.imshow(image_test[idx])
plt.show()

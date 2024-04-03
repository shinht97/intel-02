
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Dense, Flatten,Conv2D,MaxPooling2D


mnist = tf.keras.datasets.mnist


(image_train, label_train),(image_test,label_test) = mnist.load_data()

print("Train Image shape :",image_train.shape)
print("Train Label :",label_train.shape)

print(image_train[0])
print(label_train[0])

NUM = 20

plt.figure(figsize=(18,18))
for idx in range(NUM):
    sp = plt.subplot(5,5,idx+1)
    plt.imshow(image_train[idx])
    plt.title(f'Label: {label_train[idx]}' )
plt.show()

model = tf.keras.Sequential()


    
model = Sequential()
model.add(Conv2D(64, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Flatten())
model.add(Dense(64, activation='relu'))
model.add(Dense(10))

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'],)
model.fit(image_train,label_train,epochs=10,batch_size=10)
model.summary()
model.save('CNN_mnist.h5')




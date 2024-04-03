import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

model = tf.keras.models.load_model('minist2_ANN.h5')

# Fashion MNIST 데이터셋 로드
fashion_mnist = tf.keras.datasets.fashion_mnist
(image_train, label_train), (image_test, label_test) = fashion_mnist.load_data()
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


model = tf.keras.Sequential([tf.keras.layers.Flatten(),tf.keras.layers.Dense(128, activation='sigmoid'),tf.keras.layers.Dense(64, activation='sigmoid'),tf.keras.layers.Dense(10, activation='softmax'),], name="Simple-ANN")
model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'],)
model.fit(image_train, label_train,epochs=10, batch_size=10)
model.summary()
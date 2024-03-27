
#handwriten digit
mnist = tf.keras.datasets.mnist
(image_train, label_train), (image_test,
label_test) = mnist.load_data()
print("Train Image shape : ",image_train.shape)
print("Train Labe : ",label_train,"\n")
print(image_train[0])
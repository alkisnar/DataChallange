#!/usr/bin/env python
# coding: utf-8

# In[65]:


import tensorflow as tf

mnist = tf.keras.datasets.mnist #import dataset of numbers that are handwritten 0-9

(x_train, y_train), (x_test, y_test) = mnist.load_data()

#normalize datapoints to scale from 0 to 1
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

#building model
model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten()) #flattening layer
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu)) #using 128 neurons in layer
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

#parameters of training
#Adam optimization algorithm
#sparse_catagorical_crossentropy, produces a category index of the most likely matching category
model.compile(optimizer='adam',
             loss='sparse_categorical_crossentropy',
             metrics=['accuracy'])

model.fit(x_train, y_train, epochs=3)


# In[94]:


model.save('test.model')
new_model = tf.keras.models.load_model('test.model')
predictions = new_model.predict([x_test])
import numpy as np
p = 2
print("seems to be a", np.argmax(predictions[p]) )
plt.imshow(x_test[p])
plt.show()


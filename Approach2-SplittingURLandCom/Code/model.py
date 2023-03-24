import tensorflow as tf
import numpy as np
from tensorflow import keras
from prepareData import prepare_data

training_subdomain_features, training_subdomain_labels, training_second_level_features, training_second_level_labels, \
    training_top_level_features, training_top_level_labels, training_subdirectory_features, \
    training_subdirectory_labels, testing_subdomain_features, testing_subdomain_labels, testing_second_level_features, \
    testing_second_level_labels, testing_top_level_features, testing_top_level_labels, testing_subdirectory_features, \
    testing_subdirectory_labels = prepare_data()

# defining input tensor sizes
input_tensor_subdomain = tf.keras.layers.Input(shape=(62,))
input_tensor_second_level = tf.keras.layers.Input(shape=(63,))
input_tensor_top_level = tf.keras.layers.Input(shape=(217,))
input_tensor_subdirectory = tf.keras.layers.Input(shape=(2125,))

concatenated_tensor = tf.keras.layers.concatenate([input_tensor_subdomain, input_tensor_second_level,
                                                   input_tensor_top_level, input_tensor_subdirectory])

hidden_1 = tf.keras.layers.Dense(64, activation=tf.nn.relu)(concatenated_tensor)
hidden_2 = tf.keras.layers.Dense(32, activation=tf.nn.relu)(hidden_1)
hidden_3 = tf.keras.layers.Dense(16, activation=tf.nn.relu)(hidden_2)
hidden_4 = tf.keras.layers.Dense(8, activation=tf.nn.relu)(hidden_3)
output_layer = tf.keras.layers.Dense(1, activation=tf.nn.sigmoid)(hidden_4)

model = tf.keras.models.Model(inputs=[input_tensor_subdomain, input_tensor_second_level, input_tensor_top_level,
                                      input_tensor_subdirectory], outputs=output_layer)

model.compile(optimizer='rmsprop',
              loss=tf.keras.losses.MeanSquaredError(),
              metrics=['accuracy'])

# Concatenating train labels horizontally
train_labels_concat = np.concatenate([training_subdomain_labels, training_second_level_labels,
                                      training_top_level_labels, training_subdirectory_labels], axis=1)

model.fit(x=[training_subdomain_features, training_second_level_features, training_top_level_features,
             training_subdirectory_features], y=train_labels_concat, epochs=5, batch_size=10)

test_loss, test_acc = model.evaluate([testing_subdomain_features, testing_second_level_features,
                                      testing_top_level_features, testing_subdirectory_features],
                                     [testing_subdomain_labels, testing_second_level_labels, testing_top_level_labels,
                                      testing_subdirectory_labels], batch_size=10)
print("test accuracy:", test_acc)

# predictions = model.predict(testing_features)

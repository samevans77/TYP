import tensorflow as tf
import numpy as np
from tensorflow import keras
from prepareData import prepare_data

training_subdomain_features, training_subdomain_labels, training_second_level_features, training_second_level_labels, \
    training_top_level_features, training_top_level_labels, training_subdirectory_features, \
    training_subdirectory_labels, testing_subdomain_features, testing_subdomain_labels, testing_second_level_features, \
    testing_second_level_labels, testing_top_level_features, testing_top_level_labels, testing_subdirectory_features, \
    testing_subdirectory_labels, training_additional_features, training_additional_labels, testing_additional_features, \
    testing_additional_labels = prepare_data()

# defining input tensor sizes
input_tensor_subdomain = tf.keras.layers.Input(shape=(62,))
input_tensor_second_level = tf.keras.layers.Input(shape=(63,))
input_tensor_top_level = tf.keras.layers.Input(shape=(217,))
input_tensor_subdirectory = tf.keras.layers.Input(shape=(2125,))
input_tensor_additional = tf.keras.layers.Input(shape=(7,))

concatenated_tensor = tf.keras.layers.concatenate([input_tensor_subdomain, input_tensor_second_level,
                                                   input_tensor_top_level, input_tensor_subdirectory,
                                                   input_tensor_additional])

hidden_1 = tf.keras.layers.Dense(128, activation=tf.nn.relu)(concatenated_tensor)
hidden_2 = tf.keras.layers.Dense(64, activation=tf.nn.relu)(hidden_1)
hidden_3 = tf.keras.layers.Dense(32, activation=tf.nn.relu)(hidden_2)
hidden_4 = tf.keras.layers.Dense(16, activation=tf.nn.relu)(hidden_3)
hidden_5 = tf.keras.layers.Dense(8, activation=tf.nn.relu)(hidden_4)
hidden_6 = tf.keras.layers.Dense(4, activation=tf.nn.relu)(hidden_5)
output_layer = tf.keras.layers.Dense(1, activation=tf.nn.sigmoid)(hidden_6)

model = tf.keras.models.Model(inputs=[input_tensor_subdomain, input_tensor_second_level, input_tensor_top_level,
                                      input_tensor_subdirectory, input_tensor_additional], outputs=output_layer)

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              loss=tf.keras.losses.binary_crossentropy,
              metrics=['accuracy', 'FalseNegatives', 'FalsePositives', 'TrueNegatives', 'TruePositives', 'Precision'])

# Concatenating train labels horizontally
train_labels_concat = np.concatenate([training_subdomain_labels, training_second_level_labels,
                                      training_top_level_labels, training_subdirectory_labels,
                                      training_additional_labels], axis=1)

history = model.fit(x=[training_subdomain_features, training_second_level_features, training_top_level_features,
             training_subdirectory_features, training_additional_features],
          y=training_subdomain_labels, epochs=100, batch_size=32)

test_loss, test_acc, fn, fp, tn, tp, presc = model.evaluate([testing_subdomain_features, testing_second_level_features,
                                      testing_top_level_features, testing_subdirectory_features,
                                      testing_additional_features],
                                     [testing_subdomain_labels, testing_second_level_labels, testing_top_level_labels,
                                      testing_subdirectory_labels, testing_additional_labels], batch_size=10)
print("test accuracy:", test_acc)
print("FN", fn)
print("FP", fp)
print("TN", tn)
print("TP", tp)
print("Presc", presc)

print("\nAccuracy")
print(history.history['accuracy'])

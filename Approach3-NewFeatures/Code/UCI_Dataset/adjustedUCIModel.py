from prepareUCIAdjustedData import prepare_data
import tensorflow as tf


training_features, training_labels, testing_features, testing_labels = prepare_data()

# defining input tensor sizes
input_tensor = tf.keras.layers.Input(shape=(7,))
hidden_1 = tf.keras.layers.Dense(64, activation=tf.nn.relu)(input_tensor)
hidden_2 = tf.keras.layers.Dense(32, activation=tf.nn.relu)(hidden_1)
hidden_3 = tf.keras.layers.Dense(16, activation=tf.nn.relu)(hidden_2)
hidden_4 = tf.keras.layers.Dense(8, activation=tf.nn.relu)(hidden_3)
output_layer = tf.keras.layers.Dense(1, activation=tf.nn.sigmoid)(hidden_4)

model = tf.keras.models.Model(inputs=input_tensor, outputs=output_layer)

model.compile(optimizer=tf.keras.optimizers.SGD(),
              loss=tf.keras.losses.MeanSquaredError(),
              metrics=['accuracy'])

model.fit(training_features, training_labels, epochs=100, batch_size=10)

test_loss, test_acc = model.evaluate(testing_features, testing_labels, batch_size=10)

print("Test accuracy:", test_acc)

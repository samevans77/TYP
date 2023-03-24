import tensorflow as tf
from tensorflow import keras
from prepareData import prepare_data
from sklearn.metrics import confusion_matrix, f1_score

training_features, training_labels, testing_features, testing_labels = prepare_data()

model = keras.Sequential([
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(128, activation=tf.nn.relu),
    keras.layers.Dense(64, activation=tf.nn.relu),
    keras.layers.Dense(32, activation=tf.nn.relu),
    keras.layers.Dense(16, activation=tf.nn.relu),
    keras.layers.Dense(8, activation=tf.nn.relu),
    keras.layers.Dense(4, activation=tf.nn.relu),
    keras.layers.Dense(1, activation=tf.nn.sigmoid)
])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
              loss=tf.keras.losses.binary_crossentropy,
              metrics=['accuracy', 'FalseNegatives', 'FalsePositives', 'TrueNegatives', 'TruePositives', 'Precision'])

history = model.fit(training_features, training_labels, epochs=100, batch_size=32)

test_loss, test_acc, fn, fp, tn, tp, presc = model.evaluate(testing_features, testing_labels, batch_size=10)
print("test accuracy:", test_acc)
print("FN", fn)
print("FP", fp)
print("TN", tn)
print("TP", tp)
print("Presc", presc)

print("\nAccuracy")
print(history.history['accuracy'])


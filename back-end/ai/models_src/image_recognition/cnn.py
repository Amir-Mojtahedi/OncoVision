from collections import Counter
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.src.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint
from keras._tf_keras.keras.utils import image_dataset_from_directory
from keras import regularizers
from sklearn.utils.class_weight import compute_class_weight

# Run this script from the root directory of the project e.i. OncoVision
train_data_dir = './backend/ai/dataset/train'
test_data_dir = './backend/ai/dataset/test'

batch_size = 32
img_height = 224
img_width = 224
num_classes = 2  # Number of classes (e.g., Malignant and Benign)

train_ds = image_dataset_from_directory(
    directory = train_data_dir,
    label_mode = "binary",
    batch_size = batch_size,
    image_size = (img_height, img_width),
    seed = 123,
    validation_split = 0.2,
    subset = "training"
)

validation_ds = image_dataset_from_directory(
    directory = train_data_dir,
    label_mode = "binary",
    batch_size = batch_size,
    image_size = (img_height, img_width),
    seed = 123,
    validation_split = 0.2,
    subset = "validation"
)

test_ds = image_dataset_from_directory(
    directory = test_data_dir,
    label_mode = "binary",
    batch_size = batch_size,
    image_size = (img_height, img_width),
    seed = 123
)

all_labels = []
for images, labels in train_ds.unbatch():
    all_labels.append(labels.numpy().item())

# Define classes
classes = np.unique(all_labels)
class_weights = compute_class_weight(
    class_weight='balanced',
    classes=classes,
    y=all_labels
)

# Convert to dict format
class_weight_dict = {
    int(k): float(v) for k, v in zip(classes, class_weights)
}

early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=5, min_lr=1e-6)

model = keras.Sequential([
    keras.Input(shape=(img_height, img_width, 3)),
    keras.layers.RandomFlip("horizontal"),
    keras.layers.RandomRotation(0.1),
    keras.layers.RandomZoom(0.1),
    keras.layers.RandomContrast(0.2),
    keras.layers.Rescaling(1./255),
    keras.layers.Conv2D(16, 3, padding='same', activation='relu'),
    keras.layers.BatchNormalization(),
    keras.layers.MaxPooling2D(),
    keras.layers.Conv2D(32, 3, padding='same', activation='relu'),
    keras.layers.BatchNormalization(),
    keras.layers.MaxPooling2D(),
    keras.layers.Conv2D(64, 3, padding='same', activation='relu'),
    keras.layers.BatchNormalization(),
    keras.layers.MaxPooling2D(),
    keras.layers.Conv2D(128, 3, padding='same', activation='relu'),
    keras.layers.BatchNormalization(),
    keras.layers.MaxPooling2D(),
    keras.layers.Dropout(0.2),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation='relu', kernel_regularizer=regularizers.l2(0.01)),
    keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer="adam",
              loss="binary_crossentropy",
              metrics=['accuracy'])

checkpoint = ModelCheckpoint('./backend/ai/models', save_best_only=True, monitor='val_loss', mode='min')

epochs = 10
cancer_cnn_model = model.fit(
    train_ds,
    validation_data=validation_ds,
    epochs=epochs,
    class_weight=class_weight_dict,
    callbacks=[early_stopping, reduce_lr, checkpoint]
)

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input

# Define the directories containing your dataset
train_dir = 'C:\\project_check\\image\\dataset'
validation_dir = 'C:\\project_check\\image\\dataset'

# Define image dimensions and batch size
image_size = (100, 100)  # Reduced image size
batch_size = 16  # Reduced batch size

# Data augmentation and normalization for training
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.1,
    height_shift_range=0.1,
    shear_range=0.1,
    zoom_range=0.1,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Normalization for validation
validation_datagen = ImageDataGenerator(rescale=1./255)

# Flow training images in batches of batch_size using train_datagen generator
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=image_size,
    batch_size=batch_size,
    class_mode='binary'
)

# Flow validation images in batches of batch_size using validation_datagen generator
validation_generator = validation_datagen.flow_from_directory(
    validation_dir,
    target_size=image_size,
    batch_size=batch_size,
    class_mode='binary'
)

# Load the VGG16 model without the fully connected layers and use it as a feature extractor
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(image_size[0], image_size[1], 3))

# Freeze the convolutional layers
for layer in base_model.layers:
    layer.trainable = False

# Create a new model
model = Sequential([
    base_model,
    Flatten(),
    Dense(512, activation='relu'),
    Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Print the summary of the model
model.summary()

# Train the model
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // batch_size,
    epochs=11,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // batch_size
)

# Save the model to an HDF5 file
model.save('new_latest_crime_classifier_model.h5')


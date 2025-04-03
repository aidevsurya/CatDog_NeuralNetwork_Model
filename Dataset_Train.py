from tf_keras.models import Sequential
from tf_keras.layers import Dense
from tf_keras.layers import Conv2D
from tf_keras.layers import MaxPooling2D
from tf_keras.layers import Flatten
from tf_keras.layers import Dropout
from tf_keras.optimizers import Adam
from tf_keras.preprocessing.image import ImageDataGenerator

model = Sequential()

model.add(Conv2D(32,(3,3),input_shape=(64,64,3),activation="relu"))
model.add(MaxPooling2D(pool_size=(2,2)))

# model.add(Conv2D(64,(3,3),input_shape=(64,64,3),activation="relu"))
# model.add(MaxPooling2D(pool_size=(2,2)))

# model.add(Conv2D(128,(3,3),activation="relu"))
# model.add(MaxPooling2D(pool_size=(2,2)))

model.add(Dropout(0.2))

model.add(Flatten())
model.add(Dense(units=64,activation="relu"))
model.add(Dense(units=3,activation="softmax"))

model.compile(optimizer=Adam(learning_rate=0.001),loss="binary_crossentropy",metrics=["accuracy"])

train_gen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    horizontal_flip=True)

test_gen = ImageDataGenerator(rescale=1/255)

train_dataset = train_gen.flow_from_directory("train",
                                              target_size=(64,64),
                                              batch_size=30,
                                              class_mode="categorical")

val_dataset = test_gen.flow_from_directory("val",
                                              target_size=(64,64),
                                              batch_size=10,
                                              class_mode="categorical")

print(next(train_dataset))

model.fit(train_dataset,
                    steps_per_epoch=10,
                    epochs=50,
                    validation_data=val_dataset,
                    validation_steps=2)

with open("model.json","w") as file:
    file.write(model.to_json())
model.save_weights("model.h5")
print("Trained model and saved as 'model.h5' and 'model.json'")
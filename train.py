from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D,MaxPooling2D,Flatten,Dense
from tensorflow.keras.preprocessing.image import ImageDataGenerator
img=224
gen=ImageDataGenerator(rescale=1/255.)
train=gen.flow_from_directory("dataset/Training",target_size=(img,img),class_mode="categorical")
model=Sequential([Conv2D(32,(3,3),activation="relu",input_shape=(img,img,3)),MaxPooling2D(),Flatten(),Dense(64,activation="relu"),Dense(4,activation="softmax")])
model.compile(optimizer="adam",loss="categorical_crossentropy",metrics=["accuracy"])
model.fit(train,epochs=5)
model.save("models/brain_tumor_model.h5")

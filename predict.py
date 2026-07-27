from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
labels=["glioma","meningioma","notumor","pituitary"]
m=load_model("models/brain_tumor_model.h5")
img=image.load_img("sample.jpg",target_size=(224,224))
x=image.img_to_array(img)/255.
x=np.expand_dims(x,0)
p=m.predict(x)[0]
print(labels[np.argmax(p)],float(np.max(p)))

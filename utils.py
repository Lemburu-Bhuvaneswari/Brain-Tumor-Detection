from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
labels=["glioma","meningioma","notumor","pituitary"]
model=load_model("models/brain_tumor_model.h5")
def predict(path):
    img=image.load_img(path,target_size=(224,224))
    x=image.img_to_array(img)/255.
    x=np.expand_dims(x,0)
    p=model.predict(x)[0]
    return labels[np.argmax(p)],float(np.max(p))

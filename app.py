from flask import Flask,render_template,request
import os
from utils import predict
app=Flask(__name__)
UPLOAD="uploads";os.makedirs(UPLOAD,exist_ok=True)
@app.route("/",methods=["GET","POST"])
def home():
    if request.method=="POST":
        f=request.files["file"]
        path=os.path.join(UPLOAD,f.filename);f.save(path)
        label,conf=predict(path)
        return render_template("result.html",label=label,conf=round(conf*100,2),img=f.filename)
    return render_template("index.html")
@app.route("/uploads/<name>")
def up(name):
    from flask import send_from_directory
    return send_from_directory(UPLOAD,name)
app.run(debug=True)

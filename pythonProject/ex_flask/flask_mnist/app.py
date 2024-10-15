from flask import Flask, render_template, request, jsonify
from keras.models import load_model
import numpy as np
from PIL import Image
import io

#모델 로드
model = load_model("./mnist_ann.h5")
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("mnist_index.html")

@app.route("/predict", methods=['POST'])
def predict():
    file = request.files['file']
    #이미지 전처리
    img = Image.open(io.BytesIO(file.read()))
    img = img.resize((28, 28)).convert("L")
    img = 255 - np.array(img)
    sample = img.reshape(1, 784).astype('float32') / 255
    #예측 수행
    pred = model.predict(sample)
    pred_cls = np.argmax(pred, axis=1)[0]
    pred = float(np.max(pred))
    return jsonify({ 'class' : int(pred_cls)
                     ,'pred' : pred})

if __name__ == '__main__':
    app.run(debug=True)
import os,sys
from flask import Flask,render_template,jsonify,request
from flask_cors import cross_origin,CORS

from src.pipeline.prediction_pipline import PredictionPipline
from src.logging.logger import logging
from src.exception.exception import CustomException
from src.utils.utils import decodeimage

app=Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename='InputImage.jpg'
        self.clf=PredictionPipline(self.filename)


@app.route('/')
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/train',methods=['GET','POST'])
@cross_origin()
def train():
    os.system('dvc repro')
    return 'Train success'

@app.route('/predict',methods=['POST'])
@cross_origin()
def predict():
    image=request.json['image']
    decodeimage(img_str=image,filename=clapp.filename)
    result=clapp.clf.predict()

    return jsonify(result)

if __name__=='__main__':
    clapp=ClientApp()
    app.run(port=5000)
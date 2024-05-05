from src.logging.logger import logging
from src.exception.exception import CustomException

from flask import Flask,render_template,jsonify,request
import os
from flask_cors import CORS,cross_origin
from src.utils.utils import decodeImage
from src.pipeline.prediction_pipline import PredictionPipline

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app=Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self) :
        self.filename='InputImage.jpg'
        self.classifier=PredictionPipline(self.filename)


@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return render_template('index.html')

@app.route('/train',methods=['GET','POST'])
@cross_origin()
def train():
 
    os.system("dvc repro")
    return 'Train Successfully !'

@app.route('/predict',methods=['POST'])
@cross_origin()
def predict():
    image=request.json['image']
    decodeImage(imgstring=image,fileName=clapp.filename)
    result=clapp.classifier.predict()
    return jsonify(result)

if __name__=='__main__':
    clapp=ClientApp()
    app.run(port=5050,host='0.0.0.0')


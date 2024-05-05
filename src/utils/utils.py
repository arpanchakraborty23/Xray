import os,sys
import yaml
import json
import base64
from box import ConfigBox
from pathlib import Path
from tensorflow import keras
from ensure import ensure_annotations
from src.logging.logger import logging
from src.exception.exception import CustomException

@ensure_annotations
def read_yaml(file_path:Path):
    try:
        with open(file_path) as y:
            data=yaml.safe_load(y)
            logging.info(f' {file_path} has loded')
            return ConfigBox(data)
        
    except Exception as e:
        logging.info('error occured',str(e))
        raise CustomException(sys,e)

@ensure_annotations       
def create_dir(path_to_dir: list, verbose=True):
    try:

        for path in path_to_dir:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logging.info(f"created directory at: {path}")
    
    except Exception as e:
        logging.info('error occured',str(e))
        raise CustomException(sys,e)

@staticmethod
def save_model(path: Path, model: keras.Model):
        model.save(path)

def decodeimage(img_str,filename):
    image_data=base64.b64decode(img_str)
    with open(filename,'wb') as f:
        f.write()
        f.close()

import os,sys
import yaml
from Xray.logging.logger import logging
from Xray.exception.exception import CustomException
from ensure import ensure_annotation
from pathlib import Path

@ensure_annotation
def read_yaml(path_to_yaml:Path):
    try:
        logging.info('read yaml file started')
        with open(path_to_yaml) as y:
            content=yaml.safe_load(f)
            logging.info(f' yaml file {path_to_yaml} read completed')
            return content
        
    except Exception as e:
        logging.info(f'error occured {str(e)}')
        raise CustomException(sys,e)  

@ensure_annotation
def create_dir(path_to_dir:list):
    try:
        for path in path_to_dir:
            path=os.makedirs(path,exist_ok=True)
        logging.info(f' diractory {path} created')
    except Exception as e:
        logging.info(f'error occured {str(e)}')
        raise CustomException(sys,e)       


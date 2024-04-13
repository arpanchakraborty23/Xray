import os,sys
import zipfile
import gdown
from Xray.logging.logger import logging
from Xray.exception.exception import CustomException
from Xray.configuration.config_mnager import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig) -> None:
        self.config=config

    def download_data(self):
        try:
            logging.info('Downloading data started')
            data_url=self.config.source_url
            zip_download_dir=self.config.local_data_file

            os.makedirs(self.config.dir,exist_ok=True)

            logging.info(f' Download data from {data_url} into file {zip_download_dir}')

            id=data_url.split('/')[-2]
            prefix='https://drive.google.com/uc?/export=download&id='  
            gdown.download(prefix+id,zip_download_dir)
            logging.info('Downloading data completed')
        except Exception as e:
            logging.info(f'error occured {str(e)}')
            raise CustomException(sys,e)  
        

    def extract_file(self):
        unzip_file_path=self.config.unzip_data

        os.makedirs(unzip_file_path,exist_ok=True)

        with zipfile(self.config.local_data_file,'r') as z:
            z.extratall(unzip_file_path)    
            
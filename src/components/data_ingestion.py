import gdown
import os,sys
import zipfile
from src.entity.config_entity import DataIngestionConfig
from src.logging.logger import logging
from src.exception.exception import CustomException
import sys

class DataIngestion:
    def __init__(self,config:DataIngestionConfig) -> None:
        self.config=config

    def initiate_data_ingestion(self):
        try:
            data_url=self.config.source_url

            local_dir=self.config.local_data_file

            os.makedirs(self.config.dir,exist_ok=True)
            logging.info(f'download file {data_url} into {local_dir} ')

            prefix='https://drive.google.com/uc?/export=download&id='
            id=data_url.split('/')[5]

            gdown.download(prefix+id,local_dir)
            print(local_dir)
            logging.info('data loded')

           
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)
            with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
                zip_ref.extractall(unzip_path)

            logging.info('data ingestion completed')

        except Exception as e:
            logging.info(f'Error occured {str(e)}')
            raise CustomException(sys,e)
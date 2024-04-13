from Xray.components.data_ingestion import DataIngestion
from Xray.configuration.config_mnager import ConfigManager
from Xray.logging.logger import logging
from Xray.exception.exception import CustomException
import os,sys

stage_name= 'Data Ingestion'

class Data_ingestionPipline:
    def __init__(self) -> None:
        pass
    def main(self):
        config_manger=ConfigManager()
        data_ingestion_config=config_manger.get_data_ingestion_config()
        data_ingestion=DataIngestion(data_ingestion_config)
        data_ingestion.download_data()
        data_ingestion.extract_file()

if __name__=='__main__':
    try:
        logging.info(f'<<<<<<<<<< {stage_name} started >>>>>>>>>>>>')
        obj=Data_ingestionPipline()
        obj.main()
        logging.info(f'<<<<<<<<<< {stage_name} completed >>>>>>>>>>>>')

    except Exception as e:
            logging.info(f'error occured {str(e)}')
            raise CustomException(sys,e)      
from src.components.data_ingestion import DataIngestion
from src.configuration.config_manager import ConfigManger
from src.logging.logger import logging
from src.exception.exception import CustomException
import sys

class DataIngestionPipline:
    def __init__(self) -> None:
        pass

    def Pipline(self):
        try:
            logging.info('Data Ingestion pipline has started')
            config=ConfigManger()
            data_ingestion_config=config.get_data_ingestion_config()
            data_ingestion=DataIngestion(config=data_ingestion_config)
            data_ingestion.initiate_data_ingestion()
            logging.info('data Ingestion Completed')

        except Exception as e:
            logging.info(f' Error {str(e)}')
            raise CustomException(sys,e)
        
if __name__=='__main__':
    DataIngestionPipline().Pipline()
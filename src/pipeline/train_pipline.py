from src.components.data_ingestion import DataIngestion
from src.components.custom_model import CustomModel
from src.components.model_train import ModelTrain
from src.configuration.config_manager import ConfigManger
from src.logging.logger import logging
from src.exception.exception import CustomException
import sys

class TrainPipline:
    def __init__(self) -> None:
        pass

    def Pipline(self):
        try:
            logging.info('Train pipline has started')
            
            config=ConfigManger()

            logging.info(f'============={DataIngestion}===========')
            
            data_ingestion_config=config.get_data_ingestion_config()
            data_ingestion=DataIngestion(config=data_ingestion_config)
            data_ingestion.initiate_data_ingestion()
            
            logging.info(f'============={CustomModel}===========')
            custom_model_config=config.get_cusom_model_config()
            custom_model=CustomModel(config=custom_model_config)
            custom_model.initiate_custom_mode()

            logging.info(f'============={ModelTrain}===========')

            model_train_config=config.get_model_train_config()
            model_train=ModelTrain(config=model_train_config)
            model_train.get_model()
            model_train.validation_data()
            model_train.train()
          
        except Exception as e:
            logging.info(f' Error {str(e)}')
            raise CustomException(sys,e)
        


        
if __name__=='__main__':
    TrainPipline().Pipline()
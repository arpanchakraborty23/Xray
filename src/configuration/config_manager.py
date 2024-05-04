from src.utils.utils import create_dir,read_yaml
from src.constant.ymal_path import *
from src.entity.config_entity import DataIngestionConfig,CustomModelConfig,ModelTrainConfig
import os,sys

class ConfigManger:
    def __init__(self,
                 config_file_path=config_file_path,
                 params_file_path=params_file_path) -> None:
        self.config=read_yaml(config_file_path)
        self.params=read_yaml(params_file_path)

        create_dir([self.config.artifacts_root])

    def get_data_ingestion_config(self):
        config=self.config.data_ingestion

        create_dir([config.dir])

        data_ingestion_config=DataIngestionConfig(
            dir=config.dir,
            source_url=config.source_url,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    
    def get_cusom_model_config(self):
        config=self.config.custom_model
        param=self.params

        create_dir([config.dir])

        custom_model_config=CustomModelConfig(
            dir=config.dir,
            custom_Model_path=config.custom_Model_path,
            IMAGE_SIZE=param.IMAGE_SIZE,
            LEARNING_RATE=param.LEARNING_RATE,
            CLASSES=param.CLASSES
        )

        return custom_model_config
    
    def get_model_train_config(self):

        config=self.config.model_train
        train_data=os.path.join('artifacts/data_ingestion/data/train')
        test_data=os.path.join('artifacts/data_ingestion/data/test')

        model_train_config=ModelTrainConfig(
            dir=config.dir,
            model=config.model,
            model_path=config.model_path,
            train_data=train_data,
            test_data=test_data,
            eposhs=self.params.EPOCHS,
            batch_size=self.params.BATCH_SIZE,
            image_size=self.params.IMAGE_SIZE,
            AUGMENTATION=self.params.AUGMENTATION
        )
        return model_train_config
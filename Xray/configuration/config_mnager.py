import os,sys

from Xray.constant.yaml_path import *
from Xray.logging.logger import logging
from Xray.exception.exception import CustomException
from Xray.entity.config_entity import DataIngestionConfig
from Xray.utils.main_utils import read_yaml,create_dir

class ConfigManager:
    def __init__(self,
                 config_file_path,
                 params_file_path) -> None:
        self.config=read_yaml(config_file_path)
        self.params=read_yaml(params_file_path)

        create_dir([self.config.artifacts_root])

    def get_data_ingestion_config(self)-> DataIngestionConfig:
        try:
            # create data ingestion dir path
            config=self.config.data_ingestion

            # create artifacts dir
            create_dir([config.dir])
            data_ingestion_config=DataIngestionConfig(
                dir=config.dir,
                source_url=config.source_url,
                local_data_file=config.local_data_file,
                unzip_data=config.unzip_data,
            )    

            return data_ingestion_config
        except Exception as e:
            logging.info(f'error occured {str(e)}')
            raise CustomException(sys,e)  
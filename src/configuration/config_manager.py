from src.utils.utils import create_dir,read_yaml
from src.constant.ymal_path import *
from src.entity.config_entity import DataIngestionConfig

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
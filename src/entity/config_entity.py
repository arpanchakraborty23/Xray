from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    dir: Path
    source_url:Path
    local_data_file:Path
    unzip_dir:Path

@dataclass
class CustomModelConfig:
    dir:Path
    custom_Model_path:Path
    IMAGE_SIZE:list
    LEARNING_RATE:float
    CLASSES: int

@dataclass
class ModelTrainConfig:
    dir: Path
    model:Path
    model_path:Path
    train_data:Path
    test_data:Path
    eposhs:int
    batch_size:int 
    image_size:list
    AUGMENTATION: bool
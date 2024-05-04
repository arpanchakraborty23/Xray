from keras import layers,models
from tensorflow import keras 
from pathlib import Path
from src.logging.logger import logging
from src.exception.exception import CustomException
from src.entity.config_entity import CustomModelConfig


class CustomModel:
    def __init__(self,config=CustomModelConfig) -> None:
        self.config=config
    @staticmethod
    def save_model(path: Path, model: keras.Model):
        model.save(path)
    def initiate_custom_mode(self):
    
        try:
            logging.info('custom model creation started')
            
            model = models.Sequential([
            layers.Conv2D(128, (3, 3), activation='relu',input_shape=self.config.IMAGE_SIZE),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(32, (3, 3), activation='relu'),
             layers.Conv2D(16, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Flatten(),
            layers.Dense(64, activation='relu'),
            layers.Dense(self.config.CLASSES, activation='softmax')
        ])

            optimizer = keras.optimizers.SGD(learning_rate=self.config.LEARNING_RATE)
            loss = keras.losses.CategoricalCrossentropy()
            metrics = ["accuracy"]
            
            custom_model=model.compile(optimizer=optimizer, loss=loss, metrics=metrics)
            
            model.summary()  # Print summary
            self.save_model(path=self.config.custom_Model_path,model=model)
            
            return model

            
        except Exception as e:
            logging.info('error occured ', e)
            raise CustomException(sys,e) 
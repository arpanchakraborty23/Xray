import tensorflow as tf
from tensorflow import keras
from keras.models import load_model
from pathlib import Path

from src.entity.config_entity import ModelTrainConfig
from src.logging.logger import logging
from src.exception.exception import CustomException

class ModelTrain:
    def __init__(self,config:ModelTrainConfig) -> None:
        self.config=config

    def get_model(self):
        self.model=load_model(self.config.model)

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)

    def validation_data(self):
        try:
            datagen_kwargs=dict(
                rescale=1./255
            )
       
            dataflow_kwargs = dict(
            target_size=self.config.image_size[:-1],
            batch_size=self.config.batch_size,
            interpolation="bilinear"
        )       

            if self.config.AUGMENTATION:
                datagen_kwargs.update(
                    rotation_range=40,
                    horizontal_flip=True,
                    width_shift_range=0.2,
                    height_shift_range=0.2,
                    shear_range=0.2,
                    zoom_range=0.2
                )

            train_datagen=tf.keras.preprocessing.image.ImageDataGenerator(**datagen_kwargs)
            self.train_genarator=train_datagen.flow_from_directory(
                directory=self.config.train_data,
                subset='training',
                shuffle=True,
                **dataflow_kwargs
            )

            test_datagen=tf.keras.preprocessing.image.ImageDataGenerator(**datagen_kwargs)
            self.validation_genarator=test_datagen.flow_from_directory(
                directory=self.config.test_data,
                shuffle=False,
                **dataflow_kwargs
            )
        except Exception as e:
            logging.info('errorr ',str(e))
            raise CustomException(sys,e)
        
    def train(self):
        self.validation_per_steps=self.validation_genarator.samples//self.validation_genarator.batch_size

        opt=tf.keras.optimizers.SGD(learning_rate=0.01)
        loss=tf.keras.losses.categorical_crossentropy

        self.model.compile(optimizer=opt,loss=loss,metrics=['accuracy'])

        self.model.fit(
            self.train_genarator,
            epochs=self.config.eposhs,
            validation_data=self.validation_genarator
        )

        self.save_model(
                        path=self.config.model_path,model=self.model)
    
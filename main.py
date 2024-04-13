from Xray.pipeline.data_ingestion_pipline import Data_ingestionPipline
from Xray.logging.logger import logging
from Xray.exception.exception import CustomException


stage_name= 'Data Ingestion'

try:
        logging.info(f'<<<<<<<<<< {stage_name} started >>>>>>>>>>>>')
        obj=Data_ingestionPipline()
        obj.main()
        logging.info(f'<<<<<<<<<< {stage_name} completed >>>>>>>>>>>>')

except Exception as e:
            logging.info(f'error occured {str(e)}')
            raise CustomException(sys,e)    
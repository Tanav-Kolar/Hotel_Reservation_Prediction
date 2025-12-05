import os
import sys
import pandas as pd
from google.cloud import storage
from sklearn.model_selection import train_test_split
from src.logger import get_logger
from src.custom_exception import CustomException
from config.paths_config import *
from utils.common_functions import read_yaml_file


logger = get_logger(__name__)

class DataIngestion:
    def __init__(self, config_path: str = CONFIG_FILE_PATH):
        try:
            self.config = read_yaml_file(config_path)['data_ingestion']
            self.bucket_name = self.config['bucket_name']
            self.file_name = self.config['bucket_file_name']
            self.train_test_ratio = self.config['train_ratio']
        except Exception as e:
            logger.error("Error initializing DataIngestion")
            raise CustomException("Failed to initialize DataIngestion", sys)

        os.makedirs(RAW_DIR, exist_ok=True)

        logger.info(f"Data Ingestion started with bucket: {self.bucket_name}, file: {self.file_name}, train_test_ratio: {self.train_test_ratio}")

    #Function to download data from GCS
    def download_data(self):
        try:
            client = storage.Client()
            bucket = client.bucket(self.bucket_name)
            blob = bucket.blob(self.file_name)
            blob.download_to_filename(RAW_FILE_PATH)
            logger.info(f"Data downloaded successfully from bucket {self.bucket_name} to {RAW_FILE_PATH}")

        except Exception as e:
            logger.error(f"Error downloading data from GCS: {e}")
            raise CustomException("Failed to download data from GCS", sys)
    
    #Data splitting Function
    def split_data(self):
        try:
            logger.info("Starting the splitting process")
            data = pd.read_csv(RAW_FILE_PATH)

            train_data, test_data = train_test_split(data, test_size=1 - self.train_test_ratio, random_state=42)

            train_data.to_csv(TRAIN_FILE_PATH, index=False)
            test_data.to_csv(TEST_FILE_PATH, index=False)

            logger.info(f"Data split into train and test sets successfully. Train data at {TRAIN_FILE_PATH}, Test data at {TEST_FILE_PATH}")

        except Exception as e:
            logger.error("Error while splitting data")
            raise CustomException("Failed to split data", sys)
        
    
    def run_data_ingestion(self):
        try:
            logger.info("Starting Data Ingestion process")
            self.download_data()
            self.split_data()
            logger.info("Data Ingestion process completed successfully.")

        except CustomException as ce:
            logger.error(f"CustomException : {str(ce)}")

        finally:
            logger.info("Data Ingestion completely.")


if __name__ == "__main__":
    data_ingestion = DataIngestion(CONFIG_FILE_PATH)
    data_ingestion.run_data_ingestion()
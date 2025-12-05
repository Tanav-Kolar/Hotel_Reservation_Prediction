import os 

############################## DATA INGESTION ##############################

RAW_DIR = "artifacts/raw"
RAW_FILE_PATH = os.path.join(RAW_DIR, "raw_data.csv")
TRAIN_FILE_PATH = os.path.join(RAW_DIR, "train_data.csv")
TEST_FILE_PATH = os.path.join(RAW_DIR, "test_data.csv")

CONFIG_FILE_PATH = "config/config.yaml"
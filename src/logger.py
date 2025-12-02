import logging
import os
from datetime import datetime

LOGS_DIR = "logs"

os.makedirs(LOGS_DIR, exist_ok=True)

current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_file_path = os.path.join(LOGS_DIR, f"log_{current_time}.log")

logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_logger(name: str) -> logging.Logger:
    """Returns a logger instance with the specified name."""
    logger =  logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger
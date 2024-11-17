import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # Created a log file with this name
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)     # Message format ([2024-11-16 22:29:37,359] 18 root - INFO - Logging has started)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)

# if __name__ == "__main__":
#     logging.info("Logging has started")
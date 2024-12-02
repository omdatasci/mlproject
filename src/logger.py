# This code sets up a logging mechanism in Python to log events and errors to a dynamically created log file. 

import logging  # Provides functions and classes for managing log messages.
import os # Helps interact with the file system, including file and directory creation.
from datetime import datetime # Used to generate a timestamp for naming the log file uniquely.

# Creates a unique filename for the log file using the current date and time.
# strftime('%m_%d_%Y_%H_%M_%S'): Formats the date and time as MM_DD_YYYY_HH_MM_SS.
# If the current date is November 16, 2024, and the time is 10:29:37 PM, the filename would be: 11_16_2024_22_29_37.log
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  

# Defines the path where the log file will be stored.
# os.getcwd(): Gets the current working directory.
# os.path.join(): Combines the current directory, a subdirectory named 'logs', and the log filename.
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)   

# Ensures that the 'logs' directory exists in the current working directory.
# os.makedirs(): Creates the directory if it doesn’t already exist
# The exist_ok=True flag prevents errors if the directory already exists.
os.makedirs(logs_path,exist_ok=True)

# Define the Full Log File Path
# Combines the directory path (logs_path) with the log file name (LOG_FILE) to create the full path for the log file.
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configures how and where log messages will be stored.
# filename=LOG_FILE_PATH: Specifies the log file where messages will be written.
# format: Defines the structure of log messages
# %(asctime)s: Timestamp when the log entry was created.
# %(lineno)d: Line number in the code where the log entry was generated.
# %(name)s: Logger’s name.
# %(levelname)s: Log level (e.g., INFO, ERROR, DEBUG).
# %(message)s: The log message.
# level=logging.INFO: Sets the logging level to INFO, meaning all messages at INFO level or higher (e.g., WARNING, ERROR) will be logged.

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s", # Message format ([2024-11-16 22:29:37,359] 18 root - INFO - Logging has started)
    level = logging.INFO
)

# This is useful for testing of code to check logger file is working properly
# if __name__ == "__main__":
#     logging.info("Logging has started")
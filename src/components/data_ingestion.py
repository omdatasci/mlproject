# This file is used to read data from different sources
# This script automates the process of reading raw data, splitting it into training and testing sets, and saving these datasets to specified paths.
# It uses robust logging and exception handling to ensure smooth execution and easy debugging.

import os
import sys
from src.exception import CustomException  # importing exception from src folder. Custom exception handling class.
from src.logger import logging  # importing logger from src folder. Logging utility for tracking the program's execution.

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass # Used to define simple classes to store configurations.

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

# from src.components.model_trainer import ModelTrainerConfig
# from src.components.model_trainer import ModelTrainer

# This class holds the configuration details for paths where the data files will be stored.
@dataclass
class DataIngestionConfig:     # Any required input will be pass through this class
    # File path where the training data will be saved
    train_data_path: str=os.path.join('artifacts','train.csv') # Training data will be stored in artifacts folder and the file name is train.csv
    # File path where the testing data will be saved
    test_data_path: str=os.path.join('artifacts','test.csv') # Testing data will be stored in artifacts folder and the file name is test.csv
    # File path where the raw data will be saved 
    raw_data_path: str=os.path.join('artifacts','data.csv') # raw data will be stored in artifacts folder and the file name is train.csv

class DataIngestion:
    # Initializes an instance of the DataIngestionConfig class and stores the configuration in self.ingestion_config.
    def __init__(self):
        self.ingestion_config=DataIngestionConfig() # Above 3 paths will be saved in this class variable

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            df = pd.read_csv('notebook\data\stud.csv') # Reads the raw dataset (stud.csv) into a pandas DataFrame (df).
            logging.info('Read the dataset as dataframe')

            # os.path.dirname: Extracts the directory path from self.ingestion_config.train_data_path (i.e., artifacts/).
            # os.makedirs: Creates the artifacts directory if it doesn't exist (exist_ok=True ensures no error if the directory already exists).
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Saves the raw dataset (df) to artifacts/data.csv with no index column and headers included.
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train test split initiated")
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            # Saves the training set to artifacts/train.csv
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            # Saves the testing set to artifacts/test.csv.
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is completed")

            # Returns the paths of the training and testing data files.
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)


#  Executes the initiate_data_ingestion method when the script is run directly.
if __name__ == "__main__":
    obj=DataIngestion()     # Creates an instance of DataIngestion.
    train_data,test_data = obj.initiate_data_ingestion() # Calls the initiate_data_ingestion method to start the data ingestion process.

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_data,test_data)
    





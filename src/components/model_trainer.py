import sys
import os
import numpy as np
import pandas as pd

from src.logger import logging
from src.exception import CustomException

from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from src.utils import evaluate_model
from src.utils import save_object
from dataclasses import dataclass

@dataclass
class ModelTrainerconfig:
    trained_model_file_path = os.path.join('artifacts', 'model.pkl')
    
class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerconfig()
    
    def initiate_model_training(self, train_array, test_array):
        try:
            logging.info('Split dependent and independent variables from train and test data')
            X_train, y_train, X_test, y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models = {
                'LinearRegression': LinearRegression(),
                'Lasso': Lasso(),
                'Ridge': Ridge(),
                'ElasticNet': ElasticNet(),
                'DecisionTree': DecisionTreeRegressor(),
                'RandomForest': RandomForestRegressor(),
                'KNN': KNeighborsRegressor()
            }

            model_report:dict = evaluate_model(X_train, y_train, X_test, y_test, models)
            print('\n================================')
            logging.info(f'Model Report : {model_report}')

            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            print(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')
            print('\n====================================================================================\n')
            logging.info(f'Best Model Found , Model Name : {best_model_name} , R2 Score : {best_model_score}')


            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj = best_model
            )

        except Exception as e:
            raise CustomException(e, sys)
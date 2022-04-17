from pandas import Series, DataFrame
from abc import ABC, abstractmethod, abstractclassmethod

@abstractclassmethod
class Regressor:
    """
    A Regression class
    """
    def __init__(self, x_train: DataFrame, x_valid: DataFrame, y_train: Series, y_valid: Series) -> None:
        self.x_train = x_train
        self.x_valid = x_valid
        self.y_train = y_train
        self.y_valid = y_valid
        self.random_state = 42

    @staticmethod
    def best_number_of_estimator(self) -> int:
        """Add some comment"""
        pass

    def score(self):
        """Add some comment"""
        pass

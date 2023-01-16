import pandas as pd
from pandas import DataFrame
from typing import List

from dataclasses import dataclass
from sklearn.neighbors import KNeighborsClassifier


@dataclass
class KNearestNeighbors:
    k: int
    df: DataFrame
    n_neighbors: int
    target: str
    predictors: List
    text_size: float = 0.2
    random_state: int = 42

    def split_train_test(self):
        X = self.df[self.predictors].values
        y = self.df[self.target].values

    def train(self):
        self.df
        pass

    def predict(self):
        pass

    def confusion_matrix(self):
        pass



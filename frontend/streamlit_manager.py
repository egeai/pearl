from typing import Union
# from pearl.preprocessing.base.normalize import Uniform
from pearl.preprocessing.base.normalize import Uniform

import pandas as pd
from pandas import DataFrame


class StreamlitPreparation:
    def __init__(self):
        self.raw_data_frame = None
        self.uniform = None

    def get_raw_df(self):
        return self.raw_data_frame

    def shape_of_df(self):
        return self.uniform.shape()

    def columns(self):
        return self.uniform.columns()

    def target_variable_distribution(self, target_variable):
        return self.uniform.distribution_of_target_variable(target_variable)

    def get_uniformed_df(self):
        return self.uniform.data_frame

    def load_data(self, loaded_csv_object: Union) -> DataFrame:
        self.raw_data_frame = pd.read_csv(loaded_csv_object)
        # initialize uniform object
        self.uniform = Uniform(self.raw_data_frame)
        return self.raw_data_frame

    def get_dist_of_target_var(self, target_variable):
        # return self.uniform.distribution_of_target_variable_for_graph(target_variable)
        return self.uniform.focus_on_left(target_variable)

    def uniform_column_names(self) -> DataFrame:
        return self.uniform.column_names()

    def uniform_categorical_columns(self) -> DataFrame:
        return self.uniform.categorical_columns()

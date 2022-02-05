from pandas import Series, DataFrame
from pearl.algorithms.base.regression import Regressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from fpdf import FPDF # https://towardsdatascience.com/creating-pdf-files-with-python-ad3ccadfae0f
# https://github.com/yashprakash13/data-another-day


class RandomForest(Regressor):
    def __init__(self, x_train: DataFrame, x_valid: DataFrame, y_train: Series, y_valid: Series):
        super().__init__(x_train, x_valid, y_train, y_valid)

    def __repr__(self):
        # return f'RandomForest({self.number!r}, {self.manufacturer!r}, {self.resistance!r})'
        return 'RandomForest(*{!r})'.format(self.x_train)

    @staticmethod
    def best_number_of_estimator(self) -> int:
        return 10

    def score(self):
        n_estimators = self.best_number_of_estimator
        model = RandomForestRegressor(
            n_estimators=n_estimators,
            random_state=self.random_state
        )
        model.fit(self.x_train, self.y_train)
        predictions = model.predict(self.x_valid)
        return mean_absolute_error(self.y_valid, predictions)

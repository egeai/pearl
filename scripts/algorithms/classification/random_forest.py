from pandas import Series, DataFrame
from scripts.algorithms.base.regression import Regressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


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

    # KISA KODLAR:

    # Count the unique values in 'bad_conditions' and sort the index
    ## print(weather.bad_conditions.value_counts().sort_index())
    # Convert the 'bad_conditions' integers to strings using the 'mapping'
    ## weather['rating'] = weather.bad_conditions.map(mapping)

    # SelectingaDataFrameslice
    ## temp = weather.loc[:, 'TAVG':'TMAX']

    # Sum rows, not columns!!!
    ## temp.sum(axis='columns').head()

    ## mapping = {'0-15 Min':'short','16-30 Min':'medium','30+ Min':'long'}
    # ri['stop_length'] = ri.stop_duration.map(mapping)
    # ri.stop_length.dtype
    # out: dtype('O')

    # Changing data type from object to category
    ## cats = ['short', 'medium', 'long']
    ## ri['stop_length'] = ri.stop_length.astype('category',
    #                                             ordered=True,
    #                                             categories=cats)

    # CategoricalDtype
    # Specify the logical order of the weather ratings
    ## cats = pd.CategoricalDtype(['good', 'bad', 'worse'], ordered=True)

    # Change the data type of 'rating' to category
    ## weather['rating'] = weather.rating.astype(cats)

    # find upper Temperature values of  Temperature column by using loc
    ## temp_fah = temperatures.loc[temperatures['Temperature'] > 40, 'Temperature']
    # convert fahreneit to celcius and reasign the value which are above 40
    ## temp_cels = (temp_fah -32) * (5/9)
    ## temperatures.loc[temperatures['Temperature'] > 40, 'Temperature'] = temp_cels
    # Assert conversion is correct
    ## assert temperatures['Temperature'].max() < 40

    # Treating date data
    ## birtdays['Birthday'] = pd.to_datetime(birthdays['Birthday'],
    #                                       # Attepmt to infer format of each date
    #                                       infer_datetime_format=True
    #                                       # Return NA for rows where conversion failed
    #                                       errors='coerce')

    # birtdays['Birthday'] = birtdays['Birthday'].dt.strftime("%d-%m-%Y")

    # Convert acct_amount where it is in euro to dollars
    ## banking.loc[banking['acct_cur']=='euro', 'acct_amount'] = banking.loc[banking['acct_cur'] == 'euro', 'acct_amount'] * 1.1



# Import imputer module
## from sklearn.impute import SimpleImputer

# Subset numeric features: numeric_cols
## numeric_cols = loan_data.select_dtypes(include=[np.number])

# Impute with mean
## imp_mean = SimpleImputer(strategy='mean')
## loans_imp_mean = imp_mean.fit_transform(numeric_cols)

# Convert returned array to DataFrame
## loans_imp_meanDF = pd.DataFrame(loans_imp_mean, columns=numeric_cols.columns)

# Check the DataFrame's info
## print(loans_imp_meanDF.info())



# LASSO REGRESSION
# Import modules
## from sklearn.linear_model import Lasso, LassoCV
## from sklearn.metrics import mean_squared_error

# Train/test split
## X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=123, test_size=0.3)

# Instantiate cross-validated lasso, fit
##lasso_cv = LassoCV(alphas=None, cv=10, max_iter=10000)
## lasso_cv.fit(X_train, y_train)

# Instantiate lasso, fit, predict and print MSE
## lasso = Lasso(alpha = lasso_cv.alpha_)
## lasso.fit(X_train, y_train)
## print(mean_squared_error(y_true=y_test, y_pred=lasso.predict(X_test)))

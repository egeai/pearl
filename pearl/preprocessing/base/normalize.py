from pandas import DataFrame


class Uniform:
    """
    Basic preprocessing stage to normalize data by uniform them.
    """

    def __init__(self, df: DataFrame):
        self.data_frame = df

    def shape(self):
        return self.data_frame.shape

    def columns(self):
        return self.data_frame.columns

    def column_names(self) -> DataFrame:
        """
        Normalize the column names by
        replacing all spaces with underscores
        and all letters with lowercase letters.
        :return: normalized column names
        """
        self.data_frame.columns = self.data_frame.columns.str.lower().str.replace(' ', '_')
        return self.data_frame

    def categorical_columns(self) -> DataFrame:
        """
        The columns which are object type are assumed as categorical data.
        To uniform the content of the columns which are object type,
        replace all spaces with underscores,
        and all letters with lowercase letters.
        :return: normalized categorical columns
        """
        object_columns = list(
            self.data_frame.dtypes[
                self.data_frame.dtypes == 'object'
                ].index
        )
        for column in object_columns:
            self.data_frame[column] = self.data_frame[column].str.lower().str.replace(' ', '_')

        return self.data_frame

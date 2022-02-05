from pandas import DataFrame


class Uniform:
    """
    Basic preprocessing stage which is normalization
    """

    def __init__(self, df: DataFrame):
        self.data_frame = df

    def uniform_column_names(self):
        """
        Normalize the column names by
        replacing all spaces with underscores
        and all letters with lowercase letters.
        :return: normalized column names
        """
        return self.data_frame.columns.str.lower().str.replace(' ', '_')

    def uniform_categorical_columns(self) -> DataFrame:
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
            self.data_frame[column].str.lower().str.replace(' ', '_')

        return self.data_frame

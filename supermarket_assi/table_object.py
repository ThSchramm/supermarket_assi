import pandas


class TableObject:
    """
    Defines an Service-Class of one Table to execute the CRUD operations
    for this table.

    """

    def __init__(self, file_name):
        self.file_name = file_name
        self.dataframe = pandas.DataFrame()
        self.first_read = False

    def read_resource(self):
        """
        Loads the source excel-table to the pandas dateaframe of the object
        """
        path = './data/' + self.file_name + '.xlsx'
        try:
            if not self.first_read:
                self.dataframe = pandas.read_excel(path)
                self.dataframe.rename(columns=self.dataframe.iloc[0])
        except:
            return False

        return not self.dataframe.empty

    def get_data(self):
        """
        Returns the dataframe of the table object.
        :return dataframe: Pandas dataframe of rode table
        """
        return self.dataframe

    def get_filename(self):
        """
        Returns the filename of the source table.
        :return file_name: Name of Table-Resource
        """
        return self.file_name

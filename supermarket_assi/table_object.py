
import pandas

class TableObject:
    """
    Defines an Service-Class of one Table to execute the CRUD operations
    for this table.

    """

    def __init__(self, file_name):
        self.file_name = file_name
        self.dataframe = pandas.DataFrame()

    def read_resource(self):
        """

        :param xyz: xyz
        """
        path = './data/' + self.file_name + '.xlsx'
        self.dataframe = pandas.read_excel(path)

    def get_data(self):
        """

        :return dataframe: Pandas dataframe of rode table
        """
        return self.dataframe
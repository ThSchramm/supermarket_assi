# -*- coding: utf-8 -*-

import tkinter
import pandas
import table_object


if __name__ == "__main__":
    """
    This is the main program to interact as gui with an user
    """

    # Initialization
    products = table_object.TableObject(file_name='products')
    products_df = pandas.DataFrame()

    groups = table_object.TableObject(file_name='groups')
    groups_df = pandas.DataFrame()

    # Read all resources
    if products.read_resource():
        products_df = products.get_data()
    else:
        print('Fehler beim Lesen der Tabelle: ' + products.get_filename())

    if groups.read_resource():
        groups_df = groups.get_data()
    else:
        print('Fehler beim Lesen der Tabelle: ' + groups.get_filename())

    # Test
    print(products_df)
    print(groups_df)

    # Create the maingui, this is the first parent widget
    #
    # maingui = tkinter.Tk()
    # maingui.title("Einkaufsliste")

    # Label as child- of parent-widget maingui
    # w = tkinter.Label(maingui, text="Einkaufsliste")

    # The label widget will be embetted to maingui with pack-function
    # w.pack()

    # maingui.mainloop()

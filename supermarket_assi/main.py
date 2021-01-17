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
    products_df = products_df.drop(columns=['Unit'])
    print(products_df)
    # print(groups_df)

    # Create the maingui(root window), this is the first parent widget

    maingui = tkinter.Tk()
    maingui.title("Einkaufsliste")

    # Print product list at maingui as gui_table

    # create listbox object
    gui_products = tkinter.Listbox(maingui,
                                   height=10,
                                   width=15,
                                   bg="grey",
                                   activestyle='dotbox',
                                   font="Helvetica",
                                   fg="yellow")

    # Define the size of the window.
    maingui.geometry("300x250")

    # Define a label for the list.
    label = tkinter.Label(maingui, text="Produkte")

    # insert elements by their index and names.
    for i in range(len(products_df['Product'].tolist())):
        gui_products.insert(i, str(products_df['Product'].tolist()[i]))

    # Label as child- of parent-widget maingui
    # pack the widgets
    label.pack()
    gui_products.pack()


    maingui.mainloop()

# -*- coding: utf-8 -*-

import tkinter
import pandas
import table_object


# Functions
# ----------------------------------------------------------------------------------


def init_data():
    """

    :return:
    """
    # Read all resources


def init_dataframe(table_object):
    """

    :param table_object:
    :return: lcl_dataframe
    """
    lcl_dataframe = pandas.DataFrame()
    if table_object.read_resource():
        lcl_dataframe = table_object.get_data()
    else:
        print('Fehler beim Lesen der Tabelle: ' + table_object.get_filename())

    return lcl_dataframe


def init_gui(gui):
    """

    :param gui:
    :return: gui:
    """

    # Title of the window
    gui.title("Einkaufsliste")
    # Define the size of the window.
    gui.geometry('1000x500')

    return gui


def selection():
    """

    :return:
    """

    print(gui_products.curselection())
    aktuell_ausgewaehlt = gui_products.curselection()
    textausgabe = tkinter.Label(gbl_maingui, text=aktuell_ausgewaehlt, bg="orange")
    textausgabe.place(x=25, y=200)


if __name__ == "__main__":
    """
    This is the main program to interact as gui with an user
    """

    # Global variables
    # ----------------------------------------------------------------------------------

    # Data objects
    gbl_products = table_object.TableObject(file_name='products')
    gbl_products_df = init_dataframe(gbl_products)

    gbl_groups = table_object.TableObject(file_name='groups')
    gbl_groups_df = init_dataframe(gbl_groups)

    # Create the maingui(root window), this is the first parent widget
    gbl_maingui = tkinter.Tk()

    # Initialization of the gui
    gbl_maingui = init_gui(gui=gbl_maingui)

    # Test
    # products_df = products_df.drop(columns=['Unit'])
    # print(products_df)
    # print(groups_df)

    # create listbox object
    gui_products = tkinter.Listbox(gbl_maingui,
                                   height=50,
                                   width=20,
                                   bg='grey',
                                   activestyle='dotbox',
                                   font='Arial',
                                   fg='yellow')

    # insert elements by their index and names.
    for i in range(len(gbl_products_df['Product'].tolist())):
        gui_products.insert(i, str(gbl_products_df['Product'].tolist()[i]))

    gui_products["selectmode"] = "extended"  # ToDo notwendig?
    gui_products.pack()  # Label as child of parent-widget

    # Define a label for the list.
    label = tkinter.Label(gbl_maingui, text="Produkte")
    label.pack()  # Label as child of parent-widget

    # Define a button for selection
    button_select = tkinter.Button(gbl_maingui,
                                   text="Zur Liste hinzufügen",
                                   command=selection)
    button_select.place(x=25, y=100)

    # Label as child- of parent-widget maingui
    # pack the widgets

    # Start the maingui
    gbl_maingui.mainloop()

from tkinter import *
from tkinter import messagebox
from library import *


def saveSystem(window):
    if messagebox.askokcancel("Saving",
                              "Do you wish to save the data stored in the System?"
                              "\nWARNING: Data will be overwritten!",
                              parent=window):
        saveAll()


def loadSystem(window):
    if messagebox.askokcancel("Opening",
                              "Do you wish to load the data for the System?"
                              "\nWARNING: Data will be overwritten!",
                              parent=window):
        loadAll()


def infoWindow(window):
    messagebox.showinfo("Information",
                        "System Version 20/03/2017\n"
                        "Developed by N0t0rius\n\n"
                        "Status : Incomplete",
                        parent=window)


def newSystem(window):
    if messagebox.askokcancel("Creating",
                              "Do you wish to create a new System from scratch?"
                              "\nWARNING: Data will be overwritten!",
                              parent=window):
        newData()

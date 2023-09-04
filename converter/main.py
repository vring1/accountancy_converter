from raw_data_handler import raw_data_handler
from main_data_handler import main_data_handler
from fetch_and_read_file import fetch_and_read_file
from excel_handler import excel_handler
import tkinter as tk

from raw_data_handler import raw_data_handler
from main_data_handler import main_data_handler
from fetch_and_read_file import fetch_and_read_file
from excel_handler import excel_handler
import tkinter as tk


class MyGUI:
    def __init__(self):
        # initializing window
        self.window = tk.Tk()
        self.window.geometry('400x400')
        self.window.title('Regnskabsconverter')

        # variables to store user input
        self.year = tk.IntVar(value=2023)
        self.months = [tk.BooleanVar(value=False) for _ in range(12)]
        self.fetch_file_from_danske_bank = tk.BooleanVar(value=False)
        self.mitID = tk.StringVar()
        self.cpr = tk.StringVar()
        self.select_all = tk.BooleanVar(value=False)

        # labels, entry widgets, and check buttons to get user input
        tk.Label(self.window, text="Year:").grid(row=0, column=0)
        tk.Entry(self.window, textvariable=self.year).grid(row=0, column=1)

        tk.Label(self.window, text="Months:").grid(row=1, column=0)
        for i in range(12):
            tk.Checkbutton(self.window, text=str(
                i+1), variable=self.months[i]).grid(row=1+i//3, column=i % 3+1)

        tk.Checkbutton(self.window, text="Select All", variable=self.select_all,
                       command=self.select_all_months).grid(row=5, column=1)

        tk.Checkbutton(self.window, text="Fetch file from Danske Bank",
                       variable=self.fetch_file_from_danske_bank).grid(row=6, column=0, columnspan=2)

        tk.Label(self.window, text="MitID:").grid(row=7, column=0)
        tk.Entry(self.window, textvariable=self.mitID).grid(row=7, column=1)

        tk.Label(self.window, text="CPR:").grid(row=8, column=0)
        tk.Entry(self.window, textvariable=self.cpr).grid(row=8, column=1)

        # "OK" button to execute 'okay' method
        tk.Button(self.window, text="OK", command=self.okay).grid(
            row=9, column=0, columnspan=2)

        # starting the GUI main loop
        self.window.mainloop()

    def okay(self):
        # retrieving the values of variables from the GUI
        year = self.year.get()
        months = [i+1 for i,
                  checked in enumerate(self.months) if checked.get()]
        fetch_file_from_danske_bank = self.fetch_file_from_danske_bank.get()
        mitID = self.mitID.get()
        cpr = self.cpr.get()

        # handling raw data and getting dataframe
        raw_data_dataframe = raw_data_handler.handle_raw_data(
            months, year, fetch_file_from_danske_bank, cpr, mitID)[0]
        
        # handling main data and getting dataframe
        main_data_dataframe = main_data_handler.handle_main_data(months, year)

        # creating an excel file with the processed data
        excel_handler.create_excel_file(
            months, year, raw_data_dataframe, main_data_dataframe)

        # exit application and quit window
        self.window.destroy()

    def select_all_months(self):
        # check if the "Select All" check button is checked (true)
        if self.select_all.get():
            # if checked, set all month variables to true
            for var in self.months:
                var.set(True)
        else:
            # if unchecked, set all month variables to false
            for var in self.months:
                var.set(False)


if __name__ == "__main__":
    gui = MyGUI()

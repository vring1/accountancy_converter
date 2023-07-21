import os
import pandas as pd
from get_csv_file import get_csv_file_from_danske_bank


class fetch_and_read_file:
    # find the latest modified .csv file in a directory containing a specific substring
    def latest_modified_csvfile_containing_specific_substring(directory, substring):
        latest_file = None
        latest_mod_time = 0
        for file in os.listdir(directory):
            if substring and ".csv" in file:
                # get file path
                file_path = os.path.join(directory, file)
                # get the file's modification time
                mod_time = os.path.getmtime(file_path)
                if mod_time > latest_mod_time:
                    # make sure we get the file with the latest modification time
                    latest_mod_time = mod_time
                    latest_file = file_path
        return latest_file


    def fetch_and_read_file(get_file,cpr,mitID):
        if get_file:
            # if the user wants to fetch .csv file from danske bank
            get_csv_file_from_danske_bank.get_csv_file_from_danske_bank(
                mitID, cpr)

        # get directory for Downloads
        user_home = os.path.expanduser("~")
        directory = os.path.join(user_home, "Downloads")

        # find the latest modified file containing 'DanskeKonto' in the Downloads folder
        file_path = fetch_and_read_file.latest_modified_csvfile_containing_specific_substring(
            directory, 'DanskeKonto')

        # read the data from the .csv file into pandas dataframe
        data = pd.read_csv(file_path, delimiter=';', encoding='ISO-8859-1')

        return data

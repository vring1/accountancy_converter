import os
import pandas as pd
from get_csv_file import get_csv_file_from_danske_bank


class fetch_and_read_file:
    def latest_modified_file_containing_specific_substring(directory, substring):
        latest_file = None
        latest_mod_time = 0
        for file in os.listdir(directory):
            if substring and ".csv" in file:
                file_path = os.path.join(directory, file)
                mod_time = os.path.getmtime(file_path)
                if mod_time > latest_mod_time:
                    latest_mod_time = mod_time
                    latest_file = file_path
        return latest_file

    def fetch_and_read_file(hent_fil,cpr,mitID):
        if hent_fil:
            get_csv_file_from_danske_bank.get_csv_file_from_danske_bank(
                mitID, cpr)

        user_home = os.path.expanduser("~")
        directory = os.path.join(user_home, "Downloads")

        file_path = fetch_and_read_file.latest_modified_file_containing_specific_substring(
            directory, 'DanskeKonto')

        data = pd.read_csv(file_path, delimiter=';', encoding='ISO-8859-1')

        return data

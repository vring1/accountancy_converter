import pandas as pd
from fetch_and_read_file import fetch_and_read_file
import numpy as np


class raw_data_handler:
    # handle data displayed on 'Data' sheet

    def get_right_dates(month, year, fetch_check, cpr, mitID):
        i = 0 # initialize counter

        # read data into pandas dataframe
        df1 = pd.DataFrame(
            fetch_and_read_file.fetch_and_read_file(fetch_check, cpr, mitID))
        
        # create an empty dataframe to store the filtered data for the specified months
        actual_data = pd.DataFrame(columns=df1.columns)
        for months in month:
            # for each month, convert the month number to a string format with leading zeros if needed
            strmonth = str(
                month[i]) if month[i] > 9 else "0%d" % (month[i])
            
            # calculate the last month and year.
            lastmonth = month[i] - 1 if month[i] > 1 else 12
            strlastmonth = str(
                lastmonth) if lastmonth > 9 else "0%d" % (lastmonth)
            lastyear = year-1

            # two lists with the days from last month and this month, which are the days needed for each month
            days_last_month = list(range(28, 32))
            days_this_month = list(range(1, 28))

            # for each day in last month >= 28, filter the rows with the current date from the dataframe and append them to 'actual_data'
            for day in days_last_month:
                date = "%d.%s.%d" % (
                    day, strlastmonth, year if lastmonth != 12 else lastyear)
                temp_df = df1.loc[df1["Dato"] == date]
                actual_data = pd.concat(
                    [actual_data, temp_df], ignore_index=True)
                
            # for each day in this month < 28, filter the rows with the current date from the dataframe and append them to 'actual_data'
            for day in days_this_month:
                if (day > 0 and day < 10):
                    date = "0%d.%s.%d" % (day, strmonth, year)
                elif (day > 9 and day < 28):
                    date = "%d.%s.%d" % (day, strmonth, year)
                temp_df = df1.loc[df1["Dato"] == date]
                actual_data = pd.concat(
                    [actual_data, temp_df], ignore_index=True)
                
            # increment counter for next month
            i += 1

        return actual_data


    def handle_raw_data(month, year, fetch_check, cpr, mitID):
        # get the relevant data by calling the 'get_right_dates' function on input (month, year, fetch or not...)
        relevant_data = raw_data_handler.get_right_dates(
            month, year, fetch_check, cpr, mitID)
        
        # loop through the columns of 'relevant_data' to extract specific categories of data
        for column in relevant_data.columns:
            if (column == "Bel�b" or column == "Beløb"):
                beloeber = relevant_data[column]
            if (column == "Tekst"):
                tekster = relevant_data[column]
            if (column == "Saldo"):
                saldos = relevant_data[column]
            if (column == "Dato"):
                datoer = relevant_data[column]

        # initialize arrays to store data with proper size
        dato_med_rigtig_størrelse = np.empty(800, dtype=object)
        saldo_med_rigtig_størrelse = np.empty(800, dtype=object)

        # process the data for 'datoer' and 'saldos'
        p = 0
        for saldo in saldos:
            saldo_med_rigtig_størrelse[p] = saldos[p]
            dato_med_rigtig_størrelse[p] = datoer[p]
            p += 1

        # store the last value of the 'saldo_med_rigtig_størrelse' array in 'senesteSaldo'
        senesteSaldo = np.empty(800, dtype=object)
        senesteSaldo[0] = saldo_med_rigtig_størrelse[p-1]

        # convert the dates in 'dato_med_rigtig_størrelse' array to the right format
        t = 0
        for dato in dato_med_rigtig_størrelse:
            dato_med_rigtig_størrelse[t] = str(dato).replace('.', '/')
            t += 1

        # initialize arrays to store data for specific categories
        mobilePay = np.empty(800, dtype=object)
        indkoeb = np.empty(800, dtype=object)
        løn = np.empty(800, dtype=object)
        su = np.empty(800, dtype=object)
        resterende = np.empty(800, dtype=object)
        husleje = np.empty(800, dtype=object)
        huslejefraanna = np.empty(800, dtype=object)
        fastfood = np.empty(800, dtype=object)
        boligstøtte = np.empty(800, dtype=object)
        fisOgBallade = np.empty(800, dtype=object)
        el = np.empty(800, dtype=object)
        internet = np.empty(800, dtype=object)

        # initialize a counter for the loop through 'tekster' array
        y = -1
        # loop through the 'tekster' array and categorize the data based on the text
        for text in tekster:
            y += 1
            if "Anna Lisa" in text:
                if beloeber[y] == '1.000,00':
                    huslejefraanna[y] = beloeber[y]
                else:
                    mobilePay[y] = beloeber[y]
            elif "Andel Energi" in text:
                el[y] = beloeber[y]
            elif "Fibia" in text:
                internet[y] = beloeber[y]
            elif "MobilePay" in text:
                mobilePay[y] = beloeber[y]
            elif "WeShare" in text:
                mobilePay[y] = beloeber[y]
            elif "NETTO" in text:
                indkoeb[y] = beloeber[y]
            elif "Netto" in text:
                indkoeb[y] = beloeber[y]
            elif "Superbrugsen" in text:
                indkoeb[y] = beloeber[y]
            elif "F@TEX" in text:
                indkoeb[y] = beloeber[y]
            elif "Foetex" in text:
                indkoeb[y] = beloeber[y]
            elif "NORMAL" in text:
                indkoeb[y] = beloeber[y]
            elif "Rema" in text:
                indkoeb[y] = beloeber[y]
            elif "REMA" in text:
                indkoeb[y] = beloeber[y]
            elif "Apote" in text:
                indkoeb[y] = beloeber[y]
            elif "L�noverf�rsel" in text:
                løn[y] = beloeber[y]
            elif "Lønoverførsel" in text:
                løn[y] = beloeber[y]
            elif "LØNOVERFØRSEL" in text:
                løn[y] = beloeber[y]
            elif "SU" in text:
                su[y] = beloeber[y]
            elif "Husleje" in text:
                husleje[y] = beloeber[y]
            elif "Wolt" in text:
                fastfood[y] = beloeber[y]
            elif "Pizza" in text:
                fastfood[y] = beloeber[y]
            elif "Boligst�tte" in text:
                boligstøtte[y] = beloeber[y]
            elif "Boligstøtte" in text:
                boligstøtte[y] = beloeber[y]
            elif "Nexus" in text:
                fisOgBallade[y] = beloeber[y]
            elif "Steam" in text:
                fisOgBallade[y] = beloeber[y]
            elif "7-11" in text:
                fastfood[y] = beloeber[y]
            elif "Foreningen" in text:
                fisOgBallade[y] = beloeber[y]
            elif "STEAM" in text:
                fisOgBallade[y] = beloeber[y]
            else:
                resterende[y] = beloeber[y]

        # create a new dataframe 'df1' to store processed data
        df1 = pd.DataFrame({'Dato': dato_med_rigtig_størrelse,
                            'SU': su,
                            'Løn': løn,
                            'Boligstøtte': boligstøtte,
                            'El': el,
                            'Internet': internet,
                            'Husleje': husleje,
                            'Husleje fra Anna': huslejefraanna,
                            'Seneste saldo': senesteSaldo,
                            'Saldoer': saldo_med_rigtig_størrelse,
                            'MobilePay': mobilePay,
                            'Indkøb': indkoeb,
                            'Fastfood': fastfood,
                            'Fis og ballade': fisOgBallade,
                            'Resterende': resterende})
        
        # return a list containing 'df1' and arrays for some specific data (data that is used in the main_data_handler.py)
        return [df1, resterende, fisOgBallade, fastfood, indkoeb, mobilePay, senesteSaldo]

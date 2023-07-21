import os
import pandas as pd
import xlsxwriter

# labels for the 'Nøgletal' sheet
labels = ["", "Forskel i udgift/indtægt hver måned", "Penge på konto", "", "", "Indtægt i alt", "SU", "Løn", "Boligstøtte", "Husleje fra Anna", "",
          "Udgifter tilpasset ift. kontobevægelser", "", "Faste udgifter sum", "Husleje", "El", "Internet", "", "", "Alle andre kontobevægelser"]

class excel_handler:
    def create_excel_file(month, year, df1, df2):
        if len(month) == 12: 
            # all months have been chosen, therefore an annual report
            excelname = f"Regnskab-{year}.xlsx" 
        else: 
            # else all the months chosen will appear in the excel file name
            excelname = f"Regnskab-{year}_month{month}.xlsx" 
        if os.path.exists(excelname):
            # overwrite existing accounting file
            os.remove(excelname)

        # create excelwriter and sheets
        writer = pd.ExcelWriter(excelname, engine='xlsxwriter')
        df2.to_excel(writer, sheet_name="Nøgletal", index=False)
        df1.to_excel(writer, sheet_name="Data", index=False)

        # create a format for using bold text
        workbook = writer.book
        bold_format = workbook.add_format({'bold': True})

        # set active sheet
        worksheet = writer.sheets['Nøgletal']
        
        # set specific labels to bold
        for i in range(len(labels)):
            if labels[i] == 'Indtægt i alt' or labels[i] == 'Forskel i udgift/indtægt hver måned' or labels[i] == 'Penge på konto' or labels[i] == 'Udgifter tilpasset ift. kontobevægelser' or labels[i] == 'Faste udgifter sum' or labels[i] == 'Alle andre kontobevægelser':
                worksheet.write(i+1, 0, labels[i], bold_format)

        # loop through the columns of df2 to set appropriate column widths based on data length.
        for column in df2:
            column_length = max(df2[column].astype(str).map(len).max(), len(column))
            col_idx = df2.columns.get_loc(column)
            worksheet.set_column(col_idx, col_idx, column_length)

        # save excel file
        writer.save()

import os
import pandas as pd
import xlsxwriter

labels = ["", "Forskel i udgift/indtægt hver måned", "Penge på konto", "", "", "Indtægt i alt", "SU", "Løn", "Boligstøtte", "Husleje fra Anna", "",
          "Udgifter tilpasset ift. kontobevægelser", "", "Faste udgifter sum", "Husleje", "El", "Internet", "", "", "Alle andre kontobevægelser"]

class excel_handler:
    def create_excel_file(month, year, df1, df2):
        if len(month) == 12:
            excelname = f"Regnskab-{year}.xlsx"
        else:
            excelname = f"Regnskab-{year}_month{month}.xlsx"
        #print(os.path.exists(excelname))
        if os.path.exists(excelname):
            os.remove(excelname)
        writer = pd.ExcelWriter(excelname, engine='xlsxwriter')
        df2.to_excel(writer, sheet_name="Nøgletal", index=False)
        df1.to_excel(writer, sheet_name="Data", index=False)

        workbook = writer.book
        bold_format = workbook.add_format({'bold': True})
        worksheet = writer.sheets['Nøgletal']
        
        #labels = ['Indtægt i alt', 'Forskel i udgift/indtægt hver måned', 'Penge på konto', 'Udgifter tilpasset ift. kontobevægelser', 'Faste udgifter sum', 'Alle andre kontobevægelser']
#
        #for i in range(len(labels)):
        #    if labels[i] in labels:
        #        worksheet.write(i+1, 0, labels[i], bold_format)

        for i in range(len(labels)):
            if labels[i] == 'Indtægt i alt' or labels[i] == 'Forskel i udgift/indtægt hver måned' or labels[i] == 'Penge på konto' or labels[i] == 'Udgifter tilpasset ift. kontobevægelser' or labels[i] == 'Faste udgifter sum' or labels[i] == 'Alle andre kontobevægelser':
                worksheet.write(i+1, 0, labels[i], bold_format)

        for column in df2:
            column_length = max(df2[column].astype(str).map(len).max(), len(column))
            col_idx = df2.columns.get_loc(column)
            worksheet.set_column(col_idx, col_idx, column_length)

        writer.save()

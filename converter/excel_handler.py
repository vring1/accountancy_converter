import os
import pandas as pd

labels = ["", "Forskel i udgift/indtægt hver måned", "Penge på konto", "", "", "Indtægt i alt", "SU", "Løn", "Boligstøtte", "Husleje fra Anna", "",
          "Udgifter tilpasset ift. kontobevægelser", "", "Faste udgifter sum", "Husleje", "El", "Internet", "", "", "Alle andre kontobevægelser"]


class excel_handler:
    def create_excel_file(month, year, df1, df2):
        if len(month) == 12:
            excelname = f"Regnskab-{year}.xlsx"
        else:
            excelname = f"Regnskab-{year}_month{month}.xlsx"
        if os.path.exists(excelname):
            os.remove(excelname)
        with pd.ExcelWriter(excelname) as writer:
            df2.to_excel(writer, sheet_name="Nøgletal", index=False)
            df1.to_excel(writer, sheet_name="Data", index=False)

            bold_font = writer.book.add_format({'bold': True})
            worksheet = writer.sheets['Nøgletal']

            for i in range(len(labels)):
                if labels[i] == 'Indtægt i alt' or labels[i] == 'Forskel i udgift/indtægt hver måned' or labels[i] == 'Penge på konto' or labels[i] == 'Udgifter tilpasset ift. kontobevægelser' or labels[i] == 'Faste udgifter sum' or labels[i] == 'Alle andre kontobevægelser':
                    worksheet.write(i+1, 0, labels[i], bold_font)
            for column in df2:
                column_length = max(df2[column].astype(
                    str).map(len).max(), len(column))
                col_idx = df2.columns.get_loc(column)
                writer.sheets['Nøgletal'].set_column(
                    col_idx, col_idx, column_length)

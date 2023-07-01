import pandas as pd
from raw_data_handler import raw_data_handler
import numpy as np


class main_data_handler:
    def handle_main_data(month, year):
        relevant_data = raw_data_handler.get_right_dates(
            month, year, False, None, None)
        raw_data = raw_data_handler.handle_raw_data(
            month, year, False, None, None)
        #resterende_total = raw_data_handler.handle_raw_data(month, year)[1]
        resterende_total = raw_data[1]
        fisOgBallade_total = raw_data[2]
        fastfood_total = raw_data[3]
        indkoeb_total = raw_data[4]
        mobilePay_total = raw_data[5]
        senesteSaldo = raw_data[6]
        january_data = relevant_data[(relevant_data['Dato'].str.contains('.01.') & ~(relevant_data['Dato'].str.contains('31.01.'))
                                      & ~(relevant_data['Dato'].str.contains('30.01.')) & ~(relevant_data['Dato'].str.contains('29.01.'))
                                      & ~(relevant_data['Dato'].str.contains('28.01.'))) | relevant_data['Dato'].str.contains('28.12.'+str(year-1))
                                     | relevant_data['Dato'].str.contains("29.12."+str(year-1))
                                     | relevant_data['Dato'].str.contains("30.12."+str(year-1)) | relevant_data['Dato'].str.contains("31.12."+str(year-1))]

        february_data = relevant_data[(relevant_data['Dato'].str.contains('.02.'+str(year)) & ~(relevant_data['Dato'].str.contains('31.02.'+str(year)))
                                       & ~(relevant_data['Dato'].str.contains('30.02.'+str(year))) & ~(relevant_data['Dato'].str.contains('29.02.'+str(year)))
                                       & ~(relevant_data['Dato'].str.contains('28.02.'+str(year)))) | relevant_data['Dato'].str.contains('28.01.'+str(year))
                                      | relevant_data['Dato'].str.contains("29.01."+str(year))
                                      | relevant_data['Dato'].str.contains("30.01."+str(year)) | relevant_data['Dato'].str.contains("31.01."+str(year))]

        march_data = relevant_data[(relevant_data['Dato'].str.contains('.03.'+str(year)) & ~(relevant_data['Dato'].str.contains('31.03.'+str(year)))
                                    & ~(relevant_data['Dato'].str.contains('30.03.'+str(year))) & ~(relevant_data['Dato'].str.contains('29.03.'+str(year)))
                                    & ~(relevant_data['Dato'].str.contains('28.03.'+str(year)))) | relevant_data['Dato'].str.contains('28.02.'+str(year))
                                   | relevant_data['Dato'].str.contains("29.02."+str(year))
                                   | relevant_data['Dato'].str.contains("30.02."+str(year)) | relevant_data['Dato'].str.contains("31.02."+str(year))]

        april_data = relevant_data[(relevant_data['Dato'].str.contains('.04.'+str(year)) & ~(relevant_data['Dato'].str.contains('31.04.'+str(year)))
                                    & ~(relevant_data['Dato'].str.contains('30.04.'+str(year))) & ~(relevant_data['Dato'].str.contains('29.04.'+str(year)))
                                    & ~(relevant_data['Dato'].str.contains('28.04.'+str(year)))) | relevant_data['Dato'].str.contains('28.03.'+str(year))
                                   | relevant_data['Dato'].str.contains("29.03."+str(year))
                                   | relevant_data['Dato'].str.contains("30.03."+str(year)) | relevant_data['Dato'].str.contains("31.03."+str(year))]

        may_data = relevant_data[(relevant_data['Dato'].str.contains('.05.'+str(year)) & ~(relevant_data['Dato'].str.contains('31.05.'+str(year)))
                                 & ~(relevant_data['Dato'].str.contains('30.05.'+str(year))) & ~(relevant_data['Dato'].str.contains('29.05.'+str(year)))
                                 & ~(relevant_data['Dato'].str.contains('28.05.'+str(year)))) | relevant_data['Dato'].str.contains('28.04.'+str(year))
                                 | relevant_data['Dato'].str.contains("29.04."+str(year))
                                 | relevant_data['Dato'].str.contains("30.04."+str(year)) | relevant_data['Dato'].str.contains("31.04."+str(year))]

        june_data = relevant_data[(relevant_data['Dato'].str.contains('.06.'+str(year)) & ~(relevant_data['Dato'].str.contains('31.06.'+str(year)))
                                   & ~(relevant_data['Dato'].str.contains('30.06.'+str(year))) & ~(relevant_data['Dato'].str.contains('29.06.'+str(year)))
                                   & ~(relevant_data['Dato'].str.contains('28.06.'+str(year)))) | relevant_data['Dato'].str.contains('28.05.'+str(year))
                                  | relevant_data['Dato'].str.contains("29.05."+str(year))
                                  | relevant_data['Dato'].str.contains("30.05."+str(year)) | relevant_data['Dato'].str.contains("31.05."+str(year))]

        july_data = relevant_data[(relevant_data['Dato'].str.contains('.07.'+str(year)) & ~(relevant_data['Dato'].str.contains('31.07.'+str(year)))
                                   & ~(relevant_data['Dato'].str.contains('30.07.'+str(year))) & ~(relevant_data['Dato'].str.contains('29.07.'+str(year)))
                                   & ~(relevant_data['Dato'].str.contains('28.07.'+str(year)))) | relevant_data['Dato'].str.contains('28.06.'+str(year))
                                  | relevant_data['Dato'].str.contains("29.06."+str(year))
                                  | relevant_data['Dato'].str.contains("30.06."+str(year)) | relevant_data['Dato'].str.contains("31.06."+str(year))]

        august_data = relevant_data[(relevant_data['Dato'].str.contains('.08.'+str(year)) & ~(relevant_data['Dato'].str.contains('31.08.'+str(year)))
                                     & ~(relevant_data['Dato'].str.contains('30.08.'+str(year))) & ~(relevant_data['Dato'].str.contains('29.08.'+str(year)))
                                     & ~(relevant_data['Dato'].str.contains('28.08.'+str(year)))) | relevant_data['Dato'].str.contains('28.07.'+str(year))
                                    | relevant_data['Dato'].str.contains("29.07."+str(year))
                                    | relevant_data['Dato'].str.contains("30.07."+str(year)) | relevant_data['Dato'].str.contains("31.07."+str(year))]

        september_data = relevant_data[(relevant_data['Dato'].str.contains('.09.'+str(year)) & ~(relevant_data['Dato'].str.contains('31.09.'+str(year)))
                                        & ~(relevant_data['Dato'].str.contains('30.09.'+str(year))) & ~(relevant_data['Dato'].str.contains('29.09.'+str(year)))
                                        & ~(relevant_data['Dato'].str.contains('28.09.'+str(year)))) | relevant_data['Dato'].str.contains('28.08.'+str(year))
                                       | relevant_data['Dato'].str.contains("29.08."+str(year))
                                       | relevant_data['Dato'].str.contains("30.08."+str(year)) | relevant_data['Dato'].str.contains("31.08."+str(year))]

        october_data = relevant_data[(relevant_data['Dato'].str.contains('.10.'+str(year)) & ~(relevant_data['Dato'].str.contains('31.10.'+str(year)))
                                      & ~(relevant_data['Dato'].str.contains('30.10.'+str(year))) & ~(relevant_data['Dato'].str.contains('29.10.'+str(year)))
                                      & ~(relevant_data['Dato'].str.contains('28.10.'+str(year)))) | relevant_data['Dato'].str.contains('28.09.'+str(year))
                                     | relevant_data['Dato'].str.contains("29.09."+str(year))
                                     | relevant_data['Dato'].str.contains("30.09."+str(year)) | relevant_data['Dato'].str.contains("31.09."+str(year))]

        november_data = relevant_data[(relevant_data['Dato'].str.contains('.11.'+str(year)) & ~(relevant_data['Dato'].str.contains('31.11.'+str(year)))
                                       & ~(relevant_data['Dato'].str.contains('30.11.'+str(year))) & ~(relevant_data['Dato'].str.contains('29.11.'+str(year)))
                                       & ~(relevant_data['Dato'].str.contains('28.11.'+str(year)))) | relevant_data['Dato'].str.contains('28.10.'+str(year))
                                      | relevant_data['Dato'].str.contains("29.10."+str(year))
                                      | relevant_data['Dato'].str.contains("30.10."+str(year)) | relevant_data['Dato'].str.contains("31.10."+str(year))]

        december_data = relevant_data[(relevant_data['Dato'].str.contains('.12.'+str(year)) & ~(relevant_data['Dato'].str.contains('31.12.'+str(year)))
                                       & ~(relevant_data['Dato'].str.contains('30.12.'+str(year))) & ~(relevant_data['Dato'].str.contains('29.12.'+str(year)))
                                       & ~(relevant_data['Dato'].str.contains('28.12.'+str(year)))) | relevant_data['Dato'].str.contains('28.11.'+str(year))
                                      | relevant_data['Dato'].str.contains("29.11."+str(year))
                                      | relevant_data['Dato'].str.contains("30.11."+str(year)) | relevant_data['Dato'].str.contains("31.11."+str(year))]
        data_fordelt_på_months = [january_data, february_data, march_data, april_data, may_data,
                                  june_data, july_data, august_data, september_data, october_data, november_data, december_data]

        jan = ["", "", "", "", "", "", "", "", "", "",
               "", "", "", "", "", "", "", "", "", ""]
        feb = ["", "", "", "", "", "", "", "", "", "",
               "", "", "", "", "", "", "", "", "", ""]
        mar = ["", "", "", "", "", "", "", "", "", "",
               "", "", "", "", "", "", "", "", "", ""]
        apr = ["", "", "", "", "", "", "", "", "", "",
               "", "", "", "", "", "", "", "", "", ""]
        maj = ["", "", "", "", "", "", "", "", "", "",
               "", "", "", "", "", "", "", "", "", ""]
        jun = ["", "", "", "", "", "", "", "", "", "",
               "", "", "", "", "", "", "", "", "", ""]
        jul = ["", "", "", "", "", "", "", "", "", "",
               "", "", "", "", "", "", "", "", "", ""]
        aug = ["", "", "", "", "", "", "", "", "", "",
               "", "", "", "", "", "", "", "", "", ""]
        sep = ["", "", "", "", "", "", "", "", "", "",
               "", "", "", "", "", "", "", "", "", ""]
        okt = ["", "", "", "", "", "", "", "", "", "",
               "", "", "", "", "", "", "", "", "", ""]
        nov = ["", "", "", "", "", "", "", "", "", "",
               "", "", "", "", "", "", "", "", "", ""]
        dec = ["", "", "", "", "", "", "", "", "", "",
               "", "", "", "", "", "", "", "", "", ""]

        mo = 0
        temp = 0
        for months in data_fordelt_på_months:
            for column in data_fordelt_på_months[mo].columns:
                if (column == "Bel�b" or column == "Beløb"):
                    per_month_beloeber = (data_fordelt_på_months[mo])[column]
                if (column == "Tekst"):
                    per_month_tekster = (data_fordelt_på_months[mo])[column]
                if (column == "Saldo"):
                    per_month_saldos = (data_fordelt_på_months[mo])[column]
                if (column == "Dato"):
                    per_month_datoer = (data_fordelt_på_months[mo])[column]

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

            y = temp
            b = 0
            for dato in per_month_datoer:
                for i in range(27, 0, -1):
                    if f"{i}." in dato:
                        senesteSaldo[0] = per_month_saldos[y+b]
                        break
                b += 1
            for text in per_month_tekster:
                if "Anna Lisa" in text:
                    if per_month_beloeber[y] == '1.500,00' or per_month_beloeber[y] == '1.000,00':
                        huslejefraanna[y] = per_month_beloeber[y]
                    else:
                        mobilePay[y] = per_month_beloeber[y]
                elif "Andel Energi" in text:
                    el[y] = per_month_beloeber[y]
                elif "Fibia" in text:
                    internet[y] = per_month_beloeber[y]
                elif "MobilePay" in text:
                    mobilePay[y] = per_month_beloeber[y]
                elif "WeShare" in text:
                    mobilePay[y] = per_month_beloeber[y]
                elif "NETTO" in text:
                    indkoeb[y] = per_month_beloeber[y]
                elif "Netto" in text:
                    indkoeb[y] = per_month_beloeber[y]
                elif "Superbrugsen" in text:
                    indkoeb[y] = per_month_beloeber[y]
                elif "F@TEX" in text:
                    indkoeb[y] = per_month_beloeber[y]
                elif "Foetex" in text:
                    indkoeb[y] = per_month_beloeber[y]
                elif "NORMAL" in text:
                    indkoeb[y] = per_month_beloeber[y]
                elif "Rema" in text:
                    indkoeb[y] = per_month_beloeber[y]
                elif "REMA" in text:
                    indkoeb[y] = per_month_beloeber[y]
                elif "Apote" in text:
                    indkoeb[y] = per_month_beloeber[y]
                elif "L�noverf�rsel" in text:
                    løn[y] = per_month_beloeber[y]
                elif "Lønoverførsel" in text:
                    løn[y] = per_month_beloeber[y]
                elif "LØNOVERFØRSEL" in text:
                    løn[y] = per_month_beloeber[y]
                elif "SU" in text:
                    su[y] = per_month_beloeber[y]
                elif "Husleje" in text:
                    husleje[y] = per_month_beloeber[y]
                elif "Wolt" in text:
                    fastfood[y] = per_month_beloeber[y]
                elif "Pizza" in text:
                    fastfood[y] = per_month_beloeber[y]
                elif "Boligst�tte" in text:
                    boligstøtte[y] = per_month_beloeber[y]
                elif "Boligstøtte" in text:
                    boligstøtte[y] = per_month_beloeber[y]
                elif "Nexus" in text:
                    fisOgBallade[y] = per_month_beloeber[y]
                elif "Steam" in text:
                    fisOgBallade[y] = per_month_beloeber[y]
                elif "7-11" in text:
                    fastfood[y] = per_month_beloeber[y]
                elif "Foreningen" in text:
                    fisOgBallade[y] = per_month_beloeber[y]
                elif "STEAM" in text:
                    fisOgBallade[y] = per_month_beloeber[y]
                else:
                    resterende[y] = per_month_beloeber[y]
                y += 1

                su_new = [x.replace('.', '').replace(',', '.')
                          if x is not None else '0' for x in su]
                su_float = pd.to_numeric(su_new)
                su_sum = np.nansum(su_float)
                løn_new = [x.replace('.', '').replace(
                    ',', '.') if x is not None else '0' for x in løn]
                løn_float = pd.to_numeric(løn_new)
                løn_sum = np.nansum(løn_float)
                boligstøtte_new = [x.replace('.', '').replace(
                    ',', '.') if x is not None else '0' for x in boligstøtte]
                boligstøtte_float = pd.to_numeric(boligstøtte_new)
                boligstøtte_sum = np.nansum(boligstøtte_float)
                el_new = [x.replace('.', '').replace(',', '.')
                          if x is not None else '0' for x in el]
                el_float = pd.to_numeric(el_new)
                el_sum = np.nansum(el_float)
                if (el_sum < 0):
                    el_sum = -1.0*el_sum
                internet_new = [x.replace('.', '').replace(
                    ',', '.') if x is not None else '0' for x in internet]
                internet_float = pd.to_numeric(internet_new)
                internet_sum = np.nansum(internet_float)
                if (internet_sum < 0):
                    internet_sum = -1.0*internet_sum
                husleje_new = [x.replace('.', '').replace(
                    ',', '.') if x is not None else '0' for x in husleje]
                husleje_float = pd.to_numeric(husleje_new)
                husleje_sum = np.nansum(husleje_float)
                if (husleje_sum < 0):
                    husleje_sum = -1.0*husleje_sum
                huslejefraanna_new = [x.replace('.', '').replace(
                    ',', '.') if x is not None else '0' for x in huslejefraanna]
                huslejefraanna_float = pd.to_numeric(huslejefraanna_new)
                huslejefraanna_sum = np.nansum(huslejefraanna_float)
                senesteSaldo_new = [str(x).replace('.', '').replace(
                    ',', '.') if type(x) == str else x for x in senesteSaldo]
                senesteSaldo_float = pd.to_numeric(senesteSaldo_new)
                senesteSaldo_sum = np.nansum(senesteSaldo_float)
                mobilePay_new = [x.replace('.', '').replace(
                    ',', '.') if x is not None else '0' for x in mobilePay]
                mobilePay_float = pd.to_numeric(mobilePay_new)
                mobilePay_sum = np.nansum(mobilePay_float)
                indkoeb_new = [x.replace('.', '').replace(
                    ',', '.') if x is not None else '0' for x in indkoeb]
                indkoeb_float = pd.to_numeric(indkoeb_new)
                indkoeb_sum = np.nansum(indkoeb_float)
                fastfood_new = [x.replace('.', '').replace(
                    ',', '.') if x is not None else '0' for x in fastfood]
                fastfood_float = pd.to_numeric(fastfood_new)
                fastfood_sum = np.nansum(fastfood_float)
                fisOgBallade_new = [x.replace('.', '').replace(
                    ',', '.') if x is not None else '0' for x in fisOgBallade]
                fisOgBallade_float = pd.to_numeric(fisOgBallade_new)
                fisOgBallade_sum = np.nansum(fisOgBallade_float)
                resterende_new = [x.replace('.', '').replace(
                    ',', '.') if x is not None else '0' for x in resterende]
                resterende_float = pd.to_numeric(resterende_new)
                resterende_sum = np.nansum(resterende_float)
                alleandrekontobevægelser = resterende_sum + \
                    fisOgBallade_sum+fastfood_sum+indkoeb_sum+mobilePay_sum
                fasteudgifter_sum = internet_sum + husleje_sum + el_sum
                indtægtialt = su_sum + løn_sum + boligstøtte_sum+huslejefraanna_sum
                forskeliudgiftindtægt = indtægtialt - \
                    (fasteudgifter_sum - alleandrekontobevægelser)
                if mo == 0:
                    jan = ["", str(forskeliudgiftindtægt).replace('.', ','), str(senesteSaldo_sum).replace('.', ','), "", "", str(indtægtialt).replace('.', ','), str(su_sum).replace('.', ','), str(løn_sum).replace('.', ','),
                           str(boligstøtte_sum).replace('.', ','), str(huslejefraanna_sum).replace('.', ','), "", str(fasteudgifter_sum - alleandrekontobevægelser).replace(
                               '.', ','), "", str(fasteudgifter_sum).replace('.', ','), str(husleje_sum).replace('.', ','), str(el_sum).replace('.', ','),
                           str(internet_sum).replace('.', ','), "", "", str(alleandrekontobevægelser).replace('.', ',')]
                if mo == 1:
                    feb = ["", str(forskeliudgiftindtægt).replace('.', ','), str(senesteSaldo_sum).replace('.', ','), "", "", str(indtægtialt).replace('.', ','), str(su_sum).replace('.', ','), str(løn_sum).replace('.', ','),
                           str(boligstøtte_sum).replace('.', ','), str(huslejefraanna_sum).replace('.', ','), "", str(fasteudgifter_sum - alleandrekontobevægelser).replace(
                               '.', ','), "", str(fasteudgifter_sum).replace('.', ','), str(husleje_sum).replace('.', ','), str(el_sum).replace('.', ','),
                           str(internet_sum).replace('.', ','), "", "", str(alleandrekontobevægelser).replace('.', ',')]
                if mo == 2:
                    mar = ["", str(forskeliudgiftindtægt).replace('.', ','), str(senesteSaldo_sum).replace('.', ','), "", "", str(indtægtialt).replace('.', ','), str(su_sum).replace('.', ','), str(løn_sum).replace('.', ','),
                           str(boligstøtte_sum).replace('.', ','), str(huslejefraanna_sum).replace('.', ','), "", str(fasteudgifter_sum - alleandrekontobevægelser).replace(
                               '.', ','), "", str(fasteudgifter_sum).replace('.', ','), str(husleje_sum).replace('.', ','), str(el_sum).replace('.', ','),
                           str(internet_sum).replace('.', ','), "", "", str(alleandrekontobevægelser).replace('.', ',')]
                if mo == 3:
                    apr = ["", str(forskeliudgiftindtægt).replace('.', ','), str(senesteSaldo_sum).replace('.', ','), "", "", str(indtægtialt).replace('.', ','), str(su_sum).replace('.', ','), str(løn_sum).replace('.', ','),
                           str(boligstøtte_sum).replace('.', ','), str(huslejefraanna_sum).replace('.', ','), "", str(fasteudgifter_sum - alleandrekontobevægelser).replace(
                               '.', ','), "", str(fasteudgifter_sum).replace('.', ','), str(husleje_sum).replace('.', ','), str(el_sum).replace('.', ','),
                           str(internet_sum).replace('.', ','), "", "", str(alleandrekontobevægelser).replace('.', ',')]
                if mo == 4:
                    maj = ["", str(forskeliudgiftindtægt).replace('.', ','), str(senesteSaldo_sum).replace('.', ','), "", "", str(indtægtialt).replace('.', ','), str(su_sum).replace('.', ','), str(løn_sum).replace('.', ','),
                           str(boligstøtte_sum).replace('.', ','), str(huslejefraanna_sum).replace('.', ','), "", str(fasteudgifter_sum - alleandrekontobevægelser).replace(
                               '.', ','), "", str(fasteudgifter_sum).replace('.', ','), str(husleje_sum).replace('.', ','), str(el_sum).replace('.', ','),
                           str(internet_sum).replace('.', ','), "", "", str(alleandrekontobevægelser).replace('.', ',')]
                if mo == 5:
                    jun = ["", str(forskeliudgiftindtægt).replace('.', ','), str(senesteSaldo_sum).replace('.', ','), "", "", str(indtægtialt).replace('.', ','), str(su_sum).replace('.', ','), str(løn_sum).replace('.', ','),
                           str(boligstøtte_sum).replace('.', ','), str(huslejefraanna_sum).replace('.', ','), "", str(fasteudgifter_sum - alleandrekontobevægelser).replace(
                               '.', ','), "", str(fasteudgifter_sum).replace('.', ','), str(husleje_sum).replace('.', ','), str(el_sum).replace('.', ','),
                           str(internet_sum).replace('.', ','), "", "", str(alleandrekontobevægelser).replace('.', ',')]
                if mo == 6:
                    jul = ["", str(forskeliudgiftindtægt).replace('.', ','), str(senesteSaldo_sum).replace('.', ','), "", "", str(indtægtialt).replace('.', ','), str(su_sum).replace('.', ','), str(løn_sum).replace('.', ','),
                           str(boligstøtte_sum).replace('.', ','), str(huslejefraanna_sum).replace('.', ','), "", str(fasteudgifter_sum - alleandrekontobevægelser).replace(
                               '.', ','), "", str(fasteudgifter_sum).replace('.', ','), str(husleje_sum).replace('.', ','), str(el_sum).replace('.', ','),
                           str(internet_sum).replace('.', ','), "", "", str(alleandrekontobevægelser).replace('.', ',')]
                if mo == 7:
                    aug = ["", str(forskeliudgiftindtægt).replace('.', ','), str(senesteSaldo_sum).replace('.', ','), "", "", str(indtægtialt).replace('.', ','), str(su_sum).replace('.', ','), str(løn_sum).replace('.', ','),
                           str(boligstøtte_sum).replace('.', ','), str(huslejefraanna_sum).replace('.', ','), "", str(fasteudgifter_sum - alleandrekontobevægelser).replace(
                               '.', ','), "", str(fasteudgifter_sum).replace('.', ','), str(husleje_sum).replace('.', ','), str(el_sum).replace('.', ','),
                           str(internet_sum).replace('.', ','), "", "", str(alleandrekontobevægelser).replace('.', ',')]
                if mo == 8:
                    sep = ["", str(forskeliudgiftindtægt).replace('.', ','), str(senesteSaldo_sum).replace('.', ','), "", "", str(indtægtialt).replace('.', ','), str(su_sum).replace('.', ','), str(løn_sum).replace('.', ','),
                           str(boligstøtte_sum).replace('.', ','), str(huslejefraanna_sum).replace('.', ','), "", str(fasteudgifter_sum - alleandrekontobevægelser).replace(
                               '.', ','), "", str(fasteudgifter_sum).replace('.', ','), str(husleje_sum).replace('.', ','), str(el_sum).replace('.', ','),
                           str(internet_sum).replace('.', ','), "", "", str(alleandrekontobevægelser).replace('.', ',')]
                if mo == 9:
                    okt = ["", str(forskeliudgiftindtægt).replace('.', ','), str(senesteSaldo_sum).replace('.', ','), "", "", str(indtægtialt).replace('.', ','), str(su_sum).replace('.', ','), str(løn_sum).replace('.', ','),
                           str(boligstøtte_sum).replace('.', ','), str(huslejefraanna_sum).replace('.', ','), "", str(fasteudgifter_sum - alleandrekontobevægelser).replace(
                               '.', ','), "", str(fasteudgifter_sum).replace('.', ','), str(husleje_sum).replace('.', ','), str(el_sum).replace('.', ','),
                           str(internet_sum).replace('.', ','), "", "", str(alleandrekontobevægelser).replace('.', ',')]
                if mo == 10:
                    nov = ["", str(forskeliudgiftindtægt).replace('.', ','), str(senesteSaldo_sum).replace('.', ','), "", "", str(indtægtialt).replace('.', ','), str(su_sum).replace('.', ','), str(løn_sum).replace('.', ','),
                           str(boligstøtte_sum).replace('.', ','), str(huslejefraanna_sum).replace('.', ','), "", str(fasteudgifter_sum - alleandrekontobevægelser).replace(
                               '.', ','), "", str(fasteudgifter_sum).replace('.', ','), str(husleje_sum).replace('.', ','), str(el_sum).replace('.', ','),
                           str(internet_sum).replace('.', ','), "", "", str(alleandrekontobevægelser).replace('.', ',')]
                if mo == 11:
                    dec = ["", str(forskeliudgiftindtægt).replace('.', ','), str(senesteSaldo_sum).replace('.', ','), "", "", str(indtægtialt).replace('.', ','), str(su_sum).replace('.', ','), str(løn_sum).replace('.', ','),
                           str(boligstøtte_sum).replace('.', ','), str(huslejefraanna_sum).replace('.', ','), "", str(fasteudgifter_sum - alleandrekontobevægelser).replace(
                               '.', ','), "", str(fasteudgifter_sum).replace('.', ','), str(husleje_sum).replace('.', ','), str(el_sum).replace('.', ','),
                           str(internet_sum).replace('.', ','), "", "", str(alleandrekontobevægelser).replace('.', ',')]

            temp += len(per_month_beloeber)
            mo += 1

        def calculate_sum(index_til_type):
            dates = [jan, feb, mar, apr, maj,
                     jun, jul, aug, sep, okt, nov, dec]
            sum = 0
            index = 0
            for date in dates:
                if date != ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""]:
                    sum = str(float(str(dates[index][index_til_type]).replace(
                        ",", ".")) + float(str(sum).replace(",", "."))).replace(".", ",")
                index += 1
            return sum

        def sum_of_elems_in_list():
            list = [resterende_total, fisOgBallade_total,
                    fastfood_total, indkoeb_total, mobilePay_total]
            sum = 0
            for elem in list:
                for strings in elem:
                    if strings is not None:
                        sum += float(strings.replace(".",
                                     "").replace(",", "."))
            return sum

        alleandrekontobevægelser_total = sum_of_elems_in_list()

        total = ["", calculate_sum(1), "N/A", "", "", calculate_sum(5), calculate_sum(6), calculate_sum(7), calculate_sum(8), calculate_sum(9), "", str(float(str(calculate_sum(13)).replace(",", ".")) -
                                                                                                                                                        alleandrekontobevægelser_total).replace(".", ","), "", calculate_sum(13), calculate_sum(14), calculate_sum(15), calculate_sum(16), "", "", str(alleandrekontobevægelser_total).replace(".", ",")]

        labels = ["", "Forskel i udgift/indtægt hver måned", "Penge på konto", "", "", "Indtægt i alt", "SU", "Løn", "Boligstøtte", "Husleje fra Anna", "",
                  "Udgifter tilpasset ift. kontobevægelser", "", "Faste udgifter sum", "Husleje", "El", "Internet", "", "", "Alle andre kontobevægelser"]
        df2 = pd.DataFrame({'': labels,
                            'Jan': jan,
                            'Feb': feb,
                            'Mar': mar,
                            'Apr': apr,
                            'Maj': maj,
                            'Jun': jun,
                            'Jul': jul,
                            'Aug': aug,
                            'Sep': sep,
                            'Okt': okt,
                            'Nov': nov,
                            'Dec': dec,
                            'Total': total})
        return df2

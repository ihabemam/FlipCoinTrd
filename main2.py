import fxcmpy
import datetime as dt
import pandas as pd
fxcmpy.__version__


# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    token = '5fceb84a9e281ae82c56c42676409a8f3290a1d7'
    con = fxcmpy.fxcmpy(access_token=token, log_level='error', server='demo', log_file=None)
    # con = fxcmpy.fxcmpy(config_file='fxcm.cfg')

    print(con.get_instruments())

    # each time can only extract around 10k historical data
    df = pd.DataFrame()
    for year in range(2020, 2021):
        print(year)
        try:
            df = df.append(con.get_candles('NAS100', period='m5', start="2021-01-01 00:00",
                                           end="2021-02-01 00:00"))
            df = df.append(con.get_candles('NAS100', period='m5', start="2021-02-01 00:00",
                                           end="2021-02-19 00:00"))
            df = df.append(con.get_candles('NAS100', period='m5', start=str(year) + "-03-01 00:00",
                                           end=str(year) + "-04-01 00:00"))
            df = df.append(con.get_candles('NAS100', period='m5', start=str(year) + "-04-01 00:00",
                                           end=str(year) + "-05-01 00:00"))
            df = df.append(con.get_candles('NAS100', period='m5', start=str(year) + "-05-01 00:00",
                                           end=str(year) + "-06-01 00:00"))
            df = df.append(con.get_candles('NAS100', period='m5', start=str(year) + "-06-01 00:00",
                                           end=str(year) + "-07-01 00:00"))
            df = df.append(con.get_candles('NAS100', period='m5', start=str(year) + "-07-01 00:00",
                                           end=str(year) + "-08-01 00:00"))
            df = df.append(con.get_candles('NAS100', period='m5', start=str(year) + "-08-01 00:00",
                                           end=str(year) + "-09-01 00:00"))
            df = df.append(con.get_candles('NAS100', period='m5', start=str(year) + "-09-01 00:00",
                                           end=str(year) + "-10-01 00:00"))
            df = df.append(con.get_candles('NAS100', period='m5', start=str(year) + "-10-01 00:00",
                                           end=str(year) + "-11-01 00:00"))
            df = df.append(con.get_candles('NAS100', period='m5', start=str(year) + "-11-01 00:00",
                                           end=str(year) + "-12-01 00:00"))
            df = df.append(con.get_candles('NAS100', period='m5', start=str(year) + "-12-01 00:00",
                                           end=str(year + 1) + "-01-01 00:00"))
        except:
            pass
    df.drop_duplicates(subset=None, keep='first', inplace=True)
    data = df[["bidopen", "bidclose", "bidhigh", "bidlow"]]
    data.columns = ['open', 'close', 'high', 'low']
    data.reset_index(drop=False, inplace=True)

    data.head()
    data.to_csv("FXCM_NAS100_M5.csv")

    con.close()

    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

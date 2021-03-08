# python main_amr.py fxcm.cfg NAS100

# pip install cassandra-driver
# pip install mariadb

import sys
import logging
import fxcmpy
import pandas as pd
from sqlalchemy import create_engine
import algo_trading_lib as atl
import mariadb

class AlgoTrading:
    ema_fast = 7
    ema_mid = 23
    ema_slow = 20
    symbol = 'NAS100'
    start_date = '2020-09-10'
    end_date = '2021-03-10'
    timeframe1 = 'm30'
    timeframe2 = 'm1'
    timeframe1_dir = 0
    open_positions = 0
    open_orders = 0
    order_size = 5
    timeframe1_is_ma_in_cor_order = 0
    timeframe1_close_price_in_the_right_order = 0
    number_of_concurrent_positions = 2
    rsi_upper = 49
    rsi_lower = 20

    # Parameter initialisation
    def __init__(self, log_file_name=None):
        file_name = log_file_name
        if file_name is None:
            file_name = 'C:/users/ehabe/PycharmProjects/pythonProject/logs/Trading.log'

        logging.basicConfig(filename=file_name, level=logging.INFO)


    # def connectMDB(self):
    #     try:
    #         conn = mariadb.connect(
    #             user='iemam',
    #             password='test123',
    #             host='192.168.0.117',
    #             port=3306,
    #             database='trading'
    #         )
    #     except mariadb.Error as e:
    #         print(f"Error connecting to MariaDB: {e}")
    #         sys.exit(1)
    #     return conn

    def saveData(self,data,engine):
        data.to_sql(name='ticks', con=engine, if_exists='append', index=False)

    def connectPlatform(self, configFile):
        return fxcmpy.fxcmpy(config_file=configFile)

    def trade(self):
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

    def main(self,argv):
        if len(sys.argv[1:]) < 2:
            exit("Please enter configuration file and instrument code")

        configFile = sys.argv[1:][1]
        instrumentCode = sys.argv[1:][2]

        con = self.connectPlatform(configFile)
        # mariaCon = self.connectMDB()

        marketData = market_data(instrumentCode,self.timeframe1,period)
        instrumentData=marketData.getData

        engine = create_engine('mysql+mysqlconnector://iemam:test123@192.168.0.117/trading')
        self.saveDate(instrumentData, engine)

        # Write Trading Logic Here
        con.subscribe_market_data(instrumentCode, self.trade)

        # Write back testing here


        # Clean up before exit
        # mariaCon.close()
        con.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    trd = AlgoTrading()
    trd.main(sys.argv)
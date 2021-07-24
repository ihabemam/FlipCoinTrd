# python main.py fxcm.cfg NAS100

import pandas as pd
import fxcmpy
fxcmpy.__version__
import sys
import logging
import time
from collections import deque
from sqlalchemy import create_engine
from signalHandler import signalHandler
from visualise import visualise
from trading_strategy import trading_strategy

class AlgoTrading:

    input_row_size = 30  # number of reading to run the strategy
    pip = 0.01
    stopLoss = -10 * pip
    takeProfit = 20 * pip
    spread = 2 * pip
    inputs = deque(maxlen=input_row_size)

    # Parameter initialisation
    def __init__(self, log_file_name=None):
        file_name = log_file_name
        if file_name is None:
            file_name = 'C:/users/ehabe/PycharmProjects/pythonProject/logs/Trading.log'

        logging.basicConfig(filename=file_name, level=logging.INFO)

    def connectPlatform(self, configFile):
        return fxcmpy.fxcmpy(config_file=configFile)

    def main(self,argv):
        if len(sys.argv[1:]) < 2:
            exit("Please enter configuration file and instrument code")

        configFile = sys.argv[1:][0]
        instrumentCode = sys.argv[1:][1]

        #con = self.connectPlatform(configFile)

        ############# READ FILE #############

        data = pd.read_csv('GBPUSD_H1_202001020600_202006010000.csv', sep='\t', skiprows=1,
                           names=['date', 'time', 'open', 'high', 'low', 'close', 'tickvol', 'vol', 'spread'])
        # data = pd.read_csv('EURUSD_M30.csv',sep=',', skiprows=1, names = ['time', 'open', 'high', 'low', 'close', 'tickvol','vol','spread' ])
        # data = pd.read_csv('EURUSD_M30.csv',sep='\t', skiprows=1, names = ['date', 'time', 'open', 'high', 'low', 'close', 'tickvol','vol','spread' ])
        data = data.drop(['tickvol', 'vol', 'spread'], axis=1)  # we do not need these coloumns

        ############# BACKTESTING #############
        # Handels Buy and Sell
        broker = signalHandler(self.stopLoss, self.takeProfit, self.spread, data)

        start_time = time.time()
        index = 0
        signal = 0
        for _, row in data.iterrows():

            # Loading the inputs array till the
            # minimum number of inputs are reached
            self.inputs.append(row)

            if len(self.inputs) == self.input_row_size:
                signal = trading_strategy(list(
                    self.inputs))  # call trading strategy. It will return one of the following 1 (Buy), 0 (do nothing) or -1 (sell)

                # Current Price
                current_price = row['close']

                # Checks signal and executes
                if signal == 1:
                    broker.buy(current_price, index)
                elif signal == -1:
                    broker.sell(current_price, index)
                elif signal == 0:
                    # Checking if stop loss or take profit is hit
                    broker.checkStopConditions(current_price, index)
                else:
                    print("Unknown Signal")
                    break

            index += 1

        end_time = time.time()
        print("Time consumed: {}s".format(round(end_time - start_time, 2)))

        final_data = broker.getData()  # <----- Gets Data into a DATAFRAME
        final_data.to_csv('backtesting.csv')
        # final_data has THREE new coloumns
        #   'action'        : The action the code implemented at that timestep.
        #   'P/L'           : The profit or loss at the time step, 0 when holding.
        #   'Total profit'  : The total profit TILL that time step.

        ############# VISUALISEING #############
        visualiser = visualise(final_data)
        visualiser.plotFig()
        exit("Program ended")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    trd = AlgoTrading()
    trd.main(sys.argv)
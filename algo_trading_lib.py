import sys
import logging
from os import path
import numpy as np
import pandas as pd
import talib as talib
from sqlalchemy import create_engine
import mariadb
import time as t

class MarketData:
    self.con = con
    self.symbol = symbol
    self.data = []
    self.m_data = []
    self.ema_fast = ema_fast
    self.ema_slow = ema_slow
    self.timeframe = timeframe
    self.high_timeframe = high_timeframe
    self.start_date = start_date
    self.end_date = end_date
    self.market_direction = 0
    self.order_size = order_size
    self.get_markert_direction()
    self.support = 0.0
    self.resistance = 0.0
    self.pivot_points = []

    def __init__(self, con,symbol,ema_fast,ema_slow,timeframe, start_date,end_date,high_timeframe, order_size, log_file_name=None):
        self.con = con
        self.symbol = symbol
        self.data = []
        self.m_data = []
        self.ema_fast = ema_fast
        self.ema_slow = ema_slow
        self.timeframe = timeframe
        self.high_timeframe = high_timeframe
        self.start_date = start_date
        self.end_date = end_date
        self.market_direction = 0
        self.order_size = order_size
        self.get_markert_direction()
        self.support = 0.0
        self.resistance = 0.0
        self.pivot_points =[]


    def get_market_data(self):
        dt = self.con.get_candles(instrument=self.symbol, period = self.timeframe, start=self.start_date, end=self.end_date)
        self.data = dt


    def get_market_data_by_timeframe(self, timeframe):
        dt = self.con.get_candles(instrument=self.symbol, period = timeframe, start=self.start_date, end=self.end_date)
        self.data = dt
        return dt

    def add_candle_patters(self):

      CDL2CROWS = talib.CDL2CROWS(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDL2CROWS'] = CDL2CROWS
    
      CDL3BLACKCROWS = talib.CDL3BLACKCROWS(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDL3BLACKCROWS'] = CDL3BLACKCROWS
    
      CDL3INSIDE = talib.CDL3INSIDE(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDL3INSIDE'] = CDL3INSIDE
    
      CDL3LINESTRIKE = talib.CDL3LINESTRIKE(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDL3LINESTRIKE'] = CDL3LINESTRIKE
    
      CDL3OUTSIDE = talib.CDL3OUTSIDE(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDL3OUTSIDE'] = CDL3OUTSIDE
    
      CDL3STARSINSOUTH = talib.CDL3STARSINSOUTH(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDL3STARSINSOUTH'] = CDL3STARSINSOUTH
    
      CDL3WHITESOLDIERS = talib.CDL3WHITESOLDIERS(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDL3WHITESOLDIERS'] = CDL3WHITESOLDIERS
    
      CDLABANDONEDBABY = talib.CDLABANDONEDBABY(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLABANDONEDBABY'] = CDLABANDONEDBABY
    
      CDLADVANCEBLOCK = talib.CDLADVANCEBLOCK(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLADVANCEBLOCK'] = CDLADVANCEBLOCK
    
      CDLBELTHOLD = talib.CDLBELTHOLD(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLBELTHOLD'] = CDLBELTHOLD
    
      CDLBREAKAWAY = talib.CDLBREAKAWAY(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLBREAKAWAY'] = CDLBREAKAWAY
    
      CDLCLOSINGMARUBOZU = talib.CDLCLOSINGMARUBOZU(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLCLOSINGMARUBOZU'] = CDLCLOSINGMARUBOZU
    
      CDLCONCEALBABYSWALL = talib.CDLCONCEALBABYSWALL(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLCONCEALBABYSWALL'] = CDLCONCEALBABYSWALL
    
      CDLCOUNTERATTACK = talib.CDLCOUNTERATTACK(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLCOUNTERATTACK'] = CDLCOUNTERATTACK
    
      CDLDARKCLOUDCOVER = talib.CDLDARKCLOUDCOVER(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLDARKCLOUDCOVER'] = CDLDARKCLOUDCOVER
    
      CDLDOJI = talib.CDLDOJI(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLDOJI'] = CDLDOJI
    
      CDLDOJISTAR = talib.CDLDOJISTAR(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLDOJISTAR'] = CDLDOJISTAR
    
      CDLDRAGONFLYDOJI = talib.CDLDRAGONFLYDOJI(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLDRAGONFLYDOJI'] = CDLDRAGONFLYDOJI
    
      CDLENGULFING = talib.CDLENGULFING(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLENGULFING'] = CDLENGULFING
    
      CDLEVENINGDOJISTAR = talib.CDLEVENINGDOJISTAR(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLEVENINGDOJISTAR'] = CDLEVENINGDOJISTAR
    
      CDLEVENINGSTAR = talib.CDLEVENINGSTAR(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLEVENINGSTAR'] = CDLEVENINGSTAR
    
      CDLGAPSIDESIDEWHITE = talib.CDLGAPSIDESIDEWHITE(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLGAPSIDESIDEWHITE'] = CDLGAPSIDESIDEWHITE
    
      CDLGRAVESTONEDOJI = talib.CDLGRAVESTONEDOJI(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLGRAVESTONEDOJI'] = CDLGRAVESTONEDOJI
    
      CDLHAMMER = talib.CDLHAMMER(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLHAMMER'] = CDLHAMMER
    
      CDLHANGINGMAN = talib.CDLHANGINGMAN(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLHANGINGMAN'] = CDLHANGINGMAN
    
      CDLHARAMI = talib.CDLHARAMI(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLHARAMI'] = CDLHARAMI
    
      CDLHARAMICROSS = talib.CDLHARAMICROSS(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLHARAMICROSS'] = CDLHARAMICROSS
    
      CDLHIGHWAVE = talib.CDLHIGHWAVE(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLHIGHWAVE'] = CDLHIGHWAVE
    
      CDLHIKKAKE = talib.CDLHIKKAKE(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLHIKKAKE'] = CDLHIKKAKE
    
      CDLHIKKAKEMOD = talib.CDLHIKKAKEMOD(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLHIKKAKEMOD'] = CDLHIKKAKEMOD
    
      CDLHOMINGPIGEON = talib.CDLHOMINGPIGEON(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLHOMINGPIGEON'] = CDLHOMINGPIGEON
    
      CDLIDENTICAL3CROWS = talib.CDLIDENTICAL3CROWS(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLIDENTICAL3CROWS'] = CDLIDENTICAL3CROWS
    
      CDLINNECK = talib.CDLINNECK(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLINNECK'] = CDLINNECK
    
      CDLINVERTEDHAMMER = talib.CDLINVERTEDHAMMER(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLINVERTEDHAMMER'] = CDLINVERTEDHAMMER
    
      CDLKICKING = talib.CDLKICKING(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLKICKING'] = CDLKICKING
    
      CDLKICKINGBYLENGTH = talib.CDLKICKINGBYLENGTH(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLKICKINGBYLENGTH'] = CDLKICKINGBYLENGTH
    
      CDLLADDERBOTTOM = talib.CDLLADDERBOTTOM(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLLADDERBOTTOM'] = CDLLADDERBOTTOM
    
      CDLLONGLEGGEDDOJI = talib.CDLLONGLEGGEDDOJI(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLLONGLEGGEDDOJI'] = CDLLONGLEGGEDDOJI
    
      CDLLONGLINE = talib.CDLLONGLINE(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLLONGLINE'] = CDLLONGLINE
    
      CDLMARUBOZU = talib.CDLMARUBOZU(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLMARUBOZU'] = CDLMARUBOZU
    
      CDLMATCHINGLOW = talib.CDLMATCHINGLOW(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLMATCHINGLOW'] = CDLMATCHINGLOW
    
      CDLMATHOLD = talib.CDLMATHOLD(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLMATHOLD'] = CDLMATHOLD
    
      CDLMORNINGDOJISTAR = talib.CDLMORNINGDOJISTAR(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLMORNINGDOJISTAR'] = CDLMORNINGDOJISTAR
    
      CDLMORNINGSTAR = talib.CDLMORNINGSTAR(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLMORNINGSTAR'] = CDLMORNINGSTAR
    
      CDLONNECK = talib.CDLONNECK(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLONNECK'] = CDLONNECK
    
      CDLPIERCING = talib.CDLPIERCING(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLPIERCING'] = CDLPIERCING
    
      CDLRICKSHAWMAN = talib.CDLRICKSHAWMAN(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLRICKSHAWMAN'] = CDLRICKSHAWMAN
    
      CDLRISEFALL3METHODS = talib.CDLRISEFALL3METHODS(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLRISEFALL3METHODS'] = CDLRISEFALL3METHODS
    
      CDLSEPARATINGLINES = talib.CDLSEPARATINGLINES(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLSEPARATINGLINES'] = CDLSEPARATINGLINES
    
      CDLSHOOTINGSTAR = talib.CDLSHOOTINGSTAR(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLSHOOTINGSTAR'] = CDLSHOOTINGSTAR
    
      CDLSHORTLINE = talib.CDLSHORTLINE(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLSHORTLINE'] = CDLSHORTLINE
    
      CDLSPINNINGTOP = talib.CDLSPINNINGTOP(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLSPINNINGTOP'] = CDLSPINNINGTOP
    
      CDLSTALLEDPATTERN = talib.CDLSTALLEDPATTERN(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLSTALLEDPATTERN'] = CDLSTALLEDPATTERN
    
      CDLSTICKSANDWICH = talib.CDLSTICKSANDWICH(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLSTICKSANDWICH'] = CDLSTICKSANDWICH
    
      CDLTAKURI = talib.CDLTAKURI(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLTAKURI'] = CDLTAKURI
    
      CDLTASUKIGAP = talib.CDLTASUKIGAP(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLTASUKIGAP'] = CDLTASUKIGAP
    
      CDLTHRUSTING = talib.CDLTHRUSTING(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLTHRUSTING'] = CDLTHRUSTING
    
      CDLTRISTAR = talib.CDLTRISTAR(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLTRISTAR'] = CDLTRISTAR
    
      CDLUNIQUE3RIVER = talib.CDLUNIQUE3RIVER(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLUNIQUE3RIVER'] = CDLUNIQUE3RIVER
    
      CDLUPSIDEGAP2CROWS = talib.CDLUPSIDEGAP2CROWS(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLUPSIDEGAP2CROWS'] = CDLUPSIDEGAP2CROWS
    
      CDLXSIDEGAP3METHODS = talib.CDLXSIDEGAP3METHODS(self.data["askopen"], self.data["askhigh"], self.data["asklow"], self.data["askclose"])
      self.data['CDLXSIDEGAP3METHODS'] = CDLXSIDEGAP3METHODS

    def add_candle_patters(self,data):

          CDL2CROWS = talib.CDL2CROWS(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDL2CROWS'] = CDL2CROWS

          CDL3BLACKCROWS = talib.CDL3BLACKCROWS(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDL3BLACKCROWS'] = CDL3BLACKCROWS

          CDL3INSIDE = talib.CDL3INSIDE(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDL3INSIDE'] = CDL3INSIDE

          CDL3LINESTRIKE = talib.CDL3LINESTRIKE(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDL3LINESTRIKE'] = CDL3LINESTRIKE

          CDL3OUTSIDE = talib.CDL3OUTSIDE(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDL3OUTSIDE'] = CDL3OUTSIDE

          CDL3STARSINSOUTH = talib.CDL3STARSINSOUTH(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDL3STARSINSOUTH'] = CDL3STARSINSOUTH

          CDL3WHITESOLDIERS = talib.CDL3WHITESOLDIERS(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDL3WHITESOLDIERS'] = CDL3WHITESOLDIERS

          CDLABANDONEDBABY = talib.CDLABANDONEDBABY(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLABANDONEDBABY'] = CDLABANDONEDBABY

          CDLADVANCEBLOCK = talib.CDLADVANCEBLOCK(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLADVANCEBLOCK'] = CDLADVANCEBLOCK

          CDLBELTHOLD = talib.CDLBELTHOLD(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLBELTHOLD'] = CDLBELTHOLD

          CDLBREAKAWAY = talib.CDLBREAKAWAY(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLBREAKAWAY'] = CDLBREAKAWAY

          CDLCLOSINGMARUBOZU = talib.CDLCLOSINGMARUBOZU(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLCLOSINGMARUBOZU'] = CDLCLOSINGMARUBOZU

          CDLCONCEALBABYSWALL = talib.CDLCONCEALBABYSWALL(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLCONCEALBABYSWALL'] = CDLCONCEALBABYSWALL

          CDLCOUNTERATTACK = talib.CDLCOUNTERATTACK(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLCOUNTERATTACK'] = CDLCOUNTERATTACK

          CDLDARKCLOUDCOVER = talib.CDLDARKCLOUDCOVER(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLDARKCLOUDCOVER'] = CDLDARKCLOUDCOVER

          CDLDOJI = talib.CDLDOJI(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLDOJI'] = CDLDOJI

          CDLDOJISTAR = talib.CDLDOJISTAR(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLDOJISTAR'] = CDLDOJISTAR

          CDLDRAGONFLYDOJI = talib.CDLDRAGONFLYDOJI(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLDRAGONFLYDOJI'] = CDLDRAGONFLYDOJI

          CDLENGULFING = talib.CDLENGULFING(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLENGULFING'] = CDLENGULFING

          CDLEVENINGDOJISTAR = talib.CDLEVENINGDOJISTAR(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLEVENINGDOJISTAR'] = CDLEVENINGDOJISTAR

          CDLEVENINGSTAR = talib.CDLEVENINGSTAR(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLEVENINGSTAR'] = CDLEVENINGSTAR

          CDLGAPSIDESIDEWHITE = talib.CDLGAPSIDESIDEWHITE(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLGAPSIDESIDEWHITE'] = CDLGAPSIDESIDEWHITE

          CDLGRAVESTONEDOJI = talib.CDLGRAVESTONEDOJI(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLGRAVESTONEDOJI'] = CDLGRAVESTONEDOJI

          CDLHAMMER = talib.CDLHAMMER(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLHAMMER'] = CDLHAMMER

          CDLHANGINGMAN = talib.CDLHANGINGMAN(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLHANGINGMAN'] = CDLHANGINGMAN

          CDLHARAMI = talib.CDLHARAMI(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLHARAMI'] = CDLHARAMI

          CDLHARAMICROSS = talib.CDLHARAMICROSS(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLHARAMICROSS'] = CDLHARAMICROSS

          CDLHIGHWAVE = talib.CDLHIGHWAVE(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLHIGHWAVE'] = CDLHIGHWAVE

          CDLHIKKAKE = talib.CDLHIKKAKE(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLHIKKAKE'] = CDLHIKKAKE

          CDLHIKKAKEMOD = talib.CDLHIKKAKEMOD(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLHIKKAKEMOD'] = CDLHIKKAKEMOD

          CDLHOMINGPIGEON = talib.CDLHOMINGPIGEON(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLHOMINGPIGEON'] = CDLHOMINGPIGEON

          CDLIDENTICAL3CROWS = talib.CDLIDENTICAL3CROWS(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLIDENTICAL3CROWS'] = CDLIDENTICAL3CROWS

          CDLINNECK = talib.CDLINNECK(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLINNECK'] = CDLINNECK

          CDLINVERTEDHAMMER = talib.CDLINVERTEDHAMMER(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLINVERTEDHAMMER'] = CDLINVERTEDHAMMER

          CDLKICKING = talib.CDLKICKING(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLKICKING'] = CDLKICKING

          CDLKICKINGBYLENGTH = talib.CDLKICKINGBYLENGTH(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLKICKINGBYLENGTH'] = CDLKICKINGBYLENGTH

          CDLLADDERBOTTOM = talib.CDLLADDERBOTTOM(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLLADDERBOTTOM'] = CDLLADDERBOTTOM

          CDLLONGLEGGEDDOJI = talib.CDLLONGLEGGEDDOJI(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLLONGLEGGEDDOJI'] = CDLLONGLEGGEDDOJI

          CDLLONGLINE = talib.CDLLONGLINE(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLLONGLINE'] = CDLLONGLINE

          CDLMARUBOZU = talib.CDLMARUBOZU(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLMARUBOZU'] = CDLMARUBOZU

          CDLMATCHINGLOW = talib.CDLMATCHINGLOW(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLMATCHINGLOW'] = CDLMATCHINGLOW

          CDLMATHOLD = talib.CDLMATHOLD(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLMATHOLD'] = CDLMATHOLD

          CDLMORNINGDOJISTAR = talib.CDLMORNINGDOJISTAR(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLMORNINGDOJISTAR'] = CDLMORNINGDOJISTAR

          CDLMORNINGSTAR = talib.CDLMORNINGSTAR(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLMORNINGSTAR'] = CDLMORNINGSTAR

          CDLONNECK = talib.CDLONNECK(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLONNECK'] = CDLONNECK

          CDLPIERCING = talib.CDLPIERCING(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLPIERCING'] = CDLPIERCING

          CDLRICKSHAWMAN = talib.CDLRICKSHAWMAN(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLRICKSHAWMAN'] = CDLRICKSHAWMAN

          CDLRISEFALL3METHODS = talib.CDLRISEFALL3METHODS(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLRISEFALL3METHODS'] = CDLRISEFALL3METHODS

          CDLSEPARATINGLINES = talib.CDLSEPARATINGLINES(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLSEPARATINGLINES'] = CDLSEPARATINGLINES

          CDLSHOOTINGSTAR = talib.CDLSHOOTINGSTAR(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLSHOOTINGSTAR'] = CDLSHOOTINGSTAR

          CDLSHORTLINE = talib.CDLSHORTLINE(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLSHORTLINE'] = CDLSHORTLINE

          CDLSPINNINGTOP = talib.CDLSPINNINGTOP(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLSPINNINGTOP'] = CDLSPINNINGTOP

          CDLSTALLEDPATTERN = talib.CDLSTALLEDPATTERN(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLSTALLEDPATTERN'] = CDLSTALLEDPATTERN

          CDLSTICKSANDWICH = talib.CDLSTICKSANDWICH(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLSTICKSANDWICH'] = CDLSTICKSANDWICH

          CDLTAKURI = talib.CDLTAKURI(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLTAKURI'] = CDLTAKURI

          CDLTASUKIGAP = talib.CDLTASUKIGAP(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLTASUKIGAP'] = CDLTASUKIGAP

          CDLTHRUSTING = talib.CDLTHRUSTING(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLTHRUSTING'] = CDLTHRUSTING

          CDLTRISTAR = talib.CDLTRISTAR(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLTRISTAR'] = CDLTRISTAR

          CDLUNIQUE3RIVER = talib.CDLUNIQUE3RIVER(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLUNIQUE3RIVER'] = CDLUNIQUE3RIVER

          CDLUPSIDEGAP2CROWS = talib.CDLUPSIDEGAP2CROWS(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLUPSIDEGAP2CROWS'] = CDLUPSIDEGAP2CROWS

          CDLXSIDEGAP3METHODS = talib.CDLXSIDEGAP3METHODS(data["askopen"], data["askhigh"], data["asklow"], data["askclose"])
          data['CDLXSIDEGAP3METHODS'] = CDLXSIDEGAP3METHODS

    def prepare_data(self,include_SR):
        print('prepare data is started!')
        self.data['atr'] = talib.ATR(self.data['askhigh'],self.data['asklow'],(self.data['askclose']))
        self.data['ema_fast'] = talib.EMA(self.data['askclose'], self.ema_ft)
        self.data['ema_slow'] = talib.EMA(self.data['askclose'], self.ema_sw)
        self.data['rsi'] = talib.RSI(self.data['askclose'],20)
        self.data['ema_fast_dir'] = np.where(self.data['ema_fast'].diff() > 0, 1, -1)
        self.data['ema_slow_dir'] = np.where(self.data['ema_slow'].diff() > 0, 1, -1)
        self.data['timeframe2_dir'] = self.data['ema_slow_dir'].rolling(10).sum()
        self.data['avg_atr'] = self.data['atr'].rolling(10).mean()

        if(include_SR == True):
            self.pivot_point()
            i = 0
            x = len(self.data)
            print(x)
            for i in range(x):
                self.find_zone(self.data['askclose'][i])
                self.data['support'][i] = self.support
                self.data['resistance'][i] = self.resistance
                i =i+1
        print('prepare data is finished!')

    def prepare_data(self,data,include_SR ):
        print('prepare data is started!')
        data['atr'] = talib.ATR(data['askhigh'],data['asklow'],(data['askclose']))
        data['ema_fast'] = talib.EMA(data['askclose'], self.ema_fast)
        data['ema_slow'] = talib.EMA(data['askclose'], self.ema_slow)
        data['rsi'] = talib.RSI(data['askclose'],20)
        data['ema_fast_dir'] = np.where(data['ema_fast'].diff() > 0, 1, -1)
        data['ema_slow_dir'] = np.where(data['ema_slow'].diff() > 0, 1, -1)
        data['timeframe2_dir'] = data['ema_slow_dir'].rolling(10).sum()
        data['avg_atr'] = data['atr'].rolling(10).mean()
        data['c_support']=0.000
        data['c_resistance']=0.000
        data['support']=0.000
        data['resistance']=0.000

        if(include_SR == True):
            pivots_lst = self.pivot_point(data)
            i = 0
            x = len(data)
            print(x)
            sup = 0
            res = 0
            for i in range(x):
                sup,res = self.find_zone(data['askclose'][i],pivots_lst)
                data['c_support'][i] = sup
                data['c_resistance'][i] = res
                i =i+1

            data['support'] = data['c_support'].rolling(3).min()
            data['resistance'] = data['c_resistance'].rolling(3).max()
        print('prepare data is finished!')

    def ema_crossover(self):
      self.data['cross_over_down'] = np.where(self.data['ema_fast']- self.data['ema_slow']< 0,1,0)
      self.data['cross_over_up'] = np.where(self.data['ema_fast']- self.data['ema_slow']> 0,1,0)
      self.data['sell_signal'] = self.data['cross_over_down'].diff()
      self.data['buy_signal'] = self.data['cross_over_up'].diff()

    def ema_crossover(self,data):
      data['cross_over_down'] = np.where(data['ema_fast']- data['ema_slow']< 0,1,0)
      data['cross_over_up'] = np.where(data['ema_fast']- data['ema_slow']> 0,1,0)
      data['sell_signal'] = data['cross_over_down'].diff()
      data['buy_signal'] = data['cross_over_up'].diff()

    def on_tick(self,dt, df):
      open_positions = len(self.con.get_open_positions(kind='list'))
      print('number of open position:', open_positions)
      print('number of open orders: ', self.con.get_order_ids()  )

      if open_positions <= 3:
          timeframe2_is_moving_average_in_correct_order = 0
          timeframe2_is_close_price_in_correct_order = 0
          stop_loss = 0.0
          take_profit = 0.0
          entry = 0.0
          pip = 0.0001

          # serialize the data of the action frame to a file /
          # check if the file exists, append the data otherwise create the file for the first time


          # self.save_data(self.symbol, '1Min', df)
          engine = create_engine('mysql+mysqlconnector://iemam:test123@192.168.0.117/trading')
          df.to_sql(name='ticks', con=engine, if_exists='append', index=False)

          # read the persisted data from the file
          # dt = pd.read_csv('ActionFrame/' + self.symbol.replace('/', '') + '.csv')
          df = pd.read_sql_query("SELECT * FROM ticks", con=engine)
          dt2 = pd.read_csv('marketdata_nas100_15.csv')
          self.prepare_data( dt,False)
         # self.add_candle_patters(dt)
          self.ema_crossover(dt)



          dt = dt.fillna(0)
          dt.to_csv('ActionFrame/' + self.symbol.replace('/', '') + 'tr.csv')
          dist_between_supp_and_res = self.calculate_pips(dt2['resistance'][len(dt2)-1],dt2['support'][len(dt2)-1]) # calculate the number of pips between the support and resistance
          dist_to_support = self.calculate_pips(dt['askclose'][len(dt)-1],dt2['support'][len(dt2)-1]) # calculate the number of pips between the support and resistance
          dist_to_resistance = self.calculate_pips(dt2['resistance'][len(dt2)-1],dt['askclose'][len(dt)-1]) # calculate the number of pips between the support and resistance

          print('Market trend is: ', dt2['timeframe2_dir'][len(dt2)-1])
          print('dist_between_supp_and_res is: ', dist_between_supp_and_res)
          print('dist_to_support is: ', dist_to_support)
          print('dist_to_resistance is: ', dist_to_resistance)
          print('%dist_to_support is: ', dist_to_support/dist_between_supp_and_res)
          print('%dist_to_resistance is: ', dist_to_resistance/dist_between_supp_and_res)

          order =''
          last_trade = []

          if dt2['timeframe2_dir'][len(dt2)-1] >=2:
              if 0.1 <= dist_to_support/dist_between_supp_and_res <= 0.6:
                print('dist_to_support/dist_between_supp_and_res ', dist_to_support/dist_between_supp_and_res)
                print('buy condition fullfilled with the same market trend')
                #ie order = self.con.open_trade(self.symbol, is_buy=True, rate=dt['askclose'][len(dt)-1], amount=self.order_size, is_in_pips=True, time_in_force='GTC',order_type='AtMarket',limit=+5, stop=-3)
              elif 0.6 <= dist_to_resistance/dist_between_supp_and_res <= 0.85:
                 print('sell condition fullfilled against market trend')
                 #ie order = self.con.open_trade(self.symbol, is_buy=False, rate=dt['askclose'][len(dt)-1], amount=self.order_size, is_in_pips=True, time_in_force='GTC',order_type='AtMarket',limit=+5, stop=-3)

            #    order = self.con.create_market_buy_order(self.symbol,self.order_size)
            #    last_trade = self.con.get_open_trade_ids()

            #    self.con.change_trade_stop_limit(last_trade[-1],is_stop=False, rate = +3, is_in_pips=True, trailing_step=0)
            #    self.con.change_trade_stop_limit(last_trade[-1],is_stop=True, rate = -3, is_in_pips=True, trailing_step=0)


          elif dt2['timeframe2_dir'][len(dt2)-1] <= -2:
              if 0.05 <= dist_to_resistance/dist_between_supp_and_res <= 0.8 :
                print('sell condition fullfilled against market trend')
                #ie order = self.con.create_market_sell_order(self.symbol,self.order_size)
                #
                # last_trade = self.con.get_open_trade_ids()
                # self.con.change_trade_stop_limit(last_trade[-1],is_stop=False, rate = +3, is_in_pips=True, trailing_step=0)
                # self.con.change_trade_stop_limit(last_trade[-1],is_stop=True, rate = -3, is_in_pips=True, trailing_step=0)
                # order = self.con.open_trade(self.symbol, is_buy=False, rate=dt['askclose'][len(dt)-1], amount=self.order_size, is_in_pips=True, time_in_force='GTC',order_type='AtMarket',limit=+5, stop=-3)
          elif 0.2 <= dist_to_support/dist_between_supp_and_res <= 0.4:
                print('buy condition fullfilled against market trend')
                #ie order = self.con.open_trade(self.symbol, is_buy=True, rate=dt['askclose'][len(dt)-1], amount=self.order_size, is_in_pips=True, time_in_force='GTC',order_type='AtMarket',limit=+5, stop=-3)
    def save_data(self,symbol, tf,df):
      # serialize the data of the action frame to a file /
      # check if the file exists, append the data otherwise create the file for the first time
      if path.exists('ActionFrame/'+ symbol.replace('/', '') + '.csv'):
        data = df.Bid.resample(tf).ohlc()
        data.to_csv('ActionFrame/' + symbol.replace('/', '')+'.csv', mode='a',index=True, header=False)
      else:
        data = df.Bid.resample(tf).ohlc()
        data.rename({'close':'askclose' , 'open':'askopen','high':'askhigh', 'low':'asklow'},axis='columns' , inplace=True)
        data.to_csv('ActionFrame/'+ symbol.replace('/', '')+'.csv')

    def get_file_name(symbol):
      return symbol.replace('/', '')

    def get_markert_direction(self):
        m_dt = self.con.get_candles(instrument=self.symbol, period = self.high_timeframe, start=self.start_date, end=self.end_date)
        self.m_data = m_dt

        self.m_data['atr'] = talib.ATR(self.m_data['askhigh'],self.m_data['asklow'],(self.m_data['askclose']))
        self.m_data['ema_fast'] = talib.EMA(self.m_data['askclose'], self.ema_fast)
        self.m_data['ema_slow'] = talib.EMA(self.m_data['askclose'], self.ema_slow)
        self.m_data['rsi'] = talib.RSI(self.m_data['askclose'],20)
        self.m_data['ema_fast_dir'] = np.where(self.m_data['ema_fast'].diff() > 0, 1, -1)
        self.m_data['ema_slow_dir'] = np.where(self.m_data['ema_slow'].diff() > 0, 1, -1)
        self.m_data['timeframe2_dir'] = self.m_data['ema_slow_dir'].rolling(10).sum()

        self.market_direction = self.m_data['timeframe2_dir'][-1]
        print( 'market_direction ',self.m_data['timeframe2_dir'][-1] )


    def pivot_point(self,data):
        print('-----pivot point function started--------\n', self.data)
        data

        Range = [0,0,0,0,0,0,0,0,0,0]
        current_max = 0.0000
        counter = 0
        last_pivot = 0.000
        pivots =[]

        i = 0
        for i in range(len(data)):
            current_max = max(Range, default=0)
            value =  round(data['askhigh'][i],3)
            Range = Range[1:9]
            Range.append(value)
            i = i + 1
            if current_max == max(Range, default=0.000):
                counter +=1
            else:
                counter =0
            if counter == 5:
                last_pivot = current_max
                pivots.append(last_pivot)

        return pivots
        print('----------Pivot Points Prepared -------------', pivots)

    def find_zone(self, price, pivots):
        print('---------- Find Zone Started-------------- and pivot points', pivots)
        support= []
        resistance = []
        print('price', price)

        for i in pivots:
            if price > i:
                support.append([price-i,i])
                print('support list:', len(support))
            else:
                resistance.append([i-price,i])
                print('resistance list:', len(resistance))
        support = sorted(support, key = lambda x: x[0])
        resistance = sorted(resistance, key = lambda x: x[0])
        print('Support ----', resistance[0][1])

        sup = 0.0000
        res = 0.0000

        try:
            sup = support[0][1]
        except:
            print("excpetion raised as support could not be identified for this price")
            sup = -100
        try:
            res = resistance[0][1]
        except:
            print("excpetion raised as  resistance could not be identified for this price")
            res = -100
        print("support is ",sup, 'and resistance is ', res ,'for the price ',price)
        return sup,res


    def calculate_pips(self,price1,price2,JPY_pair=False):

        if JPY_pair == True: #check if a YEN cross and change the multiplier
            multiplier = 0.01
        else:
            multiplier = 0.0001

        #Calc how much to risk

        pips_int = abs((price1 - price2) / multiplier)

        return pips_int


    def size_position(self, acct_value, price, stop, risk, method=0, exchange_rate=None, JPY_pair=False):
        '''
        Helper function to calcuate the position size given a known amount of risk.

        *Args*
        - price: Float, the current price of the instrument
        - stop: Float, price level of the stop loss
        - risk: Float, the amount of the account equity to risk

        *Kwargs*
        - JPY_pair: Bool, whether the instrument being traded is part of a JPY
        pair. The muliplier used for calculations will be changed as a result.
        - Method: Int,
            - 0: Acc currency and counter currency are the same
            - 1: Acc currency is same as base currency
            - 2: Acc currency is neither same as base or counter currency
        - exchange_rate: Float, is the exchange rate between the account currency
        and the counter currency. Required for method 2.
        '''

        if JPY_pair == True: #check if a YEN cross and change the multiplier
            multiplier = 0.01
        else:
            multiplier = 0.0001

        #Calc how much to risk
        acc_value = acct_value
        cash_risk = acc_value * risk
        stop_pips_int = abs((price - stop) / multiplier)
        pip_value = cash_risk / stop_pips_int

        if method == 1:
            #pip_value = pip_value * price
            units = pip_value / multiplier
            return units

        elif method == 2:
            pip_value = pip_value * exchange_rate
            units = pip_value / multiplier
            return units

        else: # is method 0
            units = pip_value / multiplier
            return units

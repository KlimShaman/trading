from AlorPy import AlorPy  # Работа с Alor OpenAPI V2
from Config import Config  # Файл конфигурации
import pandas as pd
from datetime import datetime


def getHistData(exchange, ticker, tf, dateFrom, dateTo):   
    apProvider = AlorPy(Config.UserName, Config.RefreshToken)  # Подключаемся к торговому счету. Логин и Refresh Token берутся из файла Config.py
    hist = apProvider.GetHistory(exchange, ticker, tf, secondsFrom=apProvider.MskDatetimeToUTCTimeStamp(datetime.fromisoformat(dateFrom)), secondsTo=apProvider.MskDatetimeToUTCTimeStamp(datetime.fromisoformat(dateTo)), untraded=False)
    histdf = pd.DataFrame(columns = ['time', 'close', 'open', 'high', 'low', 'volume'])
    histdf = histdf.append(hist['history'], ignore_index=True)
    for i in range(len(histdf['time'])):
        histdf['time'][i] = apProvider.UTCTimeStampToMskDatetime(histdf['time'][i])
    return histdf

print(getHistData('MOEX', 'SBER', '60', '2023-02-16T00:05:23', '2023-02-17T00:05:23'))

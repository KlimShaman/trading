from AlorPy import AlorPy  # Работа с Alor OpenAPI V2
from Config import Config  # Файл конфигурации
import pandas as pd

apProvider = AlorPy(Config.UserName, Config.RefreshToken)  # Подключаемся к торговому счету. Логин и Refresh Token берутся из файла Config.py
securities = apProvider.GetSecuritiesExchange('MOEX')

quotes = []
for i in range(len(securities)):
    if (securities[i]['type'] == 'CS' and securities[i]['symbol'] not in quotes):
        quotes.append(securities[i]['symbol'])

df = pd.DataFrame(quotes)
df.to_csv('C:/Python/trading/quotes.csv') 

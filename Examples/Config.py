# Чтобы получить Refresh Token:
# 0. Для получения тестового логина/пароля демо счета оставить заявку в Telegram на https://t.me/AlorOpenAPI
# 1. Зарегистрироваться на https://alor.dev/login
# 2. Выбрать "Токены для доступа к API"

class Config:
    # Коды торговых серверов
    TradeServerCode = 'TRADE'  # Рынок Ценных Бумаг
    ITradeServerCode = 'ITRADE'  # Рынок Иностранных Ценных Бумаг
    FutServerCode = 'FUT1'  # Фьючерсы
    OptServerCode = 'OPT1'  # Опционы
    FxServerCode = 'FX1'  # Валютный рынок

    # Для реального счета:
    # 1. Привязать торговый аккаунт
    # 2. Выписать токен
    UserName = 'P082290'
    RefreshToken = '08eae502-8387-4d52-9d62-0a4640c28927'

    # Как заполнять переменные портфелей:
    # 1. Запустить скрипт "Examples/02 - Accounts.py"
    # 2. Получить портфели для всех рынков
    # 3. Заполнить переменные полученными значениями
    PortfolioStocks = 'D82290'  # Фондовый рынок
    PortfolioFutures = '750296L'  # Срочный рынок
    PortfolioFx = 'G48983'  # Валютный рынок

    # Для демо счета:
    # 1. Пройти по ссылке "Токены для ведения торгов в тестовом контуре" - "Begin OAuth authorization flow"
    # 2. Ввести тестовый логин/пароль. Нажать "Разрешить"
    DemoUserName = 'P000000'
    DemoRefreshToken = 'ffffffff-ffff-ffff-ffff-ffffffffffff'

    # Как заполнять переменные портфелей:
    # 1. Запустить скрипт "Examples/02 - Accounts.py"
    # 2. Получить портфели для всех рынков
    # 3. Заполнить переменные полученными значениями
    DemoPortfolioStocks = 'D00000'  # Фондовый рынок
    DemoPortfolioFutures = '0000000'  # Срочный рынок
    DemoPortfolioFx = 'G00000'  # Валютный рынок
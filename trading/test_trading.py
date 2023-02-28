import yfinance as yf
from datetime import datetime, timedelta
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import SGDRegressor
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import os
import warnings
import platform
warnings.filterwarnings('ignore')

if platform.uname().system == 'Linux':
    os.system('clear')
else:
    os.system('cls')

n_inputs = 100

class Test:
    def __init__(self, currency, initial_amount, algorithm, interval):
        self.algorithm = algorithm
        self.interval = interval
        start = datetime(2000, 1, 1)
        end = datetime(2021, 12, 31)

        df = yf.download(currency, start=start, end=end, interval='1d')
        self.data = ((df.High + df.Low) / 2)
        self.model = self.get_model()

        df = yf.download(currency, start=start, end=datetime.now(), interval='1d')
        self.full_data = ((df.High + df.Low) / 2)

        self.test_date = datetime(2022, 1, 1)

        self.USD = initial_amount
        self.coin = 0

        self.status = 'None'

    def convert(self):
        data1 = []
        data = self.data.tolist()
        for i in range(len(data)):
            try:
                data1 += data[i:i+n_inputs+1]
            except:
                break
        data1 = np.array(data1).reshape(-1, n_inputs+1)
        x = data1[:, :-1]
        y = data1[:, -1].reshape(-1, 1)
        return x, y
    
    def get_model(self):
        model = make_pipeline(StandardScaler(), self.algorithm)
        x, y = self.convert()
        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.3)
        model.fit(x_train, y_train)
        print(f'Training Score: {model.score(x_train, y_train):.5f}')
        print(f'Score: {model.score(x_test, y_test):.5f}')
        return model
    
    def get_last_100_data(self):
        end = self.test_date
        start = end - timedelta(days=n_inputs-1)
        df = self.full_data.loc[start:end]
        self.test_date += timedelta(days=self.interval)
        return df.tolist()
    
    def predict(self, data):
        try:
            return self.model.predict([data])[0][0]
        except IndexError:
            return self.model.predict([data])[0]

    def buy(self, coin_price):
        if self.USD != 0:
            self.coin = self.USD / coin_price
            self.USD = 0
            self.status = 'Buy'
        
    def sell(self, coin_price):
        if self.coin != 0:
            self.USD = self.coin * coin_price
            self.coin = 0
            self.status = 'Sell'

    def balance(self, coin_price):
        return self.coin * coin_price + self.USD

    def run(self):
        balance_data = []
        date_data = []
        price_data = []

        while self.test_date <= datetime.now()-timedelta(days=1):
            data = self.get_last_100_data()
            coin_price = data[-1]
            prediction = self.predict(data)
            self.status = 'None'
            if prediction > coin_price:
                self.buy(coin_price)
            else:
                self.sell(coin_price)

            balance_data.append(self.balance(coin_price))
            date_data.append(self.test_date - timedelta(days=1))
            price_data.append(coin_price)

            print(f'Balance: ${self.balance(coin_price):.2f}, {self.status}, Date: {self.test_date - timedelta(days=1):%d-%m-%Y}')
        print(f'Balance: ${self.balance(coin_price):.2f}')
        plt.plot(date_data, balance_data, label='Balance')
        plt.plot(date_data, price_data, label='Price')
        plt.legend()
        plt.grid()
        plt.show()

algo = SGDRegressor()

test = Test('TRX-INR', 10, algo, 1)
test.run()
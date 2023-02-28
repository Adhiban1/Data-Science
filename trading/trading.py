import yfinance as yf
from datetime import datetime, timedelta
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
import os
os.system('clear')
n_inputs = 100

class Trading:
    def __init__(self, coinpair):
        end = datetime.now()
        start = datetime(2000, 1, 1)
        df = yf.download(coinpair, start=start, end=end, interval='1d')
        # os.system('clear')
        self.data = ((df.High + df.Low)/2).tolist()
        print(f'Length: {len(self.data)}')
        self.model = self.get_model()

    def convert(self):
        data1 = []
        for i in range(len(self.data)):
            try:
                data1 += self.data[i:i+n_inputs+1]
            except:
                break
        data1 = np.array(data1).reshape(-1, n_inputs+1)
        x = data1[:, :-1]
        y = data1[:, -1].reshape(-1, 1)
        return x, y

    def get_model(self):
        model = make_pipeline(StandardScaler(), LinearRegression())
        x, y = self.convert()
        x_train, x_test, y_train, y_test = train_test_split(
            x, y, test_size=0.3)
        model.fit(x_train, y_train)
        print(f'Training Score: {model.score(x_train, y_train)}')
        print(f'Score: {model.score(x_test, y_test)}')
        return model

    def predict(self, data):
        return self.model.predict(data)

    def tomorrow_price(self):
        data = self.data[-n_inputs:]
        return self.predict([data])[0][0]

    def today_price(self):
        return self.data[-1]
        
t = Trading('BNB-USD')
tomorrow_price = t.tomorrow_price()
today_price = t.today_price()
print(f'Tomorrow Price: {tomorrow_price}')
print(f'Today Price: {today_price}')
diff = tomorrow_price - today_price
percent = diff * 100 / today_price
print(f'Diff: {diff}')
print(f'Percent: {percent:.2f}%')
if diff > 0:
    print('Buy now')
else:
    print('Sell now')
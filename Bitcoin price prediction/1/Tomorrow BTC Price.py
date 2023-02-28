from tensorflow.keras.models import load_model
import pandas_datareader as pdr
from colorama import Fore
import datetime as dt
import pandas as pd
import colorama

colorama.init(autoreset=True)
#days = int(input('Days = '))
df = pdr.DataReader('BTC-USD', 'yahoo', dt.datetime.now()-dt.timedelta(days=50), dt.datetime.now())
data = df.Open.to_numpy()[-50:]

model = load_model('Trained Models/Bitcoin50')

prediction = model.predict(data.reshape(1, -1))[0][0]
last_price = data[-1]
diff = prediction - last_price

if diff > 0:
    color = Fore.GREEN
else:
    color = Fore.RED

print(f'{Fore.CYAN}{last_price} -> {prediction} {Fore.WHITE}| {color}{diff}')
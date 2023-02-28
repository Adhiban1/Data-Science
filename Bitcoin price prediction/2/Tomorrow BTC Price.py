import warnings
warnings.filterwarnings('ignore')
import colorama
from colorama import Fore
colorama.init(autoreset=True)
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
print(f'\n{Fore.RED}Importing files...\n')
from tensorflow.keras.models import load_model
import pandas_datareader as pdr
import datetime as dt
import numpy as np
import pandas as pd

#days = int(input('Days = '))
print(f'{Fore.YELLOW}Importing BTC Historical Data...\n')
df = pdr.DataReader('BTC-USD', 'yahoo', dt.datetime.now()-dt.timedelta(days=50), dt.datetime.now())
data = df.Open.to_numpy()[-50:]

print(f'{Fore.GREEN}Getting [Bitcoin50 2.0]...\n')
model = load_model('Bitcoin50 2.0')

print(f'{Fore.MAGENTA}Working on Prediction...\n')
prediction = np.argmax(model.predict(data.reshape(1, -1))[0][0])

if prediction == 1:
    print(f'\n{Fore.CYAN}Tomorrow Price: {Fore.GREEN}[UP]\n')
else:
    print(f'\n{Fore.CYAN}Tomorrow Price: {Fore.RED}[DOWN]\n')
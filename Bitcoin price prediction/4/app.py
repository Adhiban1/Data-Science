import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

print('importing files...')
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import pandas_datareader as pdr
import datetime as dt
import numpy as np

print('importing Tensorflow Model...')
model = load_model('model')

start = dt.datetime.now() - dt.timedelta(days=60)
end = dt.datetime.now()

print('Getting BTC-INR data...')
df = pdr.DataReader('BTC-INR', 'yahoo', start, end)

print('Predicting...')
result = np.concatenate([df.Close.to_numpy()[-10:],
model.predict(df.Close.to_numpy()[-50:].reshape(1, -1), verbose=0)[0]])
print('Result:')
print(result)

plt.grid()
plt.plot(result, '-o')
plt.show()

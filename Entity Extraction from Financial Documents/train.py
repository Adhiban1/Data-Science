from glob import glob
import pandas as pd
# from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle
import os

# CustomLabelEncoder
class LabelEncoder:
    def __init__(self):
        self.d = {}
        self.d_inv = {}
    
    def fit_transform(self, x):
        self.d = {}
        self.d_inv = {}
        for i, j in enumerate(x.unique()):
            self.d[j] = i
            self.d_inv[i] = j
        return x.apply(lambda x: self.d.get(x))
    
    def transform(self, x):
        m = max(self.d.values()) + 1
        def convert(a):
            n = self.d.get(a)
            if n == None: return m
            else: return n
        return x.apply(convert)

    def inverse_transform(self, x):
        def convert(a):
            s = self.d_inv.get(a)
            if s == None: return "UNKNOWN"
            else: return s
        return x.apply(convert)

def get_train_df(loc):
    return pd.read_csv(
        loc, header=None, 
        names=['start_index', 'end_index', 'x_top_left',
               'y_top_left', 'x_bottom_right', 'y_bottom_right',
               'transcript', 'field'])

def train_transcripts():
    transcripts = glob('dataset/train/boxes_transcripts_labels/*')
    return pd.concat([get_train_df(loc) for loc in transcripts]) \
        .reset_index(drop=True)

def train_clean_transcripts():
    df = train_transcripts()
    print(df)
    label_encoder_x = LabelEncoder()
    label_encoder_y = LabelEncoder()
    df['transcript'] = label_encoder_x.fit_transform(df['transcript'])
    df['field'] = label_encoder_y.fit_transform(df['field'])
    return df.drop('field', axis=1), df['field'], label_encoder_x, label_encoder_y

def Model(x, y):
    model = LogisticRegression(verbose=2)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
    model.fit(x_train, y_train)
    score = model.score(x_test, y_test)
    model = LogisticRegression(verbose=2)
    model.fit(x, y)
    print("Score:", score)
    return model

def save_model_encoder(model, label_encoder_x, label_encoder_y):
    if not os.path.exists('models'):
        os.mkdir('models')
    with open('models/model.pickle', 'wb') as f:
        pickle.dump(model, f)
    with open('models/label_encoder_x.pickle', 'wb') as f:
        pickle.dump(label_encoder_x, f)
    with open('models/label_encoder_y.pickle', 'wb') as f:
        pickle.dump(label_encoder_y, f)

if __name__ == '__main__':
    x, y, label_encoder_x, label_encoder_y = train_clean_transcripts()
    model = Model(x, y)
    save_model_encoder(model, label_encoder_x, label_encoder_y)
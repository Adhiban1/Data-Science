from glob import glob
import pandas as pd
from train import LabelEncoder
import pickle
import os
from tqdm import tqdm

def load_models():
    with open('models/model.pickle', 'rb') as f:
        model = pickle.load(f)
    with open('models/label_encoder_x.pickle', 'rb') as f:
        label_encoder_x = pickle.load(f)
    with open('models/label_encoder_y.pickle', 'rb') as f:
        label_encoder_y = pickle.load(f)
    return model, label_encoder_x, label_encoder_y

def get_val_df(loc):
    return pd.read_csv(
        loc, header=None, 
        names=['start_index', 'end_index', 'x_top_left',
               'y_top_left', 'x_bottom_right', 'y_bottom_right',
               'transcript'])

def val_transcripts():
    transcripts = glob('dataset/val/boxes_transcripts/*')
    return pd.concat([get_val_df(loc) for loc in transcripts]) \
        .reset_index(drop=True)

def val_clean_transcripts(x, label_encoder_x):
    x['transcript'] = label_encoder_x.transform(x['transcript'])
    return x

def total_output(x, store=False, name='output.csv'):
    model, label_encoder_x, label_encoder_y = load_models()
    y = pd.Series(model.predict(val_clean_transcripts(x, label_encoder_x)))
    y = label_encoder_y.inverse_transform(y)
    x['field'] = y
    if store:
        x.to_csv(name, index=False)

def predctions():
    model, label_encoder_x, label_encoder_y = load_models()
    transcripts = os.listdir('dataset/val/boxes_transcripts')
    if not os.path.exists('dataset/predictions'):
        os.mkdir('dataset/predictions')
    for loc in tqdm(transcripts):
        x = get_val_df(os.path.join('dataset/val/boxes_transcripts', loc))
        y = pd.Series(model.predict(val_clean_transcripts(x, label_encoder_x)))
        y = label_encoder_y.inverse_transform(y)
        x['field'] = y
        x.to_csv(os.path.join('dataset/predictions', loc), index=False)

if __name__ == "__main__":
    total_output(val_transcripts(), True)
    predctions()
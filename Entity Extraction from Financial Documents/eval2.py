import os
import pandas as pd
from tqdm import tqdm
import random

def get_df(loc):
    return pd.read_csv(
        loc, header=None, 
        names=['start_index', 'end_index', 'x_top_left',
               'y_top_left', 'x_bottom_right', 'y_bottom_right',
               'transcript', 'field'])

files = os.listdir('dataset/predictions')

# Accuracy with `OTHER`
acc = 0
for loc in tqdm(files):
    val_w_ann = get_df(os.path.join('dataset/val_w_ann/boxes_transcripts_labels', loc))
    predict = get_df(os.path.join('dataset/val_w_ann/boxes_transcripts_labels', loc))
    arr = val_w_ann['field'] == predict['field']
    acc += arr.sum()/len(arr)

acc = acc/len(files)
print(f"\nAccuracy with `OTHER`: {acc}\n")

# Accuracy without `OTHER`
acc = 0
for loc in tqdm(files):
    val_w_ann = get_df(os.path.join('dataset/val_w_ann/boxes_transcripts_labels', loc))
    predict = get_df(os.path.join('dataset/val_w_ann/boxes_transcripts_labels', loc))
    temp = val_w_ann['field'] != 'OTHER'
    arr = val_w_ann['field'][temp] == predict['field'][temp]
    acc += arr.sum()/len(arr)

acc = acc/len(files)
print(f"\nAccuracy without `OTHER`: {acc}\n")

print('Press enter to see sample data... ', end='')
input()
print()

# sample output
loc = random.choice(files)
val_w_ann = get_df(os.path.join(
    'dataset/val_w_ann/boxes_transcripts_labels', 
    loc))
predict = get_df(os.path.join(
    'dataset/val_w_ann/boxes_transcripts_labels', 
    loc))
print('val - predict')
for i,j in zip(val_w_ann['field'], predict['field']):
    print(f'{i} - {j}')

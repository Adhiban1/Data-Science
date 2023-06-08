# Entity Extraction from Financial Documents: EDA, Model Analysis, and Error Insights

## Train
```
python train.py
```

This will create a model that fitted with train dataset (dataset/train/boxes_transcripts_labels) and it creates LabelEncoder for x and y in models folder.

**Output**
```
Score: 0.99
```

## Predict

```
python predict.py 
```

**Output**
```
100%|███████████████████████████| 207/207 [00:01<00:00, 117.17it/s]
```
This takes all the tsv files from `dataset/val/boxes_transcripts` and predicts the y value and combines that y to x in `field` column and save it as the same file name in the dir `dataset/predictions`

## Eval

```
python eval2.py
```

**Output**

```
100%|██████████████████████████████████████████████████████████████████████████████████| 207/207 [00:01<00:00, 103.51it/s]

Accuracy with `OTHER`: 0.9899141958838814

100%|██████████████████████████████████████████████████████████████████████████████████| 207/207 [00:00<00:00, 239.58it/s]

Accuracy without `OTHER`: 0.9171185765543208

Press enter to see sample data...  
```

This will printout that accuracy in both with 'OTHER' and without 'OTHER'

And it shows `Press enter to see sample data... ` 

**Output**

```
val - predict
box1WagesTipsAndOtherCompensations - box1WagesTipsAndOtherCompensations
box2FederalIncomeTaxWithheld - box2FederalIncomeTaxWithheld
box1WagesTipsAndOtherCompensations - box1WagesTipsAndOtherCompensations
box2FederalIncomeTaxWithheld - box2FederalIncomeTaxWithheld
...
...
OTHER - OTHER
OTHER - OTHER
```

import pickle

with open('deliveryModel.pickle', 'rb') as f:
    model = pickle.load(f)

print(model.__doc__)
print(model.predict([[0]*10])[0])

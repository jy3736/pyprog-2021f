import pickle
import os
from sklearn import neighbors

ROOT = os.path.dirname(__file__)
ROOT = '.' if (ROOT=='') else ROOT

FF = f"{ROOT}\\feature.pickle"
TF = f"{ROOT}\\target.pickle"
MF = f"{ROOT}\\model.pickle"

with open(FF, 'rb') as f:
    feature = pickle.load(f)
with open(TF, 'rb') as f:
    target = pickle.load(f)

model = neighbors.KNeighborsRegressor(5, weights='uniform')
model.fit(feature, target)

with open(MF, 'wb') as f:
    pickle.dump(model, f)
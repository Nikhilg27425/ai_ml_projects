import numpy as np
import pandas as pd
from sklearn import neighbours , metrics
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder 

data = pd.read_csv('car.data')
print(data.head())


X = data[[
    'buying' ,
    'maint' ,
    'safety'
]]

y = data[['class']]

print(X,y)


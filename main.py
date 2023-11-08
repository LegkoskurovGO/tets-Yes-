import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pprint import pprint
import numpy as np
# import catboost
train = pd.read_csv('train_amazon.csv', index_col=0).astype(object)
test = pd.read_csv('test_amazon.csv', index_col=0).astype(object).drop('id', axis=1)

data = pd.concat([train, test], axis=0, ignore_index=True)

print(data.columns)


data.info()
# print(f'Кол-во{sum(data.isna())}')

# print(train.head())
print(data.shape)
# print(train.columns)
# train.info()
# print(train.nunique())
# print(f'\nДлина датасета: {train.shape[0]}')

# train_1 = train.query('ACTION == 1').reset_index(drop=True)
# train_0 = train.query('ACTION == 0').reset_index(drop=True)
# tmp_1 = train_1.nunique()
# tmp_0 = train_0.nunique()

# res = pd.concat([tmp_1, tmp_0], axis=1)
# print(res.head(10))
# 
# sns.scatterplot(x='ROLE_CODE', y='ROLE_TITLE', data=train)
# plt.show()


train.info()
print(f'Nunique: train\n{train.nunique()}\n\n')

train_1 = train.query('ACTION == 1').reset_index(drop=True)
train_0 = train.query('ACTION == 0').reset_index(drop=True)

res = pd.concat([train.nunique(), train_0.nunique(), train_1.nunique()], axis=1)
res.columns = ['All', 'A0', 'A1']
print(res)

print()

# print('\n'*4)


train_1 = data.query('ACTION == 1').reset_index(drop=True)
train_0 = data.query('ACTION == 0').reset_index(drop=True)

res = pd.concat([data.nunique(), train_0.nunique(), train_1.nunique()], axis=1)
res.columns = ['All', 'A0', 'A1']
print(res)

group = train.groupby("ACTION", as_index=False).agg({"ROLE_FAMILY": "unique"}).reset_index(drop=True)

all_uniq = set(train["ROLE_FAMILY"])

x = group[group['ACTION'] == 0]["ROLE_FAMILY"]
a0 = set(x.to_numpy()[0])
x1 = group[group['ACTION'] == 1]["ROLE_FAMILY"]
a1 = set(x1.to_numpy()[0])

tiff0 = all_uniq - a1
tiff1 = all_uniq - a0
print(all_uniq - a0)


dic = {"ACTON=1" : tiff1, "ACTION=0" : tiff0}
pprint(dic)
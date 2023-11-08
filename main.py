import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from pprint import pprint
import numpy as np
# import catboost

from funcs import *

'''Скачиваем данные'''
train = pd.read_csv('train_amazon.csv', index_col=0).astype(object)
test = pd.read_csv('test_amazon.csv', index_col=0).astype(object).drop('id', axis=1)

data = pd.concat([train, test], axis=0, ignore_index=True)

'''Предварительный просмотр данных'''
# print(data.columns)
# data.info()
# print(train.head())
print(train.shape)
# print(train.columns)
# train.info()
# print(train.nunique())
# print(f'\nДлина датасета: {train.shape[0]}')

# Число уникальных значений сгруппированных по ACTION из train
nuniques_df(train, 'ACTION', 'train')


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

# Число уникальных значений сгруппированных по ACTION из data
nuniques_df(data, 'ACTION', 'data')


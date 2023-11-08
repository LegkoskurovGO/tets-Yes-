import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
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

# Число уникальных значений сгруппированных по ACTION из data
nuniques_df(data, 'ACTION', 'data')

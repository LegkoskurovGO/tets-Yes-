import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
# import catboost

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

'''Число уникальных значений сгруппированных по ACTION из train'''
train_1 = train.query('ACTION == 1').reset_index(drop=True)
train_0 = train.query('ACTION == 0').reset_index(drop=True)

res_train = pd.concat([train.nunique(), train_0.nunique(), train_1.nunique()], axis=1)
res_train.columns = ['All', 'A0', 'A1']
print(f'Only train: \n{res_train}')

'''Число уникальных значений сгруппированных по ACTION из data'''
data_1 = data.query('ACTION == 1').reset_index(drop=True)
data_0 = data.query('ACTION == 0').reset_index(drop=True)

res_data = pd.concat([data.nunique(), data_0.nunique(), data_1.nunique()], axis=1)
res_data.columns = ['All', 'A0', 'A1']
print(f'All data: \n{res_data}')


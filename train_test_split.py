#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn.model_selection import train_test_split

def split_dataset(dataset, test_size=0.2, random_state=None):
    """
    Функция для деления датасета на обучающую и тестовую выборки.
    
    Аргументы:
    - dataset: numpy-массив или список
    - test_size: доля тестовой выборки (по умолчанию 20%)
    - random_state: для генерации случайной последовательности
    
    Возвращает tuple с четырьмя элементами:
    - X_train: numpy-массив с обучающими признаками
    - X_test: numpy-массив с тестовыми признаками
    - y_train: numpy-массив с обучающими метками
    - y_test: numpy-массив с тестовыми метками
    """
    # Разделяем признаки и метки
    X = dataset[:, :-1]
    y = dataset[:, -1]
    
    # Делаем разделение на обучающую и тестовую выборки
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    
    return X_train, X_test, y_train, y_test


# In[ ]:


dataset = load_dataset()


# In[ ]:


X_train, X_test, y_train, y_test = split_dataset(dataset)


# In[ ]:


import numpy as np
from sklearn.model_selection import train_test_split
 
X, y = np.arange(1000).reshape((500, 2)), np.arange(500)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2, 
    random_state=42
)


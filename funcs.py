import pandas as pd


def nuniques_df(dataframe: pd.DataFrame, grouper: str, name: str) -> None:
    group_keys_ = dataframe.groupby(grouper).groups.keys()
    tmp = [dataframe[dataframe[grouper] == i].nunique() for i in group_keys_]
    res = pd.concat([dataframe.nunique(), *tmp], axis=1)
    res.columns = ['All', *group_keys_]
    print(f'Группируем {name} по {grouper}: \n{res}')
    
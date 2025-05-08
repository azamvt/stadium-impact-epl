import pandas as pd

# Загрузка данных для разных сезонов
df_2000_2017 = pd.read_csv("/Users/azamatmurat/PycharmProjects/stadium-impact-epl/data/final_dataset.csv")
df_2018_2022_1 = pd.read_csv("/Users/azamatmurat/PycharmProjects/stadium-impact-epl/data/2018-19.csv")
df_2018_2022_2 = pd.read_csv("/Users/azamatmurat/PycharmProjects/stadium-impact-epl/data/2019-20.csv")
df_2018_2022_3 = pd.read_csv("/Users/azamatmurat/PycharmProjects/stadium-impact-epl/data/2020-2021.csv")
df_2018_2022_4 = pd.read_csv("/Users/azamatmurat/PycharmProjects/stadium-impact-epl/data/2021-2022.csv")

# Объединение всех файлов
all_data = pd.concat([df_2000_2017, df_2018_2022_1, df_2018_2022_2, df_2018_2022_3, df_2018_2022_4], ignore_index=True)

# Сохранение объединенного датафрейма в новый файл
all_data.to_csv("all_seasons_combined.csv", index=False)

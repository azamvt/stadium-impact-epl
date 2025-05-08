import pandas as pd

# Загружаем объединённый датасет
df = pd.read_csv("/Users/azamatmurat/PycharmProjects/stadium-impact-epl/all_seasons_combined.csv")

# Преобразуем столбец Date в datetime
df['Date'] = pd.to_datetime(df['Date'])

# Печатаем первые несколько строк, чтобы убедиться, что данные загружены правильно
print(df.head())

# Проверим структуру данных
print(df.info())

# Простой анализ: количество матчей, сыгранных каждой командой дома
home_games = df.groupby('HomeTeam').size()
print(home_games)

# Анализ побед домашних команд (FTHG - Full Time Home Goals > FTAG - Full Time Away Goals)
home_wins = df[df['FTHG'] > df['FTAG']].groupby('HomeTeam').size()
print(home_wins)

# Процент побед домашних команд
home_win_percentage = home_wins / home_games * 100
print(home_win_percentage)

# Среднее количество голов домашних и гостевых команд
average_home_goals = df['FTHG'].mean()
average_away_goals = df['FTAG'].mean()
print(f"Среднее количество голов домашних команд: {average_home_goals}")
print(f"Среднее количество голов гостевых команд: {average_away_goals}")

# Пример анализа по стадиону (предположим, что у нас есть столбец 'Stadium' с данными о стадионе)
# Если столбца "Stadium" нет, можно пропустить этот блок или добавить соответствующие данные.
# stadium_wins = df.groupby('Stadium').apply(lambda x: (x['FTHG'] > x['FTAG']).mean() * 100)
# print(stadium_wins)

# Сохраняем результаты в файл (если нужно)
# home_win_percentage.to_csv("/path/to/home_win_percentage.csv")

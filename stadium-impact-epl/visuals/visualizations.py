import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка данных
df = pd.read_csv("../all_seasons_combined.csv")
df['Date'] = pd.to_datetime(df['Date'])

# Победы дома
home_wins = df[df['FTHG'] > df['FTAG']]['HomeTeam'].value_counts()
home_matches = df['HomeTeam'].value_counts()
home_win_pct = (home_wins / home_matches) * 100

# Удалим команды с малым числом домашних матчей (<20), чтобы не засорять график
home_win_pct = home_win_pct[home_matches >= 20]

# Построим график
plt.figure(figsize=(12, 10))
home_win_pct.sort_values().plot(kind='barh', color='skyblue')
plt.title("Home Win Percentage by Team (min 20 home games)", fontsize=16)
plt.xlabel("Win Percentage (%)")
plt.tight_layout()
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()

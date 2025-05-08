import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("../all_seasons_combined.csv", low_memory=False)
df['Date'] = pd.to_datetime(df['Date'])

# Create a column indicating match result
def match_result(row):
    if row['FTHG'] > row['FTAG']:
        return 'Home Win'
    elif row['FTHG'] < row['FTAG']:
        return 'Away Win'
    else:
        return 'Draw'

df['Result'] = df.apply(match_result, axis=1)

# Count the number of each match result
result_counts = df['Result'].value_counts()

# Visualization: Pie chart of match outcomes
plt.figure(figsize=(7, 7))
plt.pie(
    result_counts,
    labels=result_counts.index,
    autopct='%1.1f%%',
    startangle=140,
    colors=['skyblue', 'lightgreen', 'salmon']
)
plt.title('Match Outcome Distribution (All Seasons)')
plt.tight_layout()
plt.show()

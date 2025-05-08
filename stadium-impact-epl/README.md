Stadium Impact on EPL Performance Analysis
This project analyzes the impact of stadiums and home games on the performance of football teams in the English Premier League (EPL) over multiple seasons. The goal is to investigate trends in team performance based on home and away games, as well as the influence of stadium-related factors such as stadium capacity.

Project Overview
In this project, we:

Merged multiple datasets from the English Premier League (EPL) seasons (2000-2022).

Performed data cleaning and preprocessing to prepare the data for analysis.

Analyzed key statistics, such as the number of goals scored by home and away teams.

Created visualizations to reveal trends and patterns in team performance.

Explored factors that may influence match outcomes, including home advantage and stadium characteristics.

Data
The project utilizes multiple datasets, including:

final_dataset.csv: Data for EPL seasons from 2000-2017.

separate CSV files: Data for the seasons from 2018-2022, including 2018-2019.csv, 2019-2020.csv, 2020-2021.csv, and 2021-2022.csv.

Stadium Data: Information about each team's home stadium, including capacity, which is used to explore the potential influence of stadium size on performance.

Project Structure
stadium-impact-epl/
│
├── data/
│   ├── final_dataset.csv             # Combined data for seasons 2000-2017
│   ├── 2018-2019.csv                # Data for 2018-2019 season
│   ├── 2019-2020.csv                # Data for 2019-2020 season
│   ├── 2020-2021.csv                # Data for 2020-2021 season
│   ├── 2021-2022.csv                # Data for 2021-2022 season
│   └── all_seasons_combined.csv     # Merged dataset of all seasons
│
├── visuals/
│   └── visualizations.py            # Python script for generating visualizations
│
├── stadium_impact_analysis.py       # Main script for performing the analysis
├── data_processing.py               # Script for data cleaning and preprocessing
└── README.md                        # This file
Analysis
The main objective of this project was to understand how playing at home affects team performance in the EPL. Key findings include:

Home advantage: Home teams generally scored more goals than away teams across multiple seasons.

Goal trends: There were noticeable patterns in goal-scoring over the years, with some seasons showing higher overall scoring.

Stadium capacity: Larger stadiums did not directly correlate with a higher number of goals scored, but this analysis could be expanded further by considering other stadium characteristics.

Visualizations
Several visualizations were created to illustrate the key trends in the data:

Average Goals per Season: Displays the trend of goal-scoring for both home and away teams over time.

Goals by Home and Away Teams: Shows the number of goals scored by home vs. away teams, with comparisons between different seasons.

Home vs. Away Goals Comparison: Visualizes the difference in performance between home and away games over multiple seasons.

Requirements
To run this project, you will need to install the following Python libraries:

pandas – For data manipulation and analysis.

matplotlib – For data visualization.

seaborn – For enhanced data visualization (optional but recommended).

numpy – For numerical calculations.

Install the required libraries using pip:

pip install pandas matplotlib seaborn numpy
Running the Analysis
To execute the analysis, simply run the stadium_impact_analysis.py script:


python stadium_impact_analysis.py
For generating the visualizations, use the visualizations.py script:


python visuals/visualizations.py
Next Steps
Future work can involve expanding the analysis to include:

Stadium characteristics: Investigating how stadium size, location, or other attributes impact team performance.

Impact of specific players and managers: Analyzing the influence of key players or managerial changes on team success.

Advanced statistical methods: Implementing more advanced statistical tests or machine learning models to predict match outcomes based on historical data.


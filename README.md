# Stadium Impact on EPL Performance Analysis

## Project Overview
This project analyzes the impact of stadiums and home games on the performance of football teams in the English Premier League (EPL) over multiple seasons. The goal is to investigate trends in team performance based on home and away games, as well as the influence of stadium-related factors such as stadium capacity.

## How to Upload Project Files to GitHub Manually

If you'd like to upload your project files to GitHub without using the terminal, you can follow these steps:

### 1. Prepare Your Project Files
Make sure all the necessary files for your project are organized in a folder on your computer. This includes all the scripts, datasets, and any other relevant files for the project.

### 2. Create a New Repository on GitHub
1. Go to [GitHub](https://github.com/) and log in to your account.
2. Click on the **"+"** button at the top-right corner of the page and select **"New repository"**.
3. Give your repository a name (e.g., `stadium-impact-epl`).
4. Set the repository visibility to either **public** or **private**.
5. Click **"Create repository"** to finish creating the repository.

### 3. Upload Your Project Files
1. After creating the repository, you'll be redirected to a page with different options for uploading files. To upload files manually:
   - Click on the **"Add file"** button (or **"Upload files"**).
   - Drag and drop your project files into the upload area, or use the **"Choose your files"** button to select them from your computer.
2. Once the files have been uploaded, scroll down and click on **"Commit changes"** to save them to the repository.

### 4. Done!
Your project is now uploaded to GitHub! You can share the link to your repository with others or continue to make changes to the project.

## Project Structure
stadium-impact-epl/

├── data/

│ ├── final_dataset.csv # Combined data for seasons 2000-2017

│ ├── 2018-2019.csv # Data for 2018-2019 season

│ ├── 2019-2020.csv # Data for 2019-2020 season

│ ├── 2020-2021.csv # Data for 2020-2021 season

│ ├── 2021-2022.csv # Data for 2021-2022 season

│ └── all_seasons_combined.csv # Merged dataset of all seasons

├── visuals/

│ └── visualizations.py # Python script for generating visualizations

├── stadium_impact_analysis.py # Main script for performing the analysis

├── data_processing.py # Script for data cleaning and preprocessing

└── README.md # This file


## Analysis
The main objective of this project was to understand how playing at home affects team performance in the EPL. Key findings include:

- **Home advantage**: Home teams generally scored more goals than away teams across multiple seasons.
- **Goal trends**: There were noticeable patterns in goal-scoring over the years, with some seasons showing higher overall scoring.
- **Stadium capacity**: Larger stadiums did not directly correlate with a higher number of goals scored, but this analysis could be expanded further by considering other stadium characteristics.

## Requirements
To run this project, you will need to install the following Python libraries:

- `pandas` – For data manipulation and analysis.
- `matplotlib` – For data visualization.
- `seaborn` – For enhanced data visualization (optional but recommended).
- `numpy` – For numerical calculations.

Install the required libraries using pip:
pip install pandas matplotlib seaborn numpy

## Running the Analysis
To execute the analysis, simply run the `stadium_impact_analysis.py` script:

python stadium_impact_analysis.py

For generating the visualizations, use the `visualizations.py` script:

python visuals/visualizations.py

## Next Steps
Future work can involve expanding the analysis to include:

- **Stadium characteristics**: Investigating how stadium size, location, or other attributes impact team performance.
- **Impact of specific players and managers**: Analyzing the influence of key players or managerial changes on team success.
- **Advanced statistical methods**: Implementing more advanced statistical tests or machine learning models to predict match outcomes based on historical data.

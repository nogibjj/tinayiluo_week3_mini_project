[![CI](https://github.com/nogibjj/python-template/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/python-template/actions/workflows/cicd.yml)
## Polars Descriptive Statistics Script

IDS 706 Mini-Project 3

Polars Descriptive Statistics Script

### Goal

+ establish a CodeSpaces environment that automates the process of loading a dataset using `Polars` and executing a `readfile` function to generate descriptive statistics on the dataset, utilizing GitHub Actions. 
  
+ create data visualizations of the dataset using `matplotlib`

+ create summary report using `Jupyter Notebook`

The workflow includes running a Makefile to perform tasks such as installation (`make install`), testing (`make test`), code formatting (`make format`), linting (`make lint`), and an all-inclusive task (`make all`). This automation streamlines the data analysis process and enhances code quality.

### Preperation

+ I used the IDS-706-Python-GitHub-template for this project. This template includes a `Makefile`, `requirements.txt`, `.devcontainer`, `.gitignore`, `GitHubActions`, and `Readme`.

+ I downloaded the `Heart Attack Analysis & Prediction Dataset` from Kaggle.

### Dataset Description

`Heart Attack Analysis & Prediction Dataset` (simplify as `heart.csv`) is a csv file containing related information of 302 randomly picked people and their respective information including age, sex, exercise induced angina, number of major vessels, chest pain type, resting blood pressure, cholestoral, fasting blood sugar, resting electrocardiographic results, and chances of heart attack.

#### [Resources](https://www.kaggle.com/datasets/rashikrahmanpritom/heart-attack-analysis-prediction-dataset) 

### Overview

This project creates a Python script using Polars for descriptive statistics. The specific steps involve: 

+ Create a Phython script

  + Read a dataset (CSV)

  + Generate summary statistics (mean, median, standard deviation)

  + Create data visualizations

+ Generate summary report (PDF)

### Description

Step 1: In the requirements.txt, I added polars==0.10.12. 

<img width="545" alt="Screen Shot 2023-09-17 at 12 02 11 AM" src="https://github.com/nogibjj/tinayiluo_week3_mini_project/assets/143360909/8862ce71-0cd7-4f50-986d-4f45b6529cf8">

Step 2: In the main.py, I created a Python Script using Polars. It includes:
       
       + a 'summary' function which generates summary statistics for the numeric columns in the DataFrame heart.csv.

       + a 'histogram_blood_pressure' function which generates histogram for the blood pressure column in heart.csv.

<img width="932" alt="Screen Shot 2023-09-17 at 12 10 20 AM" src="https://github.com/nogibjj/tinayiluo_week3_mini_project/assets/143360909/adeb83b4-fa2a-4a0e-889b-f58ce8afefa7">

Step 3: In the `test_main.py`, I wrote test functions `test_summary`, `test_histogram_blood_pressure`, which checks the summary statistics and data visualizations of `heart.csv`.

       + check the mean value of the age column 
       
       + check the median value of the age column 
       
       + check the standard deviation value of the age column

       + check histogram for the blood pressure column

<img width="820" alt="Screen Shot 2023-09-17 at 12 19 01 AM" src="https://github.com/nogibjj/tinayiluo_week3_mini_project/assets/143360909/4c121c11-4923-41af-b71a-9ef8849b4fd8">

Step 4: I generated Data Visualizations

+ summary statistics

<img width="1105" alt="Screen Shot 2023-09-17 at 12 40 12 AM" src="https://github.com/nogibjj/tinayiluo_week3_mini_project/assets/143360909/daf6237d-92fd-4083-82ab-b446b9d85caa">

+ histogram of resting blood pressure column

![image](https://github.com/nogibjj/tinayiluo_week3_mini_project/assets/143360909/b1b1d2d4-7600-4a74-a4ba-38c12ee054e4)

Step 5: I generated the summary report (PDF) from Jupyter Notebook

#### [Summary Report PDF](./summary_report.pdf)

### Check Format and Test Approval Image

+ install code `make install`
  
<img width="1026" alt="Screen Shot 2023-09-13 at 7 08 21 PM" src="https://github.com/nogibjj/tinayiluo_week3_mini_project/assets/143360909/abe5dc02-1947-4f68-9cad-0ffc35d1f0b9">

+ lint code `make lint`
+ format code `make format`
+ test code `make test`
  
<img width="1035" alt="Screen Shot 2023-09-13 at 7 08 41 PM" src="https://github.com/nogibjj/tinayiluo_week3_mini_project/assets/143360909/032a08cb-cc09-4a98-8a19-f9ef79b78140">

+ code `make all` executes install, lint, format, and test targets
  
<img width="1021" alt="Screen Shot 2023-09-13 at 7 09 10 PM" src="https://github.com/nogibjj/tinayiluo_week3_mini_project/assets/143360909/7e4c58b1-d42d-40f1-bbba-75325d408bf2">



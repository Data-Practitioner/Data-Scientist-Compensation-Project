# Data Scientist Compensation Project

## 1. Project Overview
This project is to predict the compensation of a Data Scientist using Stack Overflow data. Also, finding out which variables contribute to Data Scientist’s compensation.

### 1.1. Problem Statement
An HR company wants to understand how much Data Scientists can get compensated in the USA based on factors such as education, seniority, location (USA), experience, and technical knowledge.

### 1.2. Solution
Build a web application that compares actual vs predicted compensation based on factors such as education, seniority, location (USA), experience, and technical knowledge.

### 1.3. Tools
Data Storage - Excel <br>
Data Mining, Analysis, and Transform - Python (Pandas & Numpy) <br>
Data Science/ML - Python (Sklearn, Feature Engine, Scipy, Feature Tools, Statsmodel, LightGBM, XGBoost, and Catboost) <br>
Data Visualization - Python (Matplotlib & Seaborn)<br>
Web Application - Python (Streamlit) <br>
Application Hosting - Github <br>

### 1.4. Technical Skills
Data Analysis <br>
Data Mining <br>
Data Transformation <br>
Data Visualization <br>
Programming (Python) <br>
ML Deployment <br>
Web Application <br>
Data Storytelling <br>
Machine Learning <br>

### 1.5. End to End Process Flowchart
![image](https://user-images.githubusercontent.com/99619460/184925146-13245ee6-2ee9-4522-b89d-bc7b8f2600da.png)

## 2. Hypothesis Generation
Hypothesis generation is broken into three different categories.

**Demographic**

Is education a good estimate for predicting salary? <br>
Does a certain education level provide a better salary? <br>
Is seniority_level a good estimate for predicting salary? <br>
Does a certain seniority_level provide a better salary? <br>
Does age impact salary? <br>

**Geographic**

Is state_code a good estimate for predicting salary? <br>
Does a certain state provide a better salary? <br>

**Psychographic**

Does one knowing a programming language provide a better salary? <br>
Does one knowing SQL provide a better salary? <br>
Does one knowing the command line provide a better salary? <br>
Does one knowing cloud computing platform provide a better salary? <br>

## 3. Data Source
Data is collected from Stack Overflow Survey 2021 data.

https://insights.stackoverflow.com/survey?_ga=2.148200503.1852735476.1659374945-1267271718.1659374945

**Data Description**

• response_id  –  Developer’s response identification number on the survey <br>
• state – State of the developer <br>
• state_code –  State code of the developer <br>
• education –  Education of the developer <br>
• seniority_level  – Level of experience in the field of Data Science <br>
• compensation – Salary of developer <br>
• avg_age – Approximate age of the developer <br>
• language_python – Codes in Python (0 – No & 1 – Yes) <br>
• language_r – Codes in R  (0 – No & 1 – Yes) <br>
• language_sql – Codes in SQL  (0 – No & 1 – Yes) <br>
• language_bash_shell – Codes in Bash/Shell (0 – No & 1 – Yes) <br>
• language_java – Codes in Java (0 – No & 1 – Yes) <br> 
• language_javascript – Codes in Javascript (0 – No & 1 – Yes) <br>
• language_html_css  – Codes in HTML/CSS (0 – No & 1 – Yes) <br>
• platform_aws – Uses AWS platform (0 – No & 1 – Yes) <br>
• platform_gcp – Uses GCP platform (0 – No & 1 – Yes) <br>
• platform_azure – Uses Azure platform (0 – No & 1 – Yes) <br>
 
## 4. Data Science Pipeline

### 4.1. Data Cleaning

Below data cleaning steps were executed to use data for further analysis.

Filter rows where the country is USA and dev type is Data Scientist. <br>
Merge state_code file to the main file to get the corresponding state code values for each row. <br>
Categorized education level into 4 buckets (Bachelor, Master, Doctorate, and Other). <br>
Created seniority level column based on years of professional coding experience. <br>
Parsed salary column and calculated from monthly & weekly to annually. <br>
Cleaned age column. <br>
Created separate columns for each programming language used based on top 7 frequency. <br>
One hot encoded all the programming language columns to 1 (Yes) or 0 (No). <br>
Created separate columns for each cloud platform used. <br>
One hot encoded all the could platform columns to 1 (Yes) or 0 (No). <br>

Python Script - https://github.com/Data-Practitioner/Data-Scientist-Compensation-Project/blob/7c04ff293697e149d4936885f5946db45c64a9a4/data_science_pipeline/data_cleaning

### 4.2. EDA

Python Script - https://github.com/Data-Practitioner/Data-Scientist-Compensation-Project/blob/7c04ff293697e149d4936885f5946db45c64a9a4/data_science_pipeline/EDA.ipynb

### 4.3. Feature Engineering

Python Script - https://github.com/Data-Practitioner/Data-Scientist-Compensation-Project/blob/7c04ff293697e149d4936885f5946db45c64a9a4/data_science_pipeline/feature_engineering.ipynb

### 4.4. Feature Selection

Python Script - https://github.com/Data-Practitioner/Data-Scientist-Compensation-Project/blob/main/data_science_pipeline/feature_selection.ipynb

### 4.5. Model Building

Python Script - https://github.com/Data-Practitioner/Data-Scientist-Compensation-Project/blob/main/data_science_pipeline/model_building.ipynb

### 4.6. Model Evaluation

Python Script - https://github.com/Data-Practitioner/Data-Scientist-Compensation-Project/blob/main/data_science_pipeline/model_evaluation.ipynb

## 5. Model Deployment
Created a Steamlit web app so anyone can view it which is deploy using Streamlit Share as front end and Github repository as backend.

### 5.1. Containerize Application

Two files are required to deploy the file on the Github repository.

Streamlit Application File - https://github.com/Data-Practitioner/Data-Scientist-Compensation-Project/blob/main/github_app.py
Requirements Txt File - https://github.com/Data-Practitioner/Data-Scientist-Compensation-Project/blob/main/requirements.txt

### 5.2. Deploy Application
Both files are uploaded to Github Repository → Streamlit Share pointing to Github Repository to show the web application.

## Conclusion
Decision Tree Regression algorithm was used to run predictions on compensation.

The below link takes to the Streamlit application where predicted vs actual compensation results on different variables and categories are shown in the form of tabular data and visualization.

Website ⇒ https://share.streamlit.io/mkamdar7/streamlit-stackoverflow-app/main/github_app.py

![image](https://user-images.githubusercontent.com/99619460/184934622-849e0d73-8fc2-4aa6-a9b6-cf267edbb070.png)
![image](https://user-images.githubusercontent.com/99619460/184934643-af879e0b-fa71-4276-a131-3d71034a97db.png)

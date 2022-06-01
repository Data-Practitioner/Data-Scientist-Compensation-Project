# Import library.
import pandas as pd
import streamlit as st
import plotly.express as px

###################### Data Cleaning ######################

# Load the data into dataframe.
column_names = ['state_code', 'education', 'seniority_level','language_python', 'language_r','language_sql','language_bash_shell',
                'language_java', 'language_javascript','language_html_css','platform_aws','platform_gcp','platform_azure',
		'predicted_compensation', 'actual_compensation', 'compensation_difference']

url = "https://raw.githubusercontent.com/mkamdar7/Streamlit-Stackoverflow-app/main/stackoverflow_predicted_data.csv"
df = pd.read_csv(url, names=column_names) 

# Replace 'rare' with 'other' in state_code.
df['state_code'] = df['state_code'].replace(['Rare'], ['Other'], regex=True)

# Getting Python/R/SQL/Bash_Shell/Java/JavaScript/HTML_CSS as 'Yes' & 'No' values.
df['language_python'] = df['language_python'].replace(['0','1'], ['No','Yes'], regex=True)
df['language_r'] = df['language_r'].replace(['0','1'], ['No','Yes'], regex=True)
df['language_sql'] = df['language_sql'].replace(['0','1'], ['No','Yes'], regex=True)
df['language_bash_shell'] = df['language_bash_shell'].replace(['0','1'], ['No','Yes'], regex=True)
df['language_java'] = df['language_java'].replace(['0','1'], ['No','Yes'], regex=True)
df['language_javascript'] = df['language_javascript'].replace(['0','1'], ['No','Yes'], regex=True)
df['language_html_css'] = df['language_html_css'].replace(['0','1'], ['No','Yes'], regex=True)

# Getting AWS/GCP/Azure as 'Yes' & 'No' values.
df['platform_aws'] = df['platform_aws'].replace(['0','1'], ['No','Yes'], regex=True)
df['platform_gcp'] = df['platform_gcp'].replace(['0','1'], ['No','Yes'], regex=True)
df['platform_azure'] = df['platform_azure'].replace(['0','1'], ['No','Yes'], regex=True)

# Changing datatype for few columns.
df['predicted_compensation'] = df['predicted_compensation'].fillna(0).apply(pd.to_numeric,errors='coerce')
df['actual_compensation'] = df['actual_compensation'].fillna(0).apply(pd.to_numeric, errors='coerce')
df['compensation_difference'] = df['compensation_difference'].fillna(0).apply(pd.to_numeric, errors='coerce')

# Seperating all categorical columns.
categorical_cols = ['state_code', 'education', 'seniority_level','language_python', 'language_r','language_sql','language_bash_shell',
                    'language_java', 'language_javascript','language_html_css','platform_aws','platform_gcp','platform_azure']

# Seperating all numerical columns.
numerical_cols = ['actual_compensation', 'predicted_compensation', 'compensation_difference']

# Storing data for each variable and category to display predicted vs actual compensation.
variable = []
category = []
mean_pred_comp = []
mean_actual_comp = []
mean_comp_diff = []

# Looping through all categorical_variables.
for col in categorical_cols:
    
    # Get unique category for each categorical_variable.
    cat = pd.Categorical(df[col].unique())

    # Get category within each variable.
    for i in cat:
        
        # Getting a list of values for each category.
        num = df.loc[(df[col] == i)]
        category_data = num[numerical_cols]
    
        # Getting variable, category, actual and predicted compensation.
        variable.append(col)
        category.append(i)
        mean_pred_comp.append(round(df[df[col] == i]['predicted_compensation'].fillna(0).mean()))
        mean_actual_comp.append(round(df[df[col] == i]['actual_compensation'].fillna(0).mean())) 
        cd  = mean_comp_diff.append(round(df[df[col] == i]['predicted_compensation'].fillna(0).mean() - df[df[col] == i]['actual_compensation'].fillna(0).mean()))
  
# Creating a dataframe.    
data = pd.DataFrame({'variable': variable,
                     'category': category,
                     'avg_predicted_compensation': mean_pred_comp,
                     'avg_actual_compensation': mean_actual_comp,
                     'avg_compensation_difference': mean_comp_diff})

# Sorting and filtering data.
data = data[data['avg_predicted_compensation'] != '0']
data = data.sort_values(['variable', 'category'],ascending=[True, True])

###################### Data & Visualisation - Streamlit ######################

##### App Heading ######

# Adding Streamlit title.
st.title('Stack Overflow Compensation Project')

# Text content.
st.markdown("""
---
## Project Description

This project is to predict the compensation of a Data Scientist using Stack Overflow data. 
Also, finding out which variables contribute to Data Scientist’s compensation.

""")

##### App Section 1 ######

# Description of section 1 - Sidebar.
st.sidebar.markdown("""
                    
### Predicted vs Actual Average Compensation by Variable
#### 1. Data
Please select the variable to view data.                    
               
""")

# Description of section 1 - Main Page.
st.markdown("""       
### Predicted vs Actual Average Compensation by Variable
            
#### 1. Data
Please select the variable from the drop-down menu in the sidebar to view data.
        
""")

# Loading data.
def load_data():
	return data

data = load_data()

# Drop down menu for variable that will display data.
variable_list = list(data['variable'].unique())
variable_list.append('All')
variable_list.sort()

variable_list = st.sidebar.multiselect("Select Variable", variable_list)
st.sidebar.write(variable_list)

# Filtering data based on variable selected.
try:
    if 'All' in variable_list:
        filtered_data = data.copy()
    elif variable_list:
        filtered_data = data.loc[data['variable'].isin(variable_list)]
    st.dataframe(filtered_data, width=1500, height=500) 
except:
    pass
 
##### App Section 2 ######

# Description of section 2 - Sidebar.
st.sidebar.markdown("""
                    
#### 2. Chart
Please select the variable to view chart.   
          
""")

# Description of section 2 - Main Page.
st.markdown("""
            
#### 2. Chart
Please select the variable from the drop-down menu in the sidebar to view chart.        
""")

# Converting columns to numeric datatype.
convert_dict = {'avg_predicted_compensation': int,
                'avg_actual_compensation': int,
                'avg_compensation_difference': int}

data = data.astype(convert_dict)

# Drop down menu for variable that will display chart.
variable_list2 = list(df[categorical_cols].columns)
variable_list2.append('')
variable_list2.sort()

variable_list2 = st.sidebar.selectbox('Select Variable', variable_list2)

try:
    # Plot variables based on predicted compensation.
    fig1 = px.histogram(data_frame=df, x=variable_list2,  y='predicted_compensation', color=variable_list2, histfunc='avg',
                       barmode='group', height=500, text_auto='.0f', title='Predicted Average Compensation by Variable',
                       color_discrete_sequence=px.colors.qualitative.Bold)
    st.plotly_chart(fig1, use_container_width=True)
    
    # Plot variables based on actual compensation.
    fig2 = px.histogram(data_frame=df, x=variable_list2,  y='actual_compensation', color=variable_list2, histfunc='avg',
                       barmode='group', height=500, text_auto='.0f',  title='Actual Average Compensation by Variable',
                       color_discrete_sequence=px.colors.qualitative.Bold)
    st.plotly_chart(fig2, use_container_width=True)
except:
    pass
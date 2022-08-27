DATA_PATH = 'ds_project\src\data\stack-overflow-developer-survey-2020\survey_results_public.csv' ; 
import pandas as pd 
import numpy as np
pd.options.display.max_rows = 10000 

# Read data and print shape
raw_df = pd.read_csv(DATA_PATH)
raw_df.shape 

#print(raw_df.info)   --clear comment

# Display random answer 
# Observations: Multiple answers need to be splitted 
# Reference to the schema needed to understand
#print(raw_df.sample(1))    --clear comment

# Get stats for the numerical column

# Get stats for the numerical column
print (raw_df.info())

#  Investigate the questionable objects columns
questionable_cols = ['YearsCodePro', 'YearsCode']

for col in questionable_cols: 
    print(col)
    print(raw_df[col].unique().tolist())
    print('--------------------------')
    print()
    
    
    
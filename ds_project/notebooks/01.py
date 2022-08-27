# preprocessing

# Constants  --constants always in top  and in capital letter
DATA_PATH = 'ds_project\src\data\stack-overflow-developer-survey-2020\survey_results_public.csv' ; 
EXPORT_PATH = "../data/processed/1_preprocessed_df.pkl"

REPLACE_DICT = {
    'YearsCodePro': {'Less than 1 year': 0, 'More than 50 years': 51}, 
    'YearsCode':    {'Less than 1 year': 0, 'More than 50 years': 51}
} 



# Load packages
import pandas as pd 
import numpy as np
import logging
import pickle

# function    -- sholud make a doc  string ( explain what function do )

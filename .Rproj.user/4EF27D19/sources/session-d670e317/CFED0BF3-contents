#### Week 8 - Bob Ross ####
# Title: Cleaning Function
# Date: June 13, 2023
# Description: A function that takes
# in a data set and cleans it. 

#### Load Packages ####
# pandas: data analysis functions. 
import pandas as pd

#### Cleaning Function ####
def clean(df):
  clean_df = df.groupby(['season'])['num_colors'].sum()
  return(clean_df)

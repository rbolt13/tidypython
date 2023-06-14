#### Week 8 - Bob Ross ####
# Title: Main
# Date: June 14, 2023
# Description: This file loads in the
# necessary packages, functions, and data.
# Then it cleans the data, creates a data 
# visual, stylizes the visual, and saves the 
# visual as a png file. 

#### Location Packages ####
# pandas: data analysis functions. 
# matplotlib: static visualization functions. 
import pandas as pd
import matplotlib.pyplot as plt

#### Load Functions ####
# import functions

### Load Data ####
url = 'https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2023/2023-02-21/bob_ross.csv'
tt_data = pd.read_csv(url, header=0)

#### Clean Data ####
# clean_data = functions.clean(tt_data)
clean_data = tt_data.groupby(['season'])['num_colors'].sum()

#### Create Data Visual ####
# vis_data = functions.vis(clean_data)
vis, ax = plt.subplots()
# plot stem on ax 
ax.stem(clean_data.index, 
        clean_data.values,
        linefmt = 'k-',
        basefmt = 'k-')
# Labels
ax.set_title('Colors Used Each Season')
ax.set_ylabel('Count')
ax.set_xlabel('Season')

#### Save Plot ####
plt.savefig('plot.png')

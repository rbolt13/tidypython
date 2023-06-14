#### Week 8 - Bob Ross ####
# Title: Visual Function
# Date: June 14, 2023
# Description: A function that takes
# in a clean data set and creates a 
# data visual from it. 

#### Load Packages ####
# matplotlib: static visualization functions. 
import matplotlib.pyplot as plt

#### Visual Function ####
def vis(clean_df):
  # create a new fig and a set of subplots within that fig
  vis, ax = plt.subplots()
  # plot stem (lollipop) on ax 
  ax.stem(clean_data.season, 
          clean_data.total_num_colors,
          linefmt = 'k-',
          basefmt = 'k-')
  # Labels
  ax.set_title('Colors Used Each Season')
  ax.set_ylabel('Count')
  ax.set_xlabel('Season')
  return(vis)

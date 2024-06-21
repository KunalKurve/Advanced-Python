# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 18:38:14 2024

@author: Administrator
"""
#2. find all masala movie - (action ,romance,comedy,thriller)
# 3. plot a pie chart to represent genre and frequency of movie count
# 4. find average rating for each movie then merge 2 frames, display movieid,name,rating
# 5. draw pie chart for each genre and average rating
# 6. draw bar graph for each rating and number of movies

# Use pandas, numpy and matplotlib,seaborn
# 1. Use movies11.csv,movie12.csv,movie13.csv and rating11.csv file and solve following

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("rating11.csv")
print(df)
df1 = pd.read_csv("movies11.csv")
print(df1)

df2 = pd.read_csv("movie12.csv")
print(df2)


df3 = pd.read_csv("movies13.csv")
print(df3)
genre = ["action", "romance", "comedy", "thriller"]

movie_df = pd.concat([df1,df2, df3])
print(movie_df)
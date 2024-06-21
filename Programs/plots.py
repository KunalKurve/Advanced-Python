# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 18:15:05 2024

@author: Administrator
"""

print("Hello World!");

#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



import seaborn as sns
# Load the data

tips = sns.load_dataset("tips")
#x=tips["total_bill"]
# Create violinplot

sns.violinplot(x = "total_bill", data=tips)
# Show the plot
plt.show()

sns.countplot(x="sex",hue="smoker",data=tips)

sns.boxplot(x="day",y="total_bill",data=tips, hue="day")

sns.distplot(tips["total_bill"],kde=True,bins=5,color="darkgreen")
#kernel densiy estimate

sns.set(style="darkgrid")
sns.histplot(x="total_bill",data=tips,bins=5)

sns.countplot(x="smoker",data=tips,hue="sex")


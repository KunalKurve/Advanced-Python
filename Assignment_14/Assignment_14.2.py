# Store year wise sales of 2 dealers for tv, fridge, mobiles, washing machines, AC and dishwashers for years (2001 to 2010)
# (0000) DEALER tv fridge mobiles washing machines AC dishwashers
# (2001) 0 10000 2000 30000 4000 2000 3000
# (2002) 1 10000 2000 30000 4000 2000 3000

# Answer the following

# b. Find in each year total how many products are sold by dealer1 and how many products are sold by dealer 2.
# c. Display average sales of a 2005 year for each dealer.
# d. Display max sales of a 2005 year for each dealer
# e. Display sales of TV and fridge for each dealer.
# f. Draw 2 bar chart one for each dealer, for each year total number of items sold in the year
# g. Draw a pie chart one for each dealer, for each year total number of items sold in the year

import numpy as np
import pandas as pd

data_frame1 = {
    'years':[2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010],
    'id':
    }

sales1 = [ 10000, 2000, 30000, 4000, 2000, 3000]
sales = pd.concat()

# a. Find total yearwise sales of tv,fridge,mobile,..... product for both dealer.


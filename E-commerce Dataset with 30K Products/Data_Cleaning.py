# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 11:13:13 2022

@author: mhela
Link to database https://www.kaggle.com/datasets/mukuldeshantri/ecommerce-fashion-dataset
"""

# Import libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy import stats
import statsmodels.api as sm
import warnings
from itertools import product
from datetime import datetime
warnings.filterwarnings('ignore')
plt.style.use('seaborn-poster')

df = pd.read_csv('C:/Users/mhela/Documents/kaggle/Data-Science-Projects/E-commerce Dataset with 30K Products/FashionDataset.csv', index_col=False)
df = df.drop(['Unnamed: 0','Index'],axis=1)

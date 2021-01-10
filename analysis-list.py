# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 13:26:50 2021

@author: sgnodde
"""
#%% Load packages
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt

#%% Determine path

paths = [rf"C:\Users\sgnodde\Documents\Spotify\sjoerd_{i}.csv" for i in range(1,4)]



#%% Load first data

for i in range(3):
    data = pd.read_csv(paths[i])
    
    
    # Hists
    plt.figure()
    data['Album Release Date'] = pd.to_datetime(data['Album Release Date'])
    
    data['Album Release Date'].hist(figsize=(9,7),bins = 30)
    plt.title(f"Release date album Sjoerd {i+1}")
    #pd.date_range(start="1990",end="2021", freq= 'y')
    
    plt.figure()
    data['Added At'] = pd.to_datetime(data['Added At'])
    data['Added At'].hist(figsize=(9,7),bins = 20)
    plt.title(f"Added at Sjoerd {i+1}")



#%% Together

data = pd.read_csv(paths[0])
data = data.append(pd.read_csv(paths[1]))
data = data.append(pd.read_csv(paths[2]))
data['Album Release Date'] = pd.to_datetime(data['Album Release Date'])
    
data['Album Release Date'].hist(figsize=(9,7),bins = 30)
plt.title(f"Release date album all lists")


#%% Ouwe meuk

print(data[data['Album Release Date'] < '1990'][['Track Name','Artist Name', 'Album Release Date']])



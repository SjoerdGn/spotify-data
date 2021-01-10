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

#%% Nieuwste nummers


print(data[data['Album Release Date'] > '2020-08'][['Track Name','Artist Name', 'Album Release Date']])


#%% Bands het vaak erin

num_per_band = data.groupby('Artist Name')['Track URI'].nunique()
num_per_band_edited = num_per_band.copy()
for total_artist in num_per_band.index:
    artists = total_artist.split(", ")
    if len(artists) > 1:
        for artist in artists:
            try:
                num_per_band_edited[artist] += 1
            except:
                num_per_band_edited[artist] = 1
                
        num_per_band_edited = num_per_band_edited.drop(total_artist) 
            

#%%

sorted_num_per_band = num_per_band_edited.sort_values()[num_per_band_edited > 4]
sorted_num_per_band.plot.bar(figsize = (12,8))
plt.ylabel("Aantal nummers")
plt.xlabel("")
plt.title("Aantal nummers per artiest dat in Sjoerd 1 t/m 3 staat")


#%% Album het vaak erin

num_per_band = data.groupby('Album Name')['Track URI'].nunique()
num_per_band_edited = num_per_band.copy()
for total_artist in num_per_band.index:
    artists = total_artist.split(", ")
    if len(artists) > 1:
        for artist in artists:
            try:
                num_per_band_edited[artist] += 1
            except:
                num_per_band_edited[artist] = 1
                
        num_per_band_edited = num_per_band_edited.drop(total_artist) 
            

#%%

sorted_num_per_band = num_per_band_edited.sort_values()[num_per_band_edited > 4]
sorted_num_per_band.plot.bar(figsize = (12,8))
plt.ylabel("Aantal nummers")
plt.xlabel("")
plt.title("Aantal nummers per album dat in Sjoerd 1 t/m 3 staat")

#%% Hist duration

(data['Track Duration (ms)']/60000).hist(bins = 30)



#%% Did lengths change?

data_year = data.groupby(data['Album Release Date'].dt.year).mean()

(data_year['Track Duration (ms)']/60000).plot()
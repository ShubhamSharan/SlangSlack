#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
get_lyrics.csv
Created on Sun Feb 10 03:16:50 2019

@author: johnkim
"""
import pandas as pd

pd.set_option('display.max_colwidth', -1)

def get_lyrics(song_title):
    song_title = song_title.lower()
    file = pd.read_csv("songdata.csv") 
    file = file[file["song"].str.lower() == song_title]["text"].values[0]
<<<<<<< HEAD:server/get_lyrics.py
    return(file)

#song_1 = get_lyrics("Billie Jean")
#print(song_1)
file = pd.read_csv("songdata.csv") 

print(file)
=======
    return(file) 
>>>>>>> 2e980a3e23ba59d71dd7345ea407406ad31f9615:get_lyrics.py
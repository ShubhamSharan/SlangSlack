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
    return(file)
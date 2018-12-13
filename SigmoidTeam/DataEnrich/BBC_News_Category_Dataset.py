#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 16:01:41 2018

@author: mk194903
"""

import os
import pandas as pd

dataset_folder = "../dataset/bbc-news"
folders_categories = ["business","sport","entertainment","tech","politics"]

os.chdir(dataset_folder)

x = []
y = []

for i in folders_categories:
    files = os.listdir(i)
    for text_file in files:
        file_path = i + "/" +text_file
        print("reading file:", file_path)
        with open(file_path) as f:
            data = f.readlines()
            #data = data[1:]
        data = ' '.join(data)
        data = data.encode('utf-8').strip()
        x.append(data)
        y.append(i)
   
data = {'news': x, 'category': y}       
df = pd.DataFrame(data)
print('writing to csv ...')
df.to_csv('bbc-news-dataset.csv')
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  8 23:53:49 2018

@author: mk194903
"""
import json
import csv
import os
from pprint import pprint

def f(self):
        return 'hello world'

directory_in_str = "/Users/mk194903/Desktop/Projects/ML/ML_Team_Project/dataprep/csv/624_webhose-2016-11_20170904081158";
directory = os.fsencode(directory_in_str)

count = 0

with open('/Users/mk194903/Desktop/Projects/ML/ML_Team_Project/dataprep/csv/NewsRealData2.tsv', 'w+') as news_tsv:
    news_tsv.write('uuid' + "\t" + 'ord_in_thread' + "\t" + 'author' + "\t" + 'published' + "\t" + 'title' + "\t" + 'text' + "\t" + 'language' + "\t" + 'crawled' + "\t" + 'site_url' + "\t" + 'country' + "\t" + 'domain_rank' + "\t" + 'thread_title' + "\t" + 'spam_score' + "\t" + 'main_img_url' + "\t" + 'replies_count' + "\t" + 'participants_count' + "\t" + 'likes' + "\t" + 'comments' + "\t" + 'shares' + "\t" + 'type' + "\n")
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if (filename.endswith(".json") and count < 2000): # 2000 rows only
            filepath = directory_in_str +'/'+ filename;
            
            with open(filepath) as data_file:
                data_item = json.load(data_file)
                #pprint(data_item)
    
                uuid = (data_item['uuid'])
                ord_in_thread = str(data_item['ord_in_thread'])
                author = (data_item['author'])
                author = author.replace('\t', ' ').replace('\n',' ')
                
                published = (data_item['published'])
                title = (data_item['title'])
                title = title.replace('\t', ' ').replace('\n',' ')
                
                text = (data_item['text'].replace('\t', ' ').replace('\n',' '))
                language = (data_item['language'])
                crawled = (data_item['crawled'])
                site_url = (data_item['thread']['site_full'])
                country = (data_item['thread']['country'])
                domain_rank = str(data_item['thread']['domain_rank'])
                thread_title = (data_item['thread']['title'])#thread_title
                spam_score = str(data_item['thread']['spam_score'])
                main_img_url = (data_item['thread']['main_image'])#main_img_url
                replies_count = str(data_item['thread']['replies_count'])
                participants_count = str(data_item['thread']['participants_count'])
                likes = str(data_item['thread']['social']['facebook']['likes'])
                comments = str(data_item['thread']['social']['facebook']['comments'])
                shares = str(data_item['thread']['social']['facebook']['shares'])
                type1 = (data_item['thread']['site_type'])#type
                news_tsv.write(uuid + "\t" + ord_in_thread + "\t" + author + "\t" + published + "\t" + title + "\t" + text + "\t" + language + "\t" + crawled + "\t" + site_url + "\t" + country + "\t" + domain_rank + "\t" + thread_title + "\t" + spam_score + "\t" + main_img_url + "\t" + replies_count + "\t" + participants_count + "\t" + likes + "\t" + comments + "\t" + shares + "\t" + type1 + "\n")
                count = count +1
                print('files progress - '+str(count))
                #news_tsv.write(l[1] + "\t" + l[2] + "\t" + l[3] + "\t" + l[4] + "\t" + l[5] + "\n")
                
                
                # print(os.path.join(directory, filename))
            #outfile.close()
            continue
        else:
            continue
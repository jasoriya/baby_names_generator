#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 15:48:58 2018

@author: shreyansj
"""

from bs4 import BeautifulSoup
import mechanicalsoup
import pandas as pd
import numpy as np
from tqdm import tqdm

"""
Source: https://hindunames.net/popular-indian-baby-names
"""

def popular_hindu_names(src_url, num_page):
    
    names_df = pd.DataFrame(columns = ['Name', 'Gender', 'Meaning'])
    page = browser.get_current_page()
    table_body = page.select("tr > td")
    for i in np.linspace(0,len(table_body),num = len(table_body)/4, endpoint=False).astype('int64'):
        names_df = names_df.append({'Name': table_body[i].get_text(), 'Gender': table_body[i+1].get_text(), 'Meaning':table_body[i+2].get_text()}, ignore_index = True)
    browser.follow_link("https://hindunames.net/popular-indian-baby-names/" + str(num_page))
    
    return names_df

names_df2 = pd.DataFrame(columns = ['Name', 'Gender', 'Meaning'])
browser = mechanicalsoup.StatefulBrowser(
        soup_config={'features': 'lxml'},
        raise_on_404=True,
        user_agent='MyBot/0.1: mysite.example.com/bot_info')
src_url = "https://hindunames.net/popular-indian-baby-names"
browser.open(src_url)

for num_page in tqdm(list(range(151))[2:]):
    names_df2 = names_df2.append(popular_hindu_names(src_url, num_page))
    
names_df2['Name'].to_csv('baby_names.txt', sep='\n', header = None, index = False)

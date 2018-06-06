#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 15:48:58 2018

@author: shreyansj
"""

from bs4 import BeautifulSoup
import mechanicalsoup

"""
Source: https://hindunames.net/popular-indian-baby-names
"""
def popular_hindu_names(src_url):
    page = browser.get_current_page()
    table_body = page.select("tr > td")
    for i in range(len(table_body)):
            name_list.append(table_body[i].get_text())
    browser.follow_link("https://hindunames.net/popular-indian-baby-names/" + str(num_page))
    
    return name_list


browser = mechanicalsoup.StatefulBrowser(
        soup_config={'features': 'lxml'},
        raise_on_404=True,
        user_agent='MyBot/0.1: mysite.example.com/bot_info')
src_url = "https://hindunames.net/popular-indian-baby-names"
browser.open(src_url)
name_list = []
for num_page in list(range(151))[2:]:
    name_list.append(popular_hindu_names(src_url))

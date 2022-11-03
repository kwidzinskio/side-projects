# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 21:41:55 2021
@author: kwidz
"""

from bs4 import BeautifulSoup
import re
import requests
import csv
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import time

i = 0

file = open('allclubs2021.csv')
csvreader = csv.reader(file)

PATH = 'C:\Program Files\chromedriver.exe'
driver = webdriver.Chrome(PATH)


for row in csvreader:
    
    google_search = "https://www.google.com/search?q="+row[0].replace(" ","+")
    driver.get(google_search)
    
    if i == 0:
        time.sleep(2)
        accept_button = driver.find_element_by_xpath("//button[@id='L2AGLb']")
        accept_button.click()
        time.sleep(2)
    
    for j in range(1,7):
        try:
            
            time.sleep(0.5)
            
            club_link = driver.find_element_by_xpath('(//div/a/h3)[{}]'.format(j))
            club_link.click()
            
            time.sleep(1.5)
            strUrl = driver.current_url
        
            if strUrl.endswith('.pdf'):
                pass
            
            if strUrl.endswith('.html'):
                pass
            
            if strUrl.startswith('https://www.dnb.com/'):
                pass
            
            else:
                try:
                    page = requests.get(strUrl)
                    time.sleep(0.5)
                    soup = str(BeautifulSoup(page.content, 'html.parser'))
                    time.sleep(0.5)
                    all_matches = re.findall(r'[\w\.-]+@[\w\.-]+', soup)
                    #print(all_matches)
                    #print(type(all_matches))
                    #print(all_matches[2])
                    
                    if all_matches:
                        print(*all_matches, sep='\n')
                        time.sleep(0.5)

                        for i in range(len(all_matches)):
                            #print(all_matches[i])
                            f = open("output2021.txt", "a")
                            f.write(all_matches[i])
                            f.write("\n")
                            f.close()
                
                except:
                    pass
                
            time.sleep(1)
            
        except:
            pass
        
        driver.get(google_search)
        time.sleep(1.5)
    
    i+=1











'''
file = open('allclubs2022.csv')
csvreader = csv.reader(file)


for row in csvreader:
    google_search = "https://www.google.com/search?q="+row[0].replace(" ","+")
    #print(google_search)
    page = requests.get(google_search)
    soup = str(BeautifulSoup(page.content, 'html.parser'))
    print(soup)
    print(soup.find('cite').text)

    
    match = re.search(r'[\w\.-]+@[\w\.-]+', soup)
    try:
        print(match.group(0))
        f = open("demofile2.txt", "a")
        f.write(match.group(0))
        f.write(' ')
        f.close()
    except:
        print('###')
'''







    

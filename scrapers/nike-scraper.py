# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 21:41:55 2021

@author: kwidz
"""

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import re


PATH = 'C:\Program Files\chromedriver.exe'
us = [i/2 for i in range(7, 45)]
eu = [35.5, 36, 36.5, 37.5, 38, 38.5, 39, 40, 40.5, 41, 42, 42.5, 43, 44, 44.5, 45, 45.5, 46, 47, 47.5, 48, 48.5, 49, 49.5, 50, 50.5, 51, 51.5, 52, 52.5, 53, 53.5, 54, 54.5, 55, 55.5, 56, 56.5]


def nike(model):
    
    ############# ACCEPT COOKIES #############
    if model == first_pair:
        cookies = True
        accept_button = driver.find_element_by_xpath("//button[@data-var='acceptBtn1']")
        accept_button.click()
    else:
        cookies = False
    
    ############# FIND NEW PAIR #############
    models_to_check = driver.find_elements_by_xpath('//div[@class="product-card__body"]')
    models_to_check[model].click()
    time.sleep(2)
    
    ############# CANCELS IF ON SNEAKERS APP #############
    if "Nike Sneakers Web" in driver.page_source:
        print('-------',model + 1,': nie znaleziono -------') 
        pass
    
    ############# STORING DATA OF A PAIR #############
    else:
        cor_sizes = []
        available_sizes = []
        colorways = driver.page_source.count('colorway-id="Colorway-')
        
        for number in range(colorways):
            if number != 0:
                next_model = str(number+1)
                next_colorway = driver.find_element_by_xpath(f"//div[@data-colorway-id='Colorway-{next_model}']")
                next_colorway.click()
                time.sleep(3)
                
            buy_price = driver.find_element_by_xpath("//meta[@property='og:price:amount']").get_attribute('content')
            # code = driver.find_element_by_xpath("//meta[@property='og:url']").get_attribute('content')[-10:]
            code = driver.find_element_by_xpath("//div[@id='chatModule']").get_attribute('data-product-id')
            in_store = re.findall('"radio"(.+?)"visually-hidden"', driver.page_source)
            size = re.findall('">EU(.+?)</label>', driver.page_source)
        
            for j in range(0, len(in_store)):
                if "disabled" not in in_store[j]: 
                    available_sizes.append(size[j])
                    
            for k in range(len(eu)):
                if str(" "+str(eu[k])) in available_sizes:
                    cor_sizes.append(us[k])
                    
            time.sleep(3)
            
            ############# CALLING STOCKX FUNCTION #############
            sell_prices, sell_sizes = stockx(code, cookies)
            cookies = False
            
            ############# PRINTING OUTPUT #############    
            print('-------',model+1,':',code,' znaleziono -------')
            for l in range(len(sell_prices)):
                if 3.8*0.88*(sell_prices.get(sell_sizes[l], 0)-11) + 10 > (float(buy_price)):
                    print(f'!!! {sell_sizes[j]} !!!')
                if 3.8*0.88*(sell_prices.get(sell_sizes[l], 0)-11) - 25 > (float(buy_price)):
                    print(f'!!!!!!!! {sell_sizes[j]} !!!!!!!!')
                if 3.8*0.88*(sell_prices.get(sell_sizes[l], 0)-11) - 40 > (float(buy_price)):
                    print(f'!!!!!!!!!!! {sell_sizes[j]} !!!!!!!!!!!!')
                
            print(f'code: {code}')
            print(f'buy_price: {buy_price}')
            print(f'sell_prices: {sell_prices}')
            print(f'av_sizes: {cor_sizes}')
            print()
            
    
        driver.back()



def stockx(code, cookies):
    
        ############# ENTERING GOOGLE #############
        driver2.get("https://www.google.pl/")
        time.sleep(3)
        
        ############# ACCEPT COOKIES #############
        if cookies:
            accept_button = driver2.find_element_by_xpath("//button[@id='L2AGLb']")
            accept_button.click()
            time.sleep(4)
        
        ############# SEARCHING FOR CODE #############
        search = driver2.find_element_by_name('q')
        search.send_keys('stockx ' + code)
        search.send_keys(Keys.RETURN)
        time.sleep(2)
        
        ############# FINDING SELL LINK #############
        stockx_link = driver2.find_element_by_xpath("//div/a/h3")
        stockx_link.click()
        time.sleep(6)
        
        link = driver2.find_element_by_xpath("//link[@hreflang='en-us']").get_attribute('href')
        link_start = link[:19]
        link_end = link[19:]
        sellings = link_start+'sell/'+link_end
        time.sleep(1)
        
        ############# ENTERING SELL LINK #############
        driver2.get(sellings)
        time.sleep(6)
        
        ############# FINDING PRICES&SIZES #############
        sizes = re.findall('<div class="tile-value">(.+?)</div>', driver2.page_source)
        prices = re.findall('<div class="tile-subvalue">(.+?)</div>', driver2.page_source)
        sell_prices = {}
        
        for i in range(len(prices)):
            prices[i] = str(prices[i][-3:])
            if '$' in prices[i]:
                price = prices[i].replace('$', '') 
            elif 'Ask' in prices[i]:
                price = prices[i].replace("Ask", "0")
            else:
                price = prices[i]
           
            sell_prices[sizes[i]] = float(price)
        time.sleep(2)
        
        ############# RETURNING TO GOOGLE #############
        driver2.get("https://www.google.com/")
        
        return sell_prices, sizes
    
 





if __name__ == '__main__':
    
    ############# STARTING VALUES #############
    first_pair = int(input("no of pair to start:"))
    colorways = 0
    
    ############# STARTING DRIVERS #############
    driver = webdriver.Chrome(PATH)
    driver2 = webdriver.Chrome(PATH)
    driver.get("https://www.nike.com/pl/w/nowosci-mezczyzni-buty-3n82yznik1zy7ok")
    time.sleep(3)
    
    for i in range(first_pair, 111):

        ############# TRYING TO RETRIEVE #############
        # try:
            nike(i)
        # except:
        #     print('-------',i+1,': nie znaleziono -------')    

        
            
        
    
    
    
    
    


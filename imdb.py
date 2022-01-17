from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup
import requests


#getting chrome browser
driver = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver.exe')
driver.get('https://imdb.com')

#dropdown
dropdown = driver.find_element_by_class_name('ipc-icon--arrow-drop-down')
dropdown.click()
time.sleep(1)

#advanced search
element = driver.find_element_by_link_text('Advanced Search')
element.click()

#click on advanced title search
adv_title = driver.find_element_by_link_text('Advanced Title Search')
adv_title.click()

# select feature film
feature_film = driver.find_element_by_id('title_type-1')
feature_film.click()

# select tv movie
tv_movie = driver.find_element_by_id('title_type-2')
tv_movie.click()

#min date for release time
min_date = driver.find_element_by_name('release_date-min')
min_date.click()
min_date.send_keys('1990')

#max date for release time
max_date = driver.find_element_by_name('release_date-max')
max_date.click()
max_date.send_keys('2020')

#rating_min
rating_min = driver.find_element_by_name('user_rating-min')
rating_min.click()
dropdown_2 = Select(rating_min)
dropdown_2.select_by_visible_text('1.0')

#rating_max
rating_max = driver.find_element_by_name('user_rating-max')
rating_max.click()
dropdown_3 = Select(rating_max)
dropdown_3.select_by_visible_text('10')

#oscar nominated
oscar_nominated =driver.find_element_by_id('groups-7')
oscar_nominated.click()

#color select
color = driver.find_element_by_id('colors-1')
color.click()

#language select
language = driver.find_element_by_name('languages')
dropdown_4 = Select(language)
dropdown_4.select_by_visible_text('English')

#results per page
results_count = driver.find_element_by_id('search-count')
dropdown_5 = Select(results_count)
dropdown_5.select_by_index(2)

#submit
submit = driver.find_element_by_xpath('//*[@id="main"]/p[3]/button')
submit.click()

# current
current_url = driver.current_url




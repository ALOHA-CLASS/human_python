import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

url = 'https://pokemonkorea.co.kr/pokedex'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)

count = 16

# 처음 데이터
info_list = driver.find_elements(By.CSS_SELECTOR, '#pokedexlist .bx-txt h3')

html_text = ''
for item in info_list:
    tag = item.get_attribute('outerHTML')
    html_text += tag
    
soup = BeautifulSoup(html_text, 'html.parser')
print( type( soup ))

no_list_tag = soup.select('p')
no_list = []
for item in no_list_tag:
    no_list.append(item.text)


name_list = []

for item in soup:
    name_list.append( item.contents[1] )
    
    
###
for i in range(1, 11):
    script = '''
                document.body.scrollIntoView(false);
            '''
    driver.execute_script(script)
    
    time.sleep(2)
    info_list = driver.find_elements(By.CSS_SELECTOR, '#pokedexlist .bx-txt h3')
    info_list = info_list[-count:]
    
    
    html_text = ''
    for item in info_list:
        tag = item.get_attribute('outerHTML')
        html_text += tag
        
    soup = BeautifulSoup(html_text, 'html.parser')
    
    no_list_tag = soup.select('p')
    for item in no_list_tag:
        no_list.append(item.text)
    
    for item in soup:
        name_list.append( item.contents[1] )
    

print(no_list)
print(name_list)

time.sleep(10)






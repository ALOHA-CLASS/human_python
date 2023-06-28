import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


no_list = []
name_list = []
img_list = []



def addData( soup ):
    no_list_tag = soup.select('.bx-txt > h3 > p:nth-of-type(1)')
    for item in no_list_tag:
        no_list.append(item.text)
    
    # 포켓몬 이름
    name_list_tag = soup.select('h3')

    for item in name_list_tag:
        name_list.append( item.contents[1] )
        
    # 이미지 URL
    img_list_tag = soup.select('.img img')

    for item in img_list_tag:
        img_list.append( item['src'] )
    


url = 'https://pokemonkorea.co.kr/pokedex'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)

count = 16

prev = 0
now = 0
while True:
    info_list = driver.find_elements(By.CSS_SELECTOR, '#pokedexlist li')
    now = len(info_list)
    if now == prev:
        break
    prev = now
    info_list = info_list[-count:]
    html_text = ''
    for item in info_list:
        tag = item.get_attribute('outerHTML')
        html_text += tag
        
    soup = BeautifulSoup(html_text, 'html.parser')
    addData(soup)
    time.sleep(2)

    # 스크롤 맨 아래로 이동
    script = '''
                document.body.scrollIntoView(false);
                '''
    driver.execute_script(script)
    time.sleep(2)


print(no_list)
print(name_list)
print(img_list)

time.sleep(10)

    
    
        
    
    
    
    
    
    
        
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
info_list = driver.find_elements(By.CSS_SELECTOR, '#pokedexlist li')

html_text = ''
for item in info_list:
    tag = item.get_attribute('outerHTML')
    html_text += tag
    
soup = BeautifulSoup(html_text, 'html.parser')
# print( type( soup ))

# 포켓몬 번호
no_list_tag = soup.select('.bx-txt > h3 > p:nth-of-type(1)')
no_list = []
for item in no_list_tag:
    no_list.append(item.text)

# 포켓몬 이름
name_list = []
name_list_tag = soup.select('h3')

for item in name_list_tag:
    name_list.append( item.contents[1] )
    
# 이미지 URL
img_list = []
img_list_tag = soup.select('.img img')

for item in img_list_tag:
    img_list.append( item['src'] )
    
###
prev = 0
now = 0
for i in range(1, 2):
# while True:
    # 스크롤 맨 아래로 이동
    script = '''
                document.body.scrollIntoView(false);
             '''
    driver.execute_script(script)
    
    
    time.sleep(2)
    info_list = driver.find_elements(By.CSS_SELECTOR, '#pokedexlist li')
    
    
    # 이전 리스트 요소 개수와 현재 리스트 요소개수가 같으면 
    # 더 이상 데이터가 없으므로 종료
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
    

print(no_list)
print(name_list)
print(img_list)

time.sleep(10)



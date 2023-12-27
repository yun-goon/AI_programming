'''
#######안될때 #########

나무위키 xpath 값을 최신으로 받아와야함
###############################
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
import wordcloud
import matplotlib.pyplot as plt

import time


browser = webdriver.Chrome()
url = "https://namu.wiki/w/KBO%20%EB%A6%AC%EA%B7%B8"
browser.get(url)

time.sleep(2)

#페이지 전체
txt = browser.find_elements(By.XPATH,'//*[@id="jWZtJ8Cjb"]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div[5]/div/div[6]/div/div/div/div/div/div/div/div/div[14]')
#일부 - 1번 문단 만 (개요)
# txt = browser.find_elements(By.XPATH,"//*[@id="jWZtJ8Cjb"]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div[5]/div/div[6]/div/div/div/div/div/div/div/div/div[14]/div/div/div/div/div/div/div[1]/div/div[6]/div")
# txt는 list형식

s_words = wordcloud.STOPWORDS.union({'있다','없다'})
image = wordcloud.WordCloud(font_path='C:/Windows/Fonts/MALGUNSL.TTF' ,width = 1000, height = 700, stopwords = s_words).generate(txt[0].text)

plt.figure(figsize = (40, 30))
plt.imshow(image)
plt.show()

'''
참고할만한 사이트
오류 해결
https://hyunsooworld.tistory.com/entry/%EC%85%80%EB%A0%88%EB%8B%88%EC%9B%80-%EC%98%A4%EB%A5%98-AttributeError-WebDriver-object-has-no-attribute-findelementbycssselector-%EC%98%A4%EB%A5%98%ED%95%B4%EA%B2%B0
예제
https://sw-ko.tistory.com/37

#######안될때 #########

나무위키 xpath 값을 최신으로 받아와야함
###############################

'''

import wordcloud
from selenium import webdriver
import matplotlib.pyplot as plt
import time
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
url = "https://namu.wiki/w/KBO%20%EB%A6%AC%EA%B7%B8"
browser.get(url)

time.sleep(2)


#페이지 전체
txt = browser.find_elements(By.XPATH,'//*[@id="jWZtJ8Cjb"]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div[5]/div/div[6]/div/div/div/div/div/div/div/div/div[14]')
#일부 - 1번 문단 만 (개요)
# txt = browser.find_elements(By.XPATH,"//*[@id="jWZtJ8Cjb"]/div[2]/div/div/div/div/div/div/div/div/div/div[1]/div[5]/div/div[6]/div/div/div/div/div/div/div/div/div[14]/div/div/div/div/div/div/div[1]/div/div[6]/div")

# txt는 list형식


for text in txt:
    print(text.text) #str값

s_words = wordcloud.STOPWORDS.union({'있다','없다'})
image = wordcloud.WordCloud(font_path='C:/Windows/Fonts/MALGUNSL.TTF' ,width = 1000, height = 700, stopwords = s_words).generate(txt[0].text)
plt.figure(figsize = (40, 30))
plt.imshow(image)
plt.show()

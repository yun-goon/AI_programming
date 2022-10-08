from selenium import webdriver
import time
from selenium.webdriver.common.by import By

chromedriver = "C:\chromeweb\chromedriver.exe"
driver = webdriver.Chrome()

# name = "KBO%20리그"
name = "효연"
driver.get('https://namu.wiki/w/'+name)

print("+" * 100)
print(driver.title)
print(driver.current_url)
print("킹무위키 크롤링")
print("-" * 100)



time.sleep(2)

# 킹무위키 페이지 진입해서 프로필 테이블 추출
allProfileElement = driver.find_elements(By.CSS_SELECTOR,"div.wiki-table-wrap.table-right")

print(type(allProfileElement))
print(allProfileElement[0])

# 나무위키 페이지 크롤링
# for item in allProfileElement:
#     for itemSub in item.find_elements(By.CSS_SELECTOR,'tr'):
#         for lastItem in itemSub.find_elements(By.CSS_SELECTOR,"td > div"):
#             if(lastItem.find_elements(By.CSS_SELECTOR,"strong")):
#                 print("\n"+lastItem.find_elements(By.CSS_SELECTOR,"strong")[0].text,end=' : ')
#             else :
#                 print(lastItem.text)
driver.quit()

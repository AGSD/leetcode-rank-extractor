from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import xlwt

bs = BeautifulSoup

browser = webdriver.Firefox()
browser.implicitly_wait(10)
wait = WebDriverWait(browser, 10)

page = browser.get("https://leetcode.com/contest/leetcode-weekly-contest-54/ranking") #change to 54
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.ranking-username")))
innerHTML = browser.execute_script("return document.body.innerHTML")
soup = bs(innerHTML,"lxml")

limit = 60#int(soup.find_all('ul')[5].find_all('li')[-2].text.encode("ascii","default"))
limit = limit + 1 #range exludes last item

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet("sheet 1")

index=0
for i in range(1,limit):
    if i==1:
        page = browser.get("https://leetcode.com/contest/leetcode-weekly-contest-54/ranking") #change to 54
    else:
        page = browser.get("https://leetcode.com/contest/leetcode-weekly-contest-54/ranking/"+str(i)+"/") #change to 54

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.ranking-username")))

    innerHTML = browser.execute_script("return document.body.innerHTML")
    soup = bs(innerHTML,"lxml")
    for tr in soup.find_all('tr')[1:]:
        td = tr.find_all('td')
        rank,name,score,time = td[0].text,td[1].text,td[2].text,td[3].text
        print rank,name,score,time
        sheet1.write(index,0,rank)
        sheet1.write(index,1,name)
        sheet1.write(index,2,score)
        sheet1.write(index,3,time)
        index = index+1

book.save("everyone.xls")

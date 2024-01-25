from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
service= Service("./chromedriver")
driver=webdriver.Chrome(service=service)
driver.get("https://www.linkedin.com/mynetwork/")
time.sleep(60)
while True:
    try:
        click=driver.find_element(By.XPATH,'/html/body/div[5]/div[3]/div/div/div/div/div[2]/div/div/main/section[2]/div/div[1]/div[1]/div[2]/ul/li[1]/div/section/div[3]/footer/button').click()
        time.sleep(2)

        delete=driver.find_element(By.XPATH,'/html/body/div[5]/div[3]/div/div/div/div/div[2]/div/div/main/section[2]/div/div[1]/div[1]/div[2]/ul/li[1]/div/section/button').click()
        time.sleep(3)
    except:
        driver.refresh()
        time.sleep(5)
        print("hata")
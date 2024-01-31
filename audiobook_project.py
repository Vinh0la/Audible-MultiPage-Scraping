import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd

url = "https://www.audible.com.br/search?node=41939682011&ref_pageloadid=O2wAvvyEoz3fDgU6&ref=a_cat_Compu_c0&pf_rd_p=dc1344c1-8d8e-4f1d-a788-ceb52686bd73&pf_rd_r=KB4NDK2FWR4G4CP0357Z&pageLoadId=NZKf8UFA0nMOR8Y3&creativeId=55f26bd3-b057-4923-8e9f-4199dafc0395"

path = r"C:\Users\gusta\Downloads\chromedriver.exe"

driver = webdriver.Chrome(service=Service(path))

driver.get(url)

pagination = driver.find_element(By.XPATH,'//ul[contains(@class,"pagingElements")]')
pages = pagination.find_elements(By.TAG_NAME,'li')
current_page = 1
last_page = int(pages[-2].text)

titles = []
authors = []
runtimes = []

while current_page <= last_page:

    time.sleep(3)
    container = driver.find_element(By.XPATH, '//*[@id="center-3"]/div/div/div/span[2]/ul')
    products = container.find_elements(By.XPATH, './li')

    for product in products:
        try:
            titles.append(product.find_element(By.TAG_NAME,'h3').text)
            authors.append(product.find_element(By.XPATH,'.//li[contains(@class,"authorLabel")]//a').text)
            runtimes.append(product.find_element(By.XPATH,'.//li[contains(@class,"runtimeLabel")]').text)
        except:
            pass

    current_page += 1
    nex_button = driver.find_element(By.XPATH, '//span[contains(@class,"nextButton")]')
    nex_button.click()


df = pd.DataFrame.from_dict({'Title':titles,'Author':authors,'Run Time':runtimes})
df.to_csv('Books.csv',index=False)

time.sleep(15)
driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

# Yapılandırma ayarları
PATH_CHROME_DRIVER = sys.prefix + "\\Library\\bin\\chromedriver.exe"
URL = "https://www.gettyimages.com/photos/traffic-cone?mediatype=photography&phrase=traffic%20cone&sort=mostpopular"
WAIT_UNTIL = "assets"

# Driver oluşturma ve bağlanma
driver = webdriver.Chrome(PATH_CHROME_DRIVER)
driver.get(URL)

try:
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.ID, WAIT_UNTIL)))
    driver.execute_script(open("./javascripts/gettyImages-min.js").read())  # hata min.js haline getir.
    urls = driver.execute_script("return getImageUrls(67)")

    print(urls)

finally:
    driver.close()

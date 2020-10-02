from selenium.webdriver.chrome.options import Options
from selenium import webdriver
chrome_options = Options()

chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('blink-settings=imagesEnabled=false')
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(chrome_options=chrome_options)
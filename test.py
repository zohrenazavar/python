from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('ignore-certificate-errors')
driver = webdriver.Chrome(options=options)

epm_section = (By.XPATH, "//span[contains(text(), 'EPM tool')]")


def open_section(locator):
    driver.get('https://spgtools.specific-group.com/')
    element = driver.find_element(*locator)
    element.click()


open_section(epm_section)
# driver.quit()

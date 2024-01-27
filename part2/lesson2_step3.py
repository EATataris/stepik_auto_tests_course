from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--remote-debugging-port=9222")


def sum(num1, num2):
    return num1 + num2


try:
    link = "http://suninjuly.github.io/selects2.html"

    browser = webdriver.Chrome(options=chrome_options)
    browser.get(link)

    num1 = int(browser.find_element(By.ID, 'num1').text)
    num2 = int(browser.find_element(By.ID, 'num2').text)
    sum_of_nums = sum(num1, num2)

    select = Select(browser.find_element(By.TAG_NAME, 'select'))
    select.select_by_value(str(sum_of_nums))

    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    submit_button.click()
finally:
    time.sleep(10)
    browser.quit()
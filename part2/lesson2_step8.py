from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math, os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--remote-debugging-port=9222")

try:
    browser = webdriver.Chrome(options=chrome_options)
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    input1.send_keys('Ivan')
    input2 = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    input3.send_keys("ivan@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    file_element = browser.find_element(By.ID, 'file')
    file_element.send_keys(file_path)

    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()
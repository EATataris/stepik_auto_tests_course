from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--remote-debugging-port=9222")


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome(options=chrome_options)
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    magic_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    magic_button.click()

    alert = browser.switch_to.alert
    alert.accept()

    x = int(browser.find_element(By.ID, 'input_value').text)
    y = calc(x)

    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(y)

    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-primary')
    submit_button.click()

finally:
    time.sleep(5)
    browser.quit()
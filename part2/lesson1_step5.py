from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--remote-debugging-port=9222")


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome(options=chrome_options)
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = int(x_element.text)
    y = calc(x)

    input_answer = browser.find_element(By.CSS_SELECTOR, '#answer')
    input_answer.send_keys(y)

    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()

    radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton.click()

    submit_button = browser.find_element(By.CSS_SELECTOR, '.btn.btn-default')
    submit_button.click()
finally:
    time.sleep(10)
    browser.quit()


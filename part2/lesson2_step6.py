from selenium import webdriver
from selenium.webdriver.common.by import By
import time, math

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--remote-debugging-port=9222")


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome(options=chrome_options)
    link = "https://SunInJuly.github.io/execute_script.html"
    browser.get(link)

    browser.execute_script("window.scrollBy(0, 100);")

    x = int(browser.find_element(By.ID, 'input_value').text)
    y = calc(x)

    input_answer = browser.find_element(By.ID, 'answer')
    input_answer.send_keys(y)

    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()

    radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton.click()

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
finally:
    time.sleep(5)
    browser.quit()

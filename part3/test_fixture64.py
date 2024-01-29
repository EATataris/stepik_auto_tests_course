import pytest, time, math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestRegistrationPages():
    mess = ''
    links_addresses = [
        'https://stepik.org/lesson/236895/step/1',
        'https://stepik.org/lesson/236896/step/1',
        'https://stepik.org/lesson/236897/step/1',
        'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1',
        'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1',
        'https://stepik.org/lesson/236905/step/1',
    ]

    @pytest.mark.parametrize('links', links_addresses)
    def test_guest_should_see_login_link(self, browser, links):

        browser.get(links)
        browser.find_element(By.ID, "ember33").click()
        browser.find_element(By.ID, "id_login_email").send_keys('')
        browser.find_element(By.ID, "id_login_password").send_keys('')
        browser.find_element(By.CSS_SELECTOR, ".sign-form__btn.button_with-loader").click()
        browser.implicitly_wait(10)
        time.sleep(5)

        browser.find_element(By.TAG_NAME, "textarea").send_keys(str(math.log(int(time.time()))))
        time.sleep(3)
        browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()

        message = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))).text

        assert 'Correct!' in message, f'expected Correct!, got {message}'

        if __name__ == "__main__":
            pytest.main()
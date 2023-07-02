from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time


class get_csv_file_from_danske_bank:
    def get_csv_file_from_danske_bank(username, cpr):
        url = 'https://danskebank.dk/privat'

        # Open Firefox and navigate to the website
        driver = webdriver.Firefox()  # options=options)
        driver.get(url)

        wait = WebDriverWait(driver, 20)
        button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="button-accept-necessary"]')))
        button.click()

        # Wait up to 10 seconds for the element to become clickable
        wait = WebDriverWait(driver, 10)
        button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/header/div[2]/div[2]/div/div/div[1]/div[3]/div/button')))

        # Click the button
        button.click()

        wait = WebDriverWait(driver, 2)
        button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="pbnetbankmid"]')))
        button.click()

        # skriv brugernavn
        wait = WebDriverWait(driver, 40)  # måske højere
        i = 0
        elements = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, '//input[contains(@id, "username")]')))
        for element in elements:
            # check if the element is reachable by keyboard
            if element.is_enabled() and element.is_displayed():
                # fill in the text box
                element.send_keys(username)
                x = i
            else:
                print(f"Element {i} is not reachable by keyboard")
            i += 1

        print(x)

        # tryk forsæt
        wait = WebDriverWait(driver, 100)
        button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, f'//*[@id="loginBtn{x}"]')))
        button.click()

        # skriv cpr nummer
        element = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//*[@id="InputWithError-1"]')))
        element.send_keys(cpr)

        # tryk forsæt
        button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div/div/div/div/div/div[1]/div/div/div/button')))
        button.click()

        # tryk på konti
        button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/form/div[4]/div[2]/div/ul/li[3]/a')))
        button.click()

        # tryk på kontobevægelser
        button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/form/div[4]/div[2]/div/ul/li[3]/div/div[1]/ul/li[3]/a')))
        button.click()

        # træk i håndtaget

        # Find the handle element
        handle = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/form/div[4]/div[3]/div/div/div[1]/div[3]/div[2]/div[3]/div/div[2]/div/div[5]/div[2]/a')))

        # Perform the drag action
        action_chains = ActionChains(driver)
        action_chains.click_and_hold(
            handle).move_by_offset(-500, 0).release().perform()
        time.sleep(3)
        action_chains.click_and_hold(
            handle).move_by_offset(-150, 0).release().perform()
        time.sleep(3)

        # time.sleep(4)
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(4)

        # TODO: Scroll in to view rigtigt ovenover!
        # tryk gem som fil
        button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="db-tl-savetofile-button"]')))
        button.click()

        # Find the iframe element
        iframe = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//iframe[@id="indhold"]')))

        # Switch to the iframe
        driver.switch_to.frame(iframe)

        # TRYK PÅ CSV.
        button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[2]/form/table[2]/tbody/tr[2]/td/div/span/table[1]/tbody/tr/td/div/table[2]/tbody/tr[2]/td[1]/input')))
        button.click()

        # Find the button element
        button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="butGemID"]')))

        # Click the button
        button.click()

        # Switch back to the default content
        driver.switch_to.default_content()

        driver.close()

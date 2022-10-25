from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class VotingMachine:

    def __init__(self):
        chrome_driver_path = "C:/Development/chromedriver.exe"
        ser = Service(chrome_driver_path)
        op = webdriver.ChromeOptions()

        chrome_prefs = {}
        op.experimental_options["prefs"] = chrome_prefs
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        chrome_prefs["profile.managed_default_content_settings"] = {"images": 2}

        self.driver = webdriver.Chrome(service=ser, options=op)

    #ADD YOUR POLL'S URL HERE
    def vote(self):
        self.driver.get("Your strawpoll url here")
        self.driver.execute_script("window.scrollTo(0, 250)")

    # CHANGE THE XPATH TO WHAT YOU WANT TO CLICK ON
        second_button = self.driver.find_element(By.XPATH, '//*[@id="strawpoll_box_1Mnwvp5N5y7"]/div[2]/div[1]/form/div[5]/fieldset/div/div[2]/label')
        second_button.click()
        time.sleep(2)
        vote_button = self.driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div[1]/form/div[8]/div/div[3]/button')
        vote_button.send_keys(Keys.ENTER)
        time.sleep(1)

        self.driver.execute_script("window.open('');")


if __name__ == "__main__":
    participatingCitizen = VotingMachine()

    while 1 == 1:
        participatingCitizen.vote()

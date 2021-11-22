from selenium.webdriver.common.by import By


class Confirmpage:
    def __init__(self,driver):
        self.driver = driver

    Countryname = (By.ID,"country")

    def GetConfirm(self):
        return self.driver.find_element(*Confirmpage.Countryname)

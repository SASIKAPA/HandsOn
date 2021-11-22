from selenium.webdriver.common.by import By


class Checkout:
    def __init__(self,driver):
        self.driver = driver
    cardtitle = (By.XPATH,"//div[@class='card h-100']")
    cardfooter = (By.XPATH,"div/button")
    checkedout = (By.CSS_SELECTOR,"a[class*='btn-primary']")
    SuccessButt = (By.XPATH,"//button[@class='btn btn-success']")

    def GetcardDetails(self):
        return  self.driver.find_elements(*Checkout.cardtitle)

    def Getcardfooter(self):
        return self.driver.find_element(*Checkout.cardfooter)

    def GetCheckedOut(self):
        return self.driver.find_element(*Checkout.checkedout)

    def GetSuccessbutt(self):
        return self.driver.find_element(*Checkout.SuccessButt)

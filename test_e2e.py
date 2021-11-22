
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import time
import pytest
from baseclass import baseclass
from pageObjects.Checkoutpage import Checkout
from pageObjects.Confirmpage import Confirmpage
from pageObjects.Homepage import Homepage

#@pytest.mark.usefixtures('setup') instead of using here, we are importing from baseclass

class test_one(baseclass):
    def test_e2e(self):
        #self.driver.find_element_by_css_selector("a[href*='shop']").click()
        homepage = Homepage(self.driver)  #This is used instead of above line L2
        homepage.shopitems().click()
        #products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        products = Checkout(self.driver).GetcardDetails()  #This is used instead of above line L2


        # //div[@class='card h-100']/div/h4/a
        # product =//div[@class='card h-100']
        for product in products:
            #productName = product.find_element_by_xpath("div/h4/a").text
            productName = product.text
            if productName == "Blackberry":
                #Add item into cart
                #product.find_element_by_xpath("div/button").click()
                Checkout(self.driver).Getcardfooter().click()   #This is used instead of above line L2


        #self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        Checkout(self.driver).GetCheckedOut().click()    #This is used instead of above line L2
        #self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        Checkout(self.driver).GetSuccessbutt().click()    #This is used instead of above line L2

        #self.driver.find_element_by_id("country").send_keys("ind")
        Confirmpage(self.driver).GetConfirm().send_keys("ind")  #This is used instead of above line L2
        #wait = WebDriverWait(self.driver, 7)
        #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.IsVerifyText('India') #This is used instead of above line L3
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        successText = self.driver.find_element_by_class_name("alert-success").text

        assert "Success! Thank you!" in successText

        self.driver.get_screenshot_as_file("screen.png")




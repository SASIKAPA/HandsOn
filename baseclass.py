import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures('setup')

class baseclass():
    #pass # tells that nothing is present inside the class, base class has a knowledge of fixtures
    def IsVerifyText(self,text):
        wait = WebDriverWait(self.driver, 7)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))


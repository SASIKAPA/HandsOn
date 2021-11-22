
import pytest
from selenium import webdriver
@pytest.fixture(scope='class')

def setup(request):
    driver = webdriver.Chrome(executable_path = 'D:\WORKSPACE\SELENIUM\chromedriver.exe')
    driver.get('https://www.rahulshettyacademy.com/angularpractice/')
    driver.maximize_window()
    #return driver
    request.cls.driver = driver     #here we cannot use return along with yield
    yield
    driver.close()

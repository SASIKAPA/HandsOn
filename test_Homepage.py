from baseclass import baseclass


class Homepagetest(baseclass):
    def test_Homepage(self):
        from selenium import webdriver
        from selenium.webdriver.support.select import Select

        driver = webdriver.Chrome(executable_path='D:\WORKSPACE\SELENIUM\chromedriver.exe')
        driver.get('https://www.rahulshettyacademy.com/angularpractice/')
        driver.maximize_window()
        driver.find_element_by_name('name').send_keys('Danie Ricciardo')
        driver.find_element_by_name('email').send_keys('DanielRicciardo@mclaren.com')
        driver.find_element_by_id('exampleCheck1').click()
        driver.find_element_by_css_selector("input[id='exampleInputPassword1']").send_keys('LandoNorrisOfficial')
        driver.find_element_by_xpath('//input[@type="submit"]').click()
        print(driver.find_element_by_class_name('alert').text)
        dropdown = Select(driver.find_element_by_id('exampleFormControlSelect1'))
        dropdown.select_by_visible_text('Male')
        dropdown.select_by_index(1)
        message = driver.find_element_by_class_name('alert').text
        assert "success" in message
from selenium import webdriver
from selenium.webdriver.support.select import Select


class Demoqa():

    def test(self):
        baseUrl = "https://demoqa.com/automation-practice-form"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseUrl)

        firstname_field = driver.find_element_by_id("firstName")
        firstname_field.send_keys("Test1")
        lastname_field = driver.find_element_by_id("lastName")
        lastname_field.send_keys("Test2")
        email_field = driver.find_element_by_id("userEmail")
        email_field.send_keys("test@gmail.com")
        phonenumber_field = driver.find_element_by_id("userNumber")
        phonenumber_field.send_keys("123456789")
        calendar_field = driver.find_element_by_id("dateOfBirthInput")
        calendar_field.click()

        month_dd = driver.find_element_by_xpath("//select[@class = 'react-datepicker__month-select']")
        dd_options =Select(month_dd)

        month_selected = dd_options.select_by_value(1)
        print(month_selected)

        month_selected1 = dd_options.select_by_visible_text("April")
        print(month_selected1)

        month_selected2 = dd_options.select_by_index(1)
        print(month_selected2)




cc =Demoqa()
cc.test()
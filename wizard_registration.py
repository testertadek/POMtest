import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

first_name = 'Tadeusz'
last_name = 'Testowy'
email = 'data2@data.com'
country = 'Poland'
mobile_number = '607789123'
password = 'test1234'

#Scenariusz testowy:
#Rejestracja nowego uytkownika na stronie http://automationpractice.com/index.php
class Wizard_registration(unittest.TestCase):

    #Warunki wstepne:
    def setUp(self):
        #1. Otwarta przegladarka
        self.driver = webdriver.Chrome()
        #2. Otwarta strona http://automationpractice.com/index.php
        self.driver.get("https://wizzair.com/#/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        #przypadki testowe:
        #I Niewybrane miasto
    def testNoCity(self):
        driver = self.driver
        print("test chodzi")
        #self.assertEqual(3,3)
        #1. Klknij "sign in"
        sign_in_xpath = '//*[@id="app"]//*[@class="navigation"]//*[contains(text(), "Sign in")]'
        #sign_in = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, sign_in_xpath)))
        #sign_in = driver.find_element_by_xpath('//*[@id="app"]//*[@class="navigation"]//*[contains(text(), "Sign in")]')
        sign_in_link = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, sign_in_xpath)))
        sign_in_link.click()
        registraion_xpath = '//*[@class="modal__inner"]//button[contains(text(), "Registration")]'
        registration_button = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, registraion_xpath)))
        registration_button.click()

        #3. wpisz imie
        first_name_xpath = '//*[@name="firstName"]'
        first_name_input = driver.find_element_by_xpath(first_name_xpath)
        first_name_input.send_keys(first_name)

        #3a wpisz nazwisko
        last_name_xpath = '//*[@name="lastName"]'
        last_name_input = driver.find_element_by_xpath(last_name_xpath)
        last_name_input.send_keys(last_name)

        #3b kliknij w modal body
        xpath_modal_body = '//*[@class="modal__body"]'
        modal_body = driver.find_element_by_xpath(xpath_modal_body)
        modal_body.click()

        #4 wybierz mail
        xpath_male_button = '//*[contains(text(),  "Male")]'
        male_button = driver.find_element_by_xpath(xpath_male_button)
        male_button.click()

        #wybierz country
        xpath_country  = '//div[@class =  "phone-number__calling-code-selector__empty"]'
        input_country_empty = driver.find_element_by_xpath(xpath_country)
        input_country_empty.click()
        name_country_name = 'phone-number-country-code';
        input_country_name = driver.find_element_by_name(name_country_name)
        input_country_name.send_keys('Poland')

        field_country_name_xpath = "//li[@data-test='PL']"
        field_country_name = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, field_country_name_xpath)))
        field_country_name.click()
        #6.Enter mobile number   678912321
        phone_number_xpath = "//input[@placeholder = 'Mobile Phone number']"
        input_phone_number = driver.find_element_by_xpath(phone_number_xpath)
        input_phone_number.send_keys(mobile_number)
        # 7 ENter email (data@data)
        email_name = 'email'
        input_email_address = driver.find_element_by_name(email_name)
        input_email_address.send_keys(email)

        password_name = 'password'
        input_password = driver.find_element_by_name(password_name)
        input_password.send_keys(password)

        country_name = 'country-select'
        country_field = driver.find_element_by_name(country_name)
        country_field.click()
        country_field.send_keys(country)
        country_field.send_keys(Keys.RETURN)
        sleep(3)
        print('96 linijka')
        button_register_xpath = "//div[@class='cta-container gutter-bottom']"
        button_register = driver.find_element_by_xpath(button_register_xpath)
        print('99 linijka')
        button_register.click()

        sleep(15)
        error_message_privacy_xpath = "//span[@class='rf-input__error__message']//span[contains(text(), 'Privacy Notice')]"
        error_message_privacy = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, error_message_privacy_xpath)))
        error_message_privacy_text = error_message_privacy.get_attribute("innerText")
        assert 'Please accept the Privacy Notice' in error_message_privacy_text




    def tearDown(self):
        self.driver.quit()
        print("Sprzatanie po kazdym tescie")


if __name__ == '__main__':
    unittest.main(verbosity=2)











# Rejestracja na stronie wizzair.com  - przypadek negatywny


#1. Kliknij sign_in

#2. WYbierz link registration
#3. wpisz imie

#4. wpisz male
#5. kliknij country code - wpisze Polska - wybierz poland z listy
#6.Enter mobile number   678912321
# 7 ENter email (data@data)
#8  Enter password - test1234
#9 enter country of citizens - Poland
#10. choose register wihout marked accept private policy

#Expected result:
#check if message Please accept the Privacy Notice appersa

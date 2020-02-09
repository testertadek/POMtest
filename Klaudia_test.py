import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

name = "Anna"
surname = "Nowak"
country = "Polska"
email = "Anna.Nowak@mail.com"
phone = "123456789"
# Scenariusz testowy:
# Rejestracja nowego uzytkownika na stronie https://wizzair.com/pl-pl#/

# Warunki wstepne
class WizzRegistration(unittest.TestCase):
    def setUp(self):
        # 1. Otwarta przegladarka
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        # 2. Otwarta strona https://wizzair.com/pl-pl#/
        self.driver.get("https://wizzair.com/pl-pl#/")
        self.driver.implicitly_wait(15)

    # Przypadki testowe:
    # NIEWAZNE HASLO

    def testRegistration(self):
        driver = self.driver
        # Kroki:
        # 1. Odszukaj i kliknij zaloguj sie
        login_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='app']/div/header/div[1]/div/nav/ul/li[11]/button")))
        login_field.click()

        # 2. Odszukaj i kliknij rejestracja

        reg_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Rejestracja')]")))
        reg_field.click()

        # 3. Wprowadz imie
        name_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='regmodal-scroll-hook-1']/label[1]/div[1]/input")))
        name_field.send_keys(name)

        # 4. Wprowadz nazwisko
        surname_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='regmodal-scroll-hook-1']/label[2]/div[1]/input")))
        surname_field.send_keys(surname)

        # 5. Wybierz plec
        driver.find_element_by_xpath("//*[@id='regmodal-scroll-hook-2']/div[1]/label[1]/span").click()

        # 6. Wybierz kod kraju
        country_input = driver.find_element_by_xpath("//div[@class ='phone-number__calling-code-selector__empty__placeholder']")
        country_input.click()
        country_input = driver.find_element_by_xpath("//*[@name='phone-number-country-code']")
        country_input.send_keys("Polska")
        sleep(10)
        country_input.send_keys(Keys.RETURN)

        # 7. Wprowadz numer telefonu
        phone_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='regmodal-scroll-hook-3']/div[2]/div/div[1]/div/label/input")))
        phone_field.click()
        phone_field.send_keys(phone)
        sleep(10)

        # 8. Wprowadz adres e-mail
        email_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='regmodal-scroll-hook-4']/div[1]/label/input")))
        email_field.click()
        email_field.send_keys(email)
        sleep(3)

        # 9. Wprowadz haslo - nie spelnia wymogow (7-16 znakow, litery i cyfry)
        pass_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//*[@id='regmodal-scroll-hook-5']/div[1]/label/input")))
        pass_field.click()
        pass_field.send_keys("a123")
        sleep(3)

        # 10. Wybierz narodowosc
        nationality_input = driver.find_element_by_xpath("//*[@id='regmodal-scroll-hook-6']/div[1]/label")
        nationality_input.click()
        nationality_input = driver.find_element_by_xpath("//*[@id='regmodal-scroll-hook-6']/div[1]/label/input")
        nationality_input.send_keys("Polska")

        nationality_input.send_keys(Keys.RETURN)

        # 11. Kliknij akceptuje informacje o polityce prywatnosci
        box_field = driver.find_element_by_xpath('//label[@for="registration-privacy-policy-checkbox"][@class="rf-checkbox__label"]')
        box_field.click()


        # 12. Kliknij zarejestruj sie
        register_button = driver.find_element_by_xpath("//*[@class='cta-container gutter-bottom']")
        register_button.click()


        # Oczekiwany rezulat
        # (0. konto nie zostaje zalozone)
        # 1. Wyswietla sie blad - "Wpisz hasło"
        errors = driver.find_elements_by_xpath('//span[@class="rf-input__error__message"]')
        visible_errors=[]
        for e in errors:
            if e.is_displayed():
                visible_errors.append(e)

        assert len(visible_errors) == 1
        tekst_bledu = visible_errors[0].text
        assert tekst_bledu == "Wpisz hasło"


        sleep(5)

    def tearDown(self):
        # Sprzatanie po kazdym tescie
        # Wylacz przegladarke
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)

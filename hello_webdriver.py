import unittest
from selenium import webdriver
from time import sleep


class WsbPlCheck(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://wsb.pl")
        self.driver.maximize_window()

        print("jestem Setup - przygotowanie do testu")

    def testTitle(self):
        #sprawdzam czy tyyu jest dobry
        self.assertIn("Bankowe", self.driver.title)
        print("Title = ", self.driver.title)
        sleep(2)


    def tearDown(self):
        self.driver.quit()


        print("Sprzatanie po kazdym tescie")


if __name__ == '__main__':
    unittest.main(verbosity=1)

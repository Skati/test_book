from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    #new user test
    def setUp(self):
        self.driver=webdriver.Chrome('/home/sergey/chromedriver')

    def tearDown(self):
        self.driver.quit()

    def test_start_and_retrieve(self):
        self.driver.get('http://localhost:8000')
        self.assertIn('To-Do', self.driver.title)
        self.fail('End Test')


if __name__== '__main__':
    unittest.main(warnings='ignore')

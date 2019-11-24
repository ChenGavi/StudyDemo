# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class AmazonSearch(unittest.TestCase):
    base_url = "https://www.amazon.in/"
    search_term = "WD My Passport 4TB"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def test_search_for_a_term(self):
        driver = self.driver
        driver.get(self.base_url)
        SearchTestBox = driver.find_element_by_id("twotabsearchtextbox")
        SearchTestBox.clear()
        SearchTestBox.send_keys(self.search_term)
        SearchTestBox.send_keys(Keys.ENTER)
        self.assertIn(f"Amazon.in: {self.search_term}",driver.title)
        self.assertNotIn("No results found.",driver.page_source)

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()

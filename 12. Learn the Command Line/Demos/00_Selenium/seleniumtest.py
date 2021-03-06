from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
import unittest
import time

def highlight(element):
    """Highlights (blinks) a Selenium Webdriver element"""
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",
                              element, s)
    original_style = element.get_attribute('style')
    apply_style("background: yellow; border: 2px solid red;")
    time.sleep(2)
    apply_style(original_style)

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def tearDown(self):
        self.driver.close()

    def test_001_TestingGeek(self):
        driver = self.driver
        driver.get("http://www.google.com")
        assert "Google" in driver.title
        searchBar = driver.find_element_by_id("lst-ib")
        searchBar.send_keys("testing geek")
        searchBar.send_keys(Keys.RETURN)
        wait = ui.WebDriverWait(driver,10)
        wait.until(lambda driver: driver.find_element_by_xpath("//*[@id='rso']/div/div[1]/div/h3/a"))
        firstLinkInSearch = driver.find_element_by_xpath("//*[@id='rso']/div/div[1]/div/h3/a")
        highlight(firstLinkInSearch)
        assert(firstLinkInSearch.text == "Software Testing Geek")


if __name__ == "__main__":
    unittest.main()
     �   
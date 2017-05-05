import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SeleniumTest():
    def __init__(self):
        """
        Constructor: It will call the main functions
        required for testing
        """
        self.driver = []
        # Set Driver count. This value will indicate number
        # of windows to open for performance testing
        self.driver_count = 1
        # navigate to the application home page
        self.google_test()

    def google_test(self):
        """
        This function will initialize driver and open up google.com
        and look for a given string.
        Once result is returned it will get the count of result list
        Select the first search item and redirect to that page
        :return:
        """
        driver_count = 0
        # This way we can open more then one browser.
        # This can be used for performance testing, or
        # This can be used to test variou situations where we need to open more then one browser
        while driver_count < self.driver_count:
            self.driver.append(webdriver.Firefox())
            self.driver[driver_count].maximize_window()
            # navigate to the google home page
            self.driver[driver_count].get("http://google.com")
            # get the search textbox
            WebDriverWait(self.driver[driver_count], 10).until(lambda s: s.find_element_by_name('q').is_displayed())
            search_field = self.driver[driver_count].find_element_by_name("q")
            search_field.clear()

            # enter search keyword and submit
            search_field.send_keys("Selenium WebDriver Interview questions")
            search_field.send_keys(Keys.RETURN)

            RESULTS_LOCATOR = "//div/h3/a"

            WebDriverWait(self.driver[driver_count], 10).until(
                EC.visibility_of_element_located((By.XPATH, RESULTS_LOCATOR)))

            page1_results = self.driver[driver_count].find_elements(By.XPATH, RESULTS_LOCATOR)

            # get the number of elements found
            print("Found " + str(len(page1_results)) + "searches:")
            # display the text of each list item
            for item in page1_results:
                print(item.text)

            # Redirect to first search result
            page1_results[0].click()

            # Increment the driver count
            driver_count += 1

        self.close_browser()

    def close_browser(self):
        """
        This function will close all the browsers once the test is over
        Sleep time of 10 seconds is given
        :return:
        """
        # close the all browser window
        time.sleep(10)
        driver_count = 0
        while driver_count < self.driver_count:
            self.driver[driver_count].quit()
            driver_count += 1

if __name__ == '__main__':
    SELENIUM_TEST = SeleniumTest()


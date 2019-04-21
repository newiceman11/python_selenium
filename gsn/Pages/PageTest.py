from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import unittest
import time


class responsive:

    def __init__(self, myDriver):
        self.driver = myDriver
        self.Path = (By.CLASS_NAME,'navbar-toggle')

    def mobile_vertical_screen(self, x, y, height, width):
        self.driver.set_window_position (x, y)
        self.driver.set_window_size (height, width)
        # assert isinstance (self.driver.find_element (*self.Path).Clickobject, )
        Path=self.driver.find_element(*self.Path)
        Path.click()
        self.driver.save_screenshot('./gsn/output/img/screen1_1.png')
        for i in range (0,4):
            if i < 4:
                time.sleep(1)
                self.driver.execute_script("window.scrollBy(0,200)")

    def mobile_horizontal_screen(self, x, y, height, width):
        self.driver.set_window_position (x, y)
        self.driver.set_window_size (height, width)
        Path=self.driver.find_element(*self.Path)
        Path.click()
        Path=self.driver.find_element(*self.Path)
        self.driver.save_screenshot('./gsn/output/img/screen1_2.png')
        for i in range (0,5):
            if i < 5:
                time.sleep(1)
                self.driver.execute_script("window.scrollBy(0,200)")

    def tablet_horizontal_screen(self, x, y, height, width):
        self.driver.set_window_position (x, y)
        self.driver.set_window_size (height, width)
        self.driver.save_screenshot('./gsn/output/img/screen1_3.png')
        for i in range (0,4):
            if i < 4:
                time.sleep(1)
                self.driver.execute_script("window.scrollBy(0,200)")

    def tablet_vertical_screen(self, x, y, height, width):
        self.driver.set_window_position (x, y)
        self.driver.set_window_size (height, width)

        self.driver.save_screenshot('./gsn/output/img/screen1_4.png')
        for i in range (0,5):
            if i < 5:
                time.sleep(1)
                self.driver.execute_script("window.scrollBy(0,200)")

from selenium.webdriver.support.ui import Select
from selenium import webdriver
import unittest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class DropDown:

    def __init__(self,myDriver):
        self.driver = myDriver
        self.link_suc= (By.LINK_TEXT,'SUCURSALES')


    def link_gsn(self,value):
           #self.driver.implicitly_wait(5)
           try:
             WebDriverWait(self.driver,5).until(expected_conditions.element_to_be_clickable(self.link_suc))
           except:
             print ('El elemento no es clickeable')
           link_suc=self.driver.find_element(*self.link_suc)
           link_suc.click()

           tc= unittest.TestCase('__init__')
           tc.assertEqual(value, 'SUCURSALES')

    def drop_List(self,val):

        self.driver.set_window_position(500, 200)
        self.driver.set_window_size(375,412)
        link_drop=Select(self.driver.find_element_by_id('sucursal'))
        link_drop.select_by_value(val)








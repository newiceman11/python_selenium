from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
class Form:
    def __init__(self,myDriver):
        self.driver = myDriver
        #usando libreria BY
        self.Name = (By.NAME, 'nombre')




    def function_form(self,value):
        #self.driver.implicitly_wait(5)
        link=self.driver.find_element_by_link_text(value)
        #se convoca a unittest.testCase para incluir assertEqual en el page object
        tc= unittest.TestCase('__init__')
        tc.assertEqual(value, 'CONTACTO')
        link.click()

        #dejamos la busqueda de el elemento a la función y no en el constructor
        self.driver.find_element(*self.Name).send_keys("Juan Pablo Foos")

        self.driver.find_element(*self.Email).send_keys("xxxx@xxxxx.xxx")

        self.driver.find_element(*self.Tel).send_keys("3364646464")

        self.driver.find_element(*self.Asunto).send_keys("Testing")

        self.driver.find_element(*self.Comentario).send_keys("Hola!, testing automatizado con Python Por Juan Pablo Foos")



    def contact_by_tab(self,value,User,Email,Tel,Asunto,Comentario):
        self.driver.implicitly_wait(5)
        link=self.driver.find_element_by_link_text(value)
        tc= unittest.TestCase('__init__')
        tc.assertEqual(value, 'CONTACTO')
        link.click()
        #WebDriverWait(self.driver,10).until(expected_conditions.presence_of_element_located(By.NAME,"enviar"))
        self.driver.find_element(*self.Name).send_keys(User+Keys.TAB+Email+Keys.TAB+Tel+Keys.TAB+Asunto+Keys.TAB+Comentario+Keys.TAB)
        self.driver.save_screenshot('./gsn/output/screen.png')
        time.sleep(2)





from selenium import webdriver
from gsn.Pages import PageDrop, PageForm
from gsn.Helpers import Data
import unittest
import HtmlTestRunner

myData= Data.test_data()

class TestGsn(unittest.TestCase):


    def setUp(self):
        op = webdriver.FirefoxOptions()
        op.add_argument('-headless')
        self.driver = webdriver.Firefox(executable_path = 'geckodriver',firefox_options=op)
        self.driver.get(myData.Url)
        self.page_drop = PageDrop.DropDown(self.driver)
        self.page_form= PageForm.Form(self.driver)

    def test_dropDown(self):
        self.page_drop.link_gsn('SUCURSALES')

        self.page_drop.drop_List('ros')

    #unittest.skip("nada")
    #unittest.skipIf(2>1)
    #unittest.skipUnless()
    def test_form(self):
        #self.page_form.function_form('CONTACTO')
        self.page_form.contact_by_tab('CONTACTO',myData.Persona,'xxxx@xxxxx.xxx','3364646464','Testing','Hola!, es un testing automatizado')



    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    '''unittest.main(
        #testRunner=xmlrunner.XMLTestRunner(output='output'),
        #failfast=False, buffer=False, catchbreak=False)'''
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner('./gsn/output'))

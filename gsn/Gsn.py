from selenium import webdriver
from Pages import PageDrop, PageForm, PageTest
from Helpers import Data
import unittest
import HtmlTestRunner
import time
myData= Data.test_data()


class TestGsn(unittest.TestCase):

    def setUp(self):
        """op = webdriver.FirefoxOptions()
        op.add_argument('-headless')"""
        self.driver = webdriver.Firefox(executable_path=myData.Driver_ff)#,firefox_options=op)
        self.driver.get(myData.Url)
        self.page_drop = PageDrop.DropDown(self.driver)
        self.page_form= PageForm.Form(self.driver)
        self.page_test=PageTest.responsive(self.driver)

    @unittest.skip("Omisión")
    def test_dropDown(self):
        self.page_drop.link_gsn('SUCURSALES')
        self.page_drop.drop_List('ros')


    #unittest.skipIf(2>1)
    #unittest.skipUnless()
    def test_form(self):
        #self.page_form.function_form('CONTACTO')
        self.page_form.contact_by_tab(myData.Contact,myData.Person,myData.Mail,myData.Phone,myData.Subject,myData.Comment)

    def test_responsive1(self):
        self.page_test.mobile_horizontal_screen(myData.Pos_x,myData.Pos_y,myData.Mobile_width,myData.Mobile_height)


    def test_responsive2(self):
        self.page_test.mobile_vertical_screen(myData.Pos_x,myData.Pos_y,myData.Mobile_height,myData.Mobile_width)


    def test_responsive3(self):
        self.page_test.tablet_vertical_screen(myData.Other_pos_x,myData.Pos_y,myData.Table_height,myData.Tablet_width)

   
    def test_responsive4(self):
         self.page_test.tablet_horizontal_screen(myData.Other_pos_x,myData.Pos_y,myData.Tablet_width,myData.Table_height)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    '''unittest.main(
        #testRunner=xmlrunner.XMLTestRunner(output='output'),
        #failfast=False, buffer=False, catchbreak=False)'''
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner('./gsn/output'))

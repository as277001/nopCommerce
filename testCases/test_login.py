from selenium import webdriver
import pytest
from pageObject.LoginPage import Login
from utilities.readProperties import readConfig
from utilities.customLogger import LogGen


class Test_001_Login:
    url=readConfig.geturl()
    username=readConfig.getusername()
    password=readConfig.getpassword()
    logger=LogGen.loggen()

    def test_homePageTitle(self,setup):
        self.logger.info("**********Test_001_Login***********")
        self.logger.info("**********verifying homePageTitle***********")
        self.driver=setup
        self.driver.get(self.url)
        act_title= self.driver.title
        print(readConfig.getusername())
        print(readConfig.getpassword())
        print(readConfig.geturl())
        if act_title=='Your store. Login':
            assert True
            self.driver.close()
            self.logger.info("**********homePageTitle passed***********")
        else:
            self.driver.close()
            self.logger.error("**********homePageTitle failed***********")
            assert False

    def test_login(self,setup):
        self.logger.info("**********verifying login test***********")
        self.driver=setup
        self.driver.get(self.url)
        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        if act_title=='Dashboard / nopCommerce administration':
            assert True
            self.driver.close()
            self.logger.info("**********login test passed***********")
        else:
            self.driver.close()
            self.logger.error("**********login test failed**********")
            assert False

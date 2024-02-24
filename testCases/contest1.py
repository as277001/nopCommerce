from selenium import webdriver
import pytest

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
    elif browser=='firfox':
        driver=webdriver.Firefox()
    else:
        driver=webdriver.Ie()
    return driver

#this will get value from CLI
def pytest_addoption(parser):
    parser.addoption("__browser")

#this will return browser value to setup
@pytest.fixture()
def browser(request):
    return request.config.pgetoption("__browser")

#####pytest html report#######

#it is a hook for adding environment info to html reports
def pytest_configure(config):
    config._metadata['project name']='nop Commerce'
    config._metadata['module name'] = 'Customers'
    config._metadata['Tester'] = 'amit'

#it is a hook for delete/modify environment info to html reports
def pytest_metadata(metadata):
    metadata.pop('JAVA_HOME',None)
    metadata.pop('plugins', None)

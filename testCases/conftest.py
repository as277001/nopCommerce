from selenium import webdriver
import pytest

@pytest.fixture()
def setup():
    dr=webdriver.Chrome()
    return dr
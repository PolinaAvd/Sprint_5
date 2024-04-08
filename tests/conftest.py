import pytest
import settings
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    chrom_driver = webdriver.Chrome()
    chrom_driver.get(settings.URL + "/login")

    return chrom_driver



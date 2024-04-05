import pytest
import settings
from selenium import webdriver

@pytest.fixture(scope='function')
def driver():
    chrom_driver = webdriver.Chrome()
    chrom_driver.get(settings.URL)

    return chrom_driver
@pytest.fixture
def email():
    return {"mail": "polina_avdohina_k7_077@gmail.com"}

@pytest.fixture
def password():
    return {"pass": "Gitera"}
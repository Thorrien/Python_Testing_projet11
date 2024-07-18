import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time

@pytest.fixture
def browser():
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    yield driver
    driver.quit()


def test_login(browser):

    browser.get('http://127.0.0.1:5000/')
    
    email_input = browser.find_element(By.NAME, 'email')
    email_input.send_keys('admin@irontemple.com')
    email_input.send_keys(Keys.RETURN)
    time.sleep(3)
    assert "Points available" in browser.page_source
    time.sleep(3)


def test_listclub(browser):
    browser.get('http://127.0.0.1:5000/')
    email_input = browser.find_element(By.NAME, 'email')
    email_input.send_keys('admin@irontemple.com')
    email_input.send_keys(Keys.RETURN)
    time.sleep(3)

    listclub_btn = browser.find_element(By.NAME, 'clubsbtn')
    listclub_btn.click()
    time.sleep(3)
    assert "Nom du club" in browser.page_source

def test_Book_2_Places(browser):
    browser.get('http://127.0.0.1:5000/')
    email_input = browser.find_element(By.NAME, 'email')
    email_input.send_keys('admin@irontemple.com')
    email_input.send_keys(Keys.RETURN)
    time.sleep(3)

    listclub_btn = browser.find_element(By.NAME, 'Fall Classic')
    listclub_btn.click()
    time.sleep(3)
    assert "Places available: 13" in browser.page_source
    assert "How many places?" in browser.page_source
    place_input = browser.find_element(By.NAME, 'places')
    place_input.send_keys(2)
    place_input.send_keys(Keys.RETURN)
    time.sleep(2)
    assert "Great-booking complete!" in browser.page_source
    listclub_btn = browser.find_element(By.NAME, 'Fall Classic')
    listclub_btn.click()
    time.sleep(3)
    assert "Places available: 11" in browser.page_source


def test_Book_16_Places(browser):
    browser.get('http://127.0.0.1:5000/')
    email_input = browser.find_element(By.NAME, 'email')
    email_input.send_keys('admin@irontemple.com')
    email_input.send_keys(Keys.RETURN)
    time.sleep(3)

    listclub_btn = browser.find_element(By.NAME, 'Fall Classic')
    listclub_btn.click()
    time.sleep(3)
    assert "How many places?" in browser.page_source
    place_input = browser.find_element(By.NAME, 'places')
    place_input.send_keys(16)
    place_input.send_keys(Keys.RETURN)
    time.sleep(3)
    assert "Booking for Fall Classic" in browser.page_source

def test_Book_6_Places(browser):
    browser.get('http://127.0.0.1:5000/')
    email_input = browser.find_element(By.NAME, 'email')
    email_input.send_keys('admin@irontemple.com')
    email_input.send_keys(Keys.RETURN)
    time.sleep(3)

    listclub_btn = browser.find_element(By.NAME, 'Fall Classic')
    listclub_btn.click()
    time.sleep(3)
    assert "How many places?" in browser.page_source
    place_input = browser.find_element(By.NAME, 'places')
    place_input.send_keys(6)
    place_input.send_keys(Keys.RETURN)
    time.sleep(2)
    assert "Refus : Réservation de plus de place que vous avez de points" in browser.page_source
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_buy_button_add_item_to_cart(browser):
    browser.get(link)
    basket_value_el = browser.find_element_by_css_selector(".basket-mini").text
    browser.find_element_by_css_selector(".btn-add-to-basket").click()
    time.sleep(3)
    add_to_basket_button_attr1 = browser.find_element_by_css_selector("button.btn-add-to-basket").get_attribute('type')
    add_to_basket_button_attr2 = browser.find_element_by_css_selector("button.btn-add-to-basket").get_attribute('disabled')
    basket_next_value_el = browser.find_element_by_css_selector(".basket-mini").text
    assert str(add_to_basket_button_attr1) == "submit", "На кнопку нельзя нажать"
    assert str(add_to_basket_button_attr2) == "None" , "Кнока выключена"
    assert basket_value_el != basket_next_value_el, "Стоимость покупок в корзине не изменилась"
    browser.quit()

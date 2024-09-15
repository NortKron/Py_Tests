import time
import random

from constants import TestData as testdata

from selenium import webdriver
from selenium.webdriver.common.by import By

# Автотест покупки товара на сайте saucedemo.com
def test_buying_product(browser: webdriver):

    url_shop_auth = testdata.urls_shop['shop_auth']
    url_shop_main = testdata.urls_shop['inventory']
    url_shop_cart = testdata.urls_shop['cart']

    test_login = testdata.shop_data['login']
    test_password = testdata.shop_data['password']
    test_firstname = testdata.shop_data['firstname']
    test_lastname = testdata.shop_data['lastname']
    test_postalCode = testdata.shop_data['postalCode']

    timeout_load_page = testdata.timeouts['load_page']

    # Процедура авторизации
    browser.get(url_shop_auth)
    current_url = browser.current_url

    # Проверка открытия страницы авторизации
    assert current_url == url_shop_auth, 'Ошибка при переходне на страницу авторизации'

    input_login = browser.find_element(By.ID, 'user-name')
    input_password = browser.find_element(By.ID, 'password')
    button_login = browser.find_element(By.ID, 'login-button')

    input_login.send_keys(test_login)
    input_password.send_keys(test_password)
    button_login.click()

    browser.implicitly_wait(timeout_load_page)
    current_url = browser.current_url

    # Проверка открытия главной страницы магазны
    assert current_url == url_shop_main, 'Ошибка при переходе на главную страницу'

    # Найти все товары на странице
    list_items = browser.find_elements(By.CLASS_NAME, 'inventory_item')

    # Выбрать случайны товар и добавить его в корзину
    rand_index = random.randint(0, len(list_items)-1)
    itemPurch = list_items[rand_index]
    itemPurch_Name = itemPurch.find_element(By.CLASS_NAME, 'inventory_item_name').text
    itemPurch_button_add_to_cart = itemPurch.find_element(By.TAG_NAME, 'button')
    itemPurch_button_add_to_cart.click()

    item_cart = browser.find_element(By.ID, 'shopping_cart_container')
    item_cart.click()

    browser.implicitly_wait(timeout_load_page)
    current_url = browser.current_url

    # Проверка перехода на страницу корзины
    assert current_url == url_shop_cart, 'Ошибка при переходе в корзину'

    # Найти все товары в корзине
    list_items_in_cart = browser.find_elements(By.CLASS_NAME, 'cart_item')
    
    # Проверка наличия товаров в корзине
    assert len(list_items_in_cart) > 0, 'Ошибка: в корзине отсутствуют товары'

    try:
        item_purchased = browser.find_element(By.XPATH, f'//div[text()="{itemPurch_Name}"]')
    except:
        raise AssertionError('Ошибка: товар, добавленны в корзину, не найден в корзине!')
    
    button_checkout = browser.find_element(By.ID, 'checkout')
    button_checkout.click()

    input_firstname = browser.find_element(By.NAME, 'firstName')
    input_lastname = browser.find_element(By.NAME, 'lastName')
    input_postalCode = browser.find_element(By.NAME, 'postalCode')

    input_firstname.send_keys(test_firstname)
    input_lastname.send_keys(test_lastname)
    input_postalCode.send_keys(test_postalCode)

    button_continue = browser.find_element(By.ID, 'continue')
    button_continue.click()

    browser.implicitly_wait(timeout_load_page)

    button_finish = browser.find_element(By.ID, 'finish')
    button_finish.click()

    browser.implicitly_wait(timeout_load_page)

    button_back = browser.find_element(By.ID, 'back-to-products')
    button_back.click()
    
    browser.implicitly_wait(timeout_load_page)

    # Повторный переход на страницу корзины
    item_cart = browser.find_element(By.ID, 'shopping_cart_container')
    item_cart.click()

    # Найти все товары в корзине
    list_items_in_cart = browser.find_elements(By.CLASS_NAME, 'cart_item')
    
    # Корзина должна быть пустой
    assert len(list_items_in_cart) == 0, 'Ошибка: в корзине остались товары'

    print('Тест успешно завершён!')
    time.sleep(2)

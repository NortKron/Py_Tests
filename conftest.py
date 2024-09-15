import pytest
from driver import Driver
from selenium import webdriver

#@pytest.fixture()
@pytest.fixture(scope="session")
def browser() -> Driver:

    # Настройки Google Chrome
    options = webdriver.ChromeOptions()

    # Включение безоконного режима (новой версии)
    options.add_argument('--headless=new')
    #
    options.add_argument('--no-sandbox')
    # Отключить расщирения
    options.add_argument('--disable-extensions')
    # 
    options.add_argument('--disable-gpu')
    # Развернуть окно
    options.add_argument('--start-maximized')
    # отключает использование разделяемой памяти
    options.add_argument('--disable-dev-shm-usage')

    driver = Driver(options=options)

    yield driver
    driver.quit()

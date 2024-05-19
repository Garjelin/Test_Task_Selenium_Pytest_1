import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from .Test_Scenario_0 import Test_Scenario_0
# from ...

from LIB_PAGES.general import Page_general
# from ...

@pytest.fixture(scope="class")
def driver():
    options = webdriver.FirefoxOptions()
    # Устанавливаем параметры ширины и высоты окна браузера
    width = 1600
    height = 900
    options.add_argument(f'--width={width}')
    options.add_argument(f'--height={height}')
    driver_path = '/snap/bin/geckodriver'
    service = webdriver.firefox.service.Service(driver_path)
    service.start()
    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def setup(request, driver):
    # Создаем экземпляры страниц
    request.cls.page_general = Page_general(driver)

# Запускаем все тестовые сценарии
if __name__ == "__main__":
    pytest.main(["-v", "main_script.py"])

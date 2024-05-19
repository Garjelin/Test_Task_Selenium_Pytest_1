import pytest
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
    
class Page_general:

    def __init__(self, driver):
        self.driver = driver

    def start_print(self, msg):
        logging.info("")
        logging.info(f"******{msg}******")
        logging.info("")

    def find_text_h5(self, text):  
        xpath = f'//h5[contains(text(), "{text}")]'
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
    def find_css_selector(self, text):  
        css_selector = f'{text}'
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector)))
    def find_css_selector_in_element(self, element, text): 
        css_selector = f'{text}' 
        return element.find_element(By.CSS_SELECTOR, css_selector)
    def find_id(self, text):  
        id = f'{text}'
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, id)))
    def find_text_span(self, text):  
        xpath = f'//span[contains(text(), "{text}")]'
        return WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, xpath)))
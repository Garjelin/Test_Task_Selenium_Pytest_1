import pytest
import logging
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time


URL = "https://demoqa.com/"
URL_ELEMENTS = "https://demoqa.com/elements"
URL_CHECKBOX = "https://demoqa.com/checkbox"

@pytest.mark.usefixtures("setup")
class Test_Scenario_0:
    def test_scenario_1(self, caplog):
        caplog.set_level(logging.INFO)
        self.page_general.start_print("Test_Scenario_0")

        self.page_general.driver.get(URL)
        current_url = self.page_general.driver.current_url
        logging.info(f"Current URL: {current_url}")
        assert self.page_general.driver.current_url == URL
            
        button_Element = self.page_general.find_css_selector("#app > div > div > div.home-body > div > div:nth-child(1)")
        button_Element_text = button_Element.text
        assert button_Element_text == "Elements"
        logging.info(f"button_Element_text is {button_Element_text}")
        button_Element.click()
        logging.info(f"Clicked on {button_Element_text} button")

        current_url = self.page_general.driver.current_url
        logging.info(f"Current URL: {current_url}")
        assert self.page_general.driver.current_url == URL_ELEMENTS

        element_list_item = self.page_general.find_id("item-1")
        element_list_item_text = element_list_item.text
        assert element_list_item_text == "Check Box"
        logging.info(f"element_list_item_text is {element_list_item_text}")
        element_list_item.click()
        logging.info(f"Clicked on {element_list_item_text} item")

        current_url = self.page_general.driver.current_url
        logging.info(f"Current URL: {current_url}")
        assert self.page_general.driver.current_url == URL_CHECKBOX

        button_collapse_home_close = self.page_general.find_css_selector("#tree-node > ol > li > span > button")
        if not self.page_general.find_css_selector_in_element(button_collapse_home_close, "svg.rct-icon-expand-close"):
            pytest.fail("Element 'button_collapse_home_close' not found")
        assert button_collapse_home_close.is_displayed()
        button_collapse_home_close.click()
        logging.info("Clicked on button_collapse_home_close")
        button_collapse_home_open = self.page_general.find_css_selector("#tree-node > ol > li > span > button")
        if not self.page_general.find_css_selector_in_element(button_collapse_home_open, "svg.rct-icon-expand-open"):
            pytest.fail("Element 'button_collapse_home_open' not found")
        assert button_collapse_home_open.is_displayed()
        logging.info("button_collapse_home_open is opened")
            
        button_collapse_downloads_close = self.page_general.find_css_selector("#tree-node > ol > li > ol > li:nth-child(3) > span > button")
        if not self.page_general.find_css_selector_in_element(button_collapse_downloads_close, "svg.rct-icon-expand-close"):
            pytest.fail("Element 'button_collapse_downloads_close' not found")
        assert button_collapse_downloads_close.is_displayed()
        button_collapse_downloads_close.click()
        logging.info(f"Clicked on button_collapse_downloads_close")
        button_collapse_downloads_open = self.page_general.find_css_selector("#tree-node > ol > li > ol > li:nth-child(3) > span > button")
        if not self.page_general.find_css_selector_in_element(button_collapse_downloads_open, "svg.rct-icon-expand-open"):
            pytest.fail("Element 'button_collapse_downloads_open' not found")
        assert button_collapse_downloads_open.is_displayed()
        logging.info("button_collapse_downloads_open is opened")

        checkbox_word = self.page_general.find_css_selector("#tree-node > ol > li > ol > li.rct-node.rct-node-parent.rct-node-expanded > ol > li:nth-child(1) > span > label > span.rct-checkbox > svg")
        logging.info(f"checkbox is {checkbox_word.text}")
        checkbox_word.click()
        logging.info("checkbox Word File.doc is switched on")

        choose_result_1 = self.page_general.find_text_span("You have selected :")
        assert choose_result_1.text == "You have selected :"
        choose_result_2 = self.page_general.find_text_span("wordFile")
        assert choose_result_2.text == "wordFile"
        logging.info(f"choose_result is {choose_result_1.text} {choose_result_2.text}")

        # time.sleep(5)
            
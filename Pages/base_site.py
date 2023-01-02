from Pages import get_driver
from selenium.webdriver.common.by import By


class BaseSite(object):

    def __init__(self, *args, **kwargs):
        super(BaseSite, self).__init__()
        self._driver = get_driver()


    # def _find_element_by_selector(self, selector, timeout=10):


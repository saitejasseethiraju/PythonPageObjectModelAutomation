from selenium.webdriver import Chrome as ChromeDriver, DesiredCapabilities
from selenium.webdriver.chrome.options import Options as ChromeOptions
from Pages import set_driver
from Pages import set_device
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from hosts import hosts


class LocalBrowser(object):
    _chrome_driver ={'type': ChromeDriver}

    def __init__(self, **kwargs):
        super(LocalBrowser, self).__init__()
        self._driver = None
        self._browser = 'chrome'
        set_device(self)

    @property
    def driver(self):
        if self._driver is None:
            self.start_browser()
            self._driver.implicitly_wait()
        return self._driver

    @driver.setter
    def driver(self, value):
        if self._driver is None:
            self.browser = value

    def start_browser(self):
        if self._browser.lower() == 'chrome':
            self._driver = self.__start_chrome_browser()

        set_driver(self._driver)
        self.navigate_to_url(hosts.Orange_HRM)

    def __start_chrome_browser(self):
        self.browser_opts = ChromeOptions()
        desired = DesiredCapabilities.CHROME
        # driver = self._chrome_driver['type'](,
        #                                      options=self.browser_opts, desired_capabilities=desired,
        #                                      service_args=self._chrome_driver.get('service_args')
        #                                      )
        driver = self._chrome_driver['type'](service=ChromeService(ChromeDriverManager().install()))
        return driver

    def navigate_to_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url()










import pytest
import unittest
import tests
from base.device_manager import DeviceManager
import hosts.hosts
import time
import sys


@pytest.mark.incremental
class BaseTest(unittest.TestCase):
    _site = None
    _device = None
    _device_name =None
    use_chrome_profile = False

    @classmethod
    def get_profile_path(cls):
        if cls.use_chrome_profile:
            if cls._chrome_profile_path is None:
                cls._chrome_profile_path = '/tmp/%s' % time.time()
            return cls._chrome_profile_path

    @property
    def site(self):
        self.OpenHomepage()
        return self._site

    @classmethod
    def OpenHomepage(cls):
        if cls._site is None:
            cls.SetUpSite()
            cls._device.navigate_to_url(url=tests.HOSTNAME)

    @classmethod
    def set_device_name(cls):
        """
        User to set actual device name needed for run
        Method is added to handle CI runs
        :return:
        """
        cmd_line_device_arg = next((arg.split('=')[1] for arg in sys.argv if 'device_name' in arg), tests.device_name)
        if cls.device_name is not None and 'desktop' not in cmd_line_device_arg.lower():
            return
        # if cls.device_name is not None and tests.mobile_safari_default.lower() in cmd_line_device_arg.lower():
        #     cls.device_name = cmd_line_device_arg
        elif 'desktop' in cmd_line_device_arg.lower():
            cls.device_name = cmd_line_device_arg
        else:
            cls.device_name = tests.device_name

    @classmethod
    def SetUpSite(cls):
        if cls._device is None:
            chrome_profile = cls.get_profile_path() if DeviceManager.supported_devices.get(cls.device_name, {}).get(
                'browser', '') == 'chrome' \
                else None
            cls._device = DeviceManager(device_name=cls.device_name, location='IDE',
                                        chrome_profile=chrome_profile).get_device()
            cls._device.start_browser()


def vtest(Cls):
    Cls.device_name = tests.device_name
    device_name = Cls.device_name
    return Cls

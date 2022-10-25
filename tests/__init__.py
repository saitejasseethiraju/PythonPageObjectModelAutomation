import pytest


mobile_default = 'Galaxy S9'
desktop_default = 'Desktop Chrome'
device_name = mobile_default

try:
    device_name = pytest.config.getoption('device_name')
except Exception:
    pass
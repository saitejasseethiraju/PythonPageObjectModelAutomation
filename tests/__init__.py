import pytest
from hosts import hosts
import os
from conftest import pytest_configure


mobile_default = 'Galaxy S9'
desktop_default = 'Desktop Chrome'
device_name = mobile_default
hostname = hosts.Orange_HRM


try:
    # device_name = config.getoption(name="--device_name")
    device_name = os.environ.get('MY_DEVICE_NAME')
    print(f"Device name: {device_name}")
except Exception:
    pass

try:
    hostname = os.environ.get('MY_HOSTNAME')
    print(f"Hostname: {hostname}")
except Exception:
    pass
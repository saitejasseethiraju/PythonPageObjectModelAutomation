import pytest
import os
from hosts import hosts


def pytest_addoption(parser):
    parser.addoption('--hostname', action='store', default=hosts.Orange_HRM,
                     help='Provide hostname as a base for URLs, --hostname=omayo')
    parser.addoption('--device_name', action='store', default='Desktop Chrome',
                     help='select device name, one of: Galaxy S9, Note 4, Nexus 5, iPhone 6S, S7, S8, Desktop Chrome etc.')


def pytest_configure(config):
    print("Running pytest_configure hook...")
    hostname = config.getoption("hostname")
    device_name = config.getoption("device_name")
    os.environ['MY_HOSTNAME'] = hostname
    os.environ['MY_DEVICE_NAME'] = device_name


# @pytest.fixture
# def hostname(request):
#     return request.config.getoption('--hostname')
#
# @pytest.fixture
# def device_name(request):
#     return request.config.getoption('--device_name')


# @pytest.fixture
# def command_line_args(request):
#     args = {}
#     args['hostname'] = request.config.getoption('--hostname')
#     args['device_name'] = request.config.getoption('--device_name')
#     return args
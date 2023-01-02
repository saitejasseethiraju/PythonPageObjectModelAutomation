import pytest
from hosts import hosts


def pytest_addoption(parser):
    parser.addoption('--hostname', action='store', default=hosts.Omayo_Demo,
                     help='Provide hostname as a base for URLs, --hostname=omayo')
    parser.addoption('--device_name', action='store', default='Galaxy S9',
                     help='select device name, one of: Galaxy S9, Note 4, Nexus 5, iPhone 6S, S7, S8, Desktop Chrome etc.')

# @pytest.fixture
def command_line_args(request):
    args = {}
    args['hostname'] = request.config.getoption('--hostname')
    args['device_name'] = request.config.getoption('--device_name')
    return args
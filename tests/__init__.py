import pytest
from hosts import hosts
from conftest import command_line_args

mobile_default = 'Galaxy S9'
desktop_default = 'Desktop Chrome'
device_name = mobile_default
HOSTNAME = hosts.Orange_HRM

try:
    device_name = command_line_args['device_name']
except Exception:
    pass

# try:
#     # HOSTNAME = request_cmd_args.config.getoption('hostname')
# except Exception:
#     pass
from hosts import hosts

def pytest_addoption(parser):
    parser.addoption('--hostname', action='store', default=hosts.Orange_HRM,
                     help='Provide hostname as a base for URLs, --hostname=invictus.coral.co.uk')
    parser.addoption('--device_name', action='store', default='Galaxy S9',
                     help='select device name, one of: Galaxy S9, Note 4, Nexus 5, iPhone 6S, S7, S8, Desktop Chrome etc.')
_global_driver = None
_global_device = None


def set_driver(driver):
    global _global_driver
    _global_driver = driver

def get_driver():
    return _global_driver


def set_device(device):
    global _global_device
    _global_device = device

def get_device():
    return _global_device
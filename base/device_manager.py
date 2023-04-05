from base.local_browser import LocalBrowser


class DeviceManager(object):
    locations = {
        'IDE': {
            'browsers': ['Chrome', 'Firefox', 'Safari'],
            'device_class': LocalBrowser
        },}

    supported_devices = {
        'Galaxy S9': {
            'type': 'mobile',
            'allow_emulation': False,
            'os': 'Android',
            'browser': 'Chrome',
            'dp_resolution': '544x1110',
            'user-agent': 'Mozilla/5.0 (Linux; Android 9.0.0; SM-G960F Build/R16NW) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Mobile Safari/537.36'
        },
        'Desktop Chrome': {
            'type': 'desktop',
            'allow_emulation': False,
            'os': 'Mac OS X',
            'browser': 'Chrome',
            'dp_resolution': '1280x720',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 '
                          '(KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'

        },
    }

    def __init__(self, device_name, location, proxy=None, **kwargs):
        self.location_name = location
        if device_name not in self.supported_devices:
            raise Exception("unsupported decice %s", device_name)
        device_args = self.supported_devices[device_name]
        browser = device_args['browser'].lower()
        device_args.update({'name': device_name, 'browser': browser})
        self.device = LocalBrowser(proxy=proxy, **device_args, **kwargs)

    def get_device(self):
        return self.device





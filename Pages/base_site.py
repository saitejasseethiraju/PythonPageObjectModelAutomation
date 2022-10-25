from Pages import get_driver


class BaseSite(object):

    def __init__(self, *args, **kwargs):
        super(BaseSite, self).__init__()
        self._driver = get_driver()

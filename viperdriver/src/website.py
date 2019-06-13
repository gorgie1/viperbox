from .core import SessionDriver
from ..viperlib.src.jsd import jsondata
from ..viperlib import dir_get
from .. import logger

class logininfo(jsondata):

    def __init__(self):
        self.filename = 'login'
        self._user = None

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, val):
        self._user = val
        self._contents = self.contents[self.user]

    @jsondata.contents.getter
    def contents(self):
        return self._contents


class SitePages(jsondata):

    def __init__(self):
        self.filename = 'pages'

class Websession(SessionDriver):

    _url_home = None
    _url_main = None
    _credentials = None

    _dataloc = None

    def __init__(self):
        super().__init__()
        self._credentials = logininfo()
        self.pages = SitePages()

    def launch(self):
        super().launch()
        self.go_page('Home')

    @property
    def data_location(self):
        return self._dataloc

    @data_location.setter
    def data_location(self, val):
        self._dataloc = val
        self.credentials.location = self._dataloc
        self.credentials.get_from_file()
        self.pages.location = self._dataloc
        self.pages.get_from_file()
        self.session.location = self._dataloc

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, val):
        self._pages = val

    @property
    def credentials(self):
        return self._credentials

    @credentials.setter
    def credentials(self, data):
        self._credentials = data

    def go_page(self, page_name):
        assert page_name in self.pages.contents, 'Page not defined: ' + page_name + '.'
        self.get(self.pages.contents[page_name])
        logger.debug(self.title)

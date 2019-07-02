from selenium.webdriver import Remote
from selenium.webdriver import ChromeOptions
from selenium.webdriver import IeOptions
from ...viperlib.src.jsd import jsondata
from .. import logger, PATH_SELF

kwd_url = 'url'
kwd_sessionid = 'sessionid'
default_listener = 'http://127.0.0.1:9515'
f_session = 'last_session.json'

class Session(jsondata):

    def __init__(self):
        self.contents = { kwd_url: None, kwd_sessionid: None }
        self.url =  default_listener
        self.filename = f_session
        self.location = PATH_SELF
        self._exists = False
        self._savetofile = True

    @property
    def url(self):
        return self.contents[kwd_url]

    @url.setter
    def url(self, val):
        self.contents[kwd_url] = val

    @property
    def session_id(self):
        return self.contents[kwd_sessionid]

    @session_id.setter
    def session_id(self, val):
        self.contents[kwd_sessionid] = val

    @property
    def exists(self):
        return self._exists

    @exists.setter
    def exists(self, val):
        self._exists = val

    @property
    def savetofile(self):
        return self._savetofile

    @savetofile.setter
    def savetofile(self, val):
        self._savetofile = val

    def destroy(self):
        sid = self.session_id # saving id for logger; will be destroyed with execution of next line
        super().destroy()
        logger.debug('Session ' + sid + ' destroyed.')
        self.__init__()

class SessionDriver(Remote):

    options = None
    session = Session()

    def __init__(self, browser='Chrome', headless=True):
        self._browser = browser
        if self._browser is not 'Safari': # no Options exists for Safari
            self.options = eval(self._browser + 'Options()')
        self.options.headless = headless

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.quit()


    def launch(self):
        if self.session.exists:
            try:
                self.session.get_from_file()
                self.session_connect()
                logger.debug('Connected to session ' + self.session.session_id + '.')
            except:
                raise Exception('Could not connect to existing session.')
        else:
            super().__init__(command_executor=self.session.url, options=self.options)
            self.session.session_id = self.session_id
            self.session.exists = True
            logger.debug('Session ' + self.session_id + ' created.')
            if self.session.savetofile:
                self.session.save_to_file()

    def session_connect(self, url=None, sessionid=None):
        if url != None and sessionid != None:
            self.session.url = url
            self.session.session_id = sessionid
        assert self.session.url != None and self.session.session_id != None, __name__ + ": driver session parameters are empty."
        super().__init__(command_executor=self.session.url, desired_capabilities={}, options=self.options)
        self.close()
        self.session_id = self.session.session_id # do not remove: assigning property to RemoteWebDriver parent object

   def switch_to_window(drv, s, strict=False): # strict mode if True: title must match exaclty
       rc = False
       for handle in drv.window_handles:
           drv.switch_to_window(handle)
           if (strict and drv.title == title) or (not strict and s in drv.title):
              rc = drv.title
              return rc    
        
    def quit(self):
        super().quit()
        if self.session.exists:
            self.session.destroy()

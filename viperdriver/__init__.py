import logging

logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
logger.addHandler(console)

PATH_SELF = __path__[0]

KWD_DIR_HOME = 'home'

def switch_to_window(drv, s, strict=False): # strict mode if True: title must match exaclty
   rc = False
   for handle in drv.window_handles:
       drv.switch_to_window(handle)
       if (strict and drv.title == title) or (not strict and s in drv.title):
          rc = drv.title
          return rc

def dropdown_all_options_list_get(drv, elementId):
    lst = []
    items = drv.find_elements_by_xpath('//select[@id=\'' + elementId + '\']/option')
    for item in items:
        lst.append(item.get_attribute('text'))
    return lst

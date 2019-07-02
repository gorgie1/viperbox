import logging

logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
logger.addHandler(console)

PATH_SELF = __path__[0]

KWD_DIR_HOME = 'home'

def dropdown_all_options_list_get(drv, elementId):
    lst = []
    items = drv.find_elements_by_xpath('//select[@id=\'' + elementId + '\']/option')
    for item in items:
        lst.append(item.get_attribute('text'))
    return lst

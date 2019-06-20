"""
vipertools general library.
"""
import calendar
import logging

logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
logger.addHandler(console)

def dir_get(path):
    import os
    s = path.split(os.sep)
    s.pop()
    return os.sep.join(s)

def parent_module_name_get(modulename=__name__):
    return '.'.join(modulename.split('.')[:-1])

def months():
    x = None
    return [x for x in calendar.month_name]

def strdigit_normalize(strdigit):
   if int(strdigit) < 10:
      strdigit = '0' + strdigit
   return strdigit

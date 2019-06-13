"""
vipertools general library.
"""
import calendar
import logging

logger = logging.getLogger(__file__)
logger.setLevel(logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logger.addHandler(console)

def dir_separator_by_platform():
    import sys
    if sys.platform == 'darwin': return '/'
    if sys.platform == 'win32': return '\\'

def dir_get(path):
    separator = dir_separator_by_platform()
    s= path.split(separator)
    s.pop()
    return separator.join(s)

def parent_module_name_get(modulename=__name__):
    return '.'.join(modulename.split('.')[:-1])

def months():
    x = None
    return [x for x in calendar.month_name]

def strdigit_normalize(strdigit):
   if int(strdigit) < 10:
      strdigit = '0' + strdigit
   return strdigit

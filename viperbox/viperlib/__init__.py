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
    """
    Returns directory portion of the path argument.
    """
    import os
    s = path.split(os.sep)
    s.pop()
    return os.sep.join(s)

def parent_module_name_get(modulename=__name__):
    """
    Returns name of the parent module as defined by actual module hierarchy if no argument provided.
    Returns name of the parent module as defined by module hierarchy represented as a string argument.
    Example 1:
    With the following folder structure
    / root
       / dir1
           / dir2
               example.py

    parent_module_name_get() executed in example.py will return dir1.
    Example 2:
    parent_module_name_get('root.whatever.whichever') will return 'root.whatever'.
    """
    if modulename.find(' ') != -1:
        raise ValueError('Wrong argument: must be module tree separated by \'.\'')
    return '.'.join(modulename.split('.')[:-1])

def months():
    """Returns list of names of months. First element is empty."""
    x = None
    return [x for x in calendar.month_name]

def strdigit_normalize(digit):
    """Normalizes input to format '0x'. Example: '9' -> '09'"""
    assert type(digit) is str, 'Invalid input. Must be a string.'
    s = int(digit)
    assert s >= 0, 'Invalid input. Must be string representing a positive number.'
    if s < 10:
      return '0' + str(s)
    return digit

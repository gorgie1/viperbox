from ..src.core import SessionDriver
from .. import KWD_DIR_HOME
import sys

assert len(sys.argv) > 1, 'Location argument required.'

if __name__ == '__main__':
    drv = SessionDriver()
    if sys.argv[1] != KWD_DIR_HOME:
        drv.session.location = sys.argv[1]
    drv.session_exists = True
    drv.launch()
    drv.quit()

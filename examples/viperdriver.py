from . import SeleniumDriver
from . import driver_logger as logger
from . import datafile, session_file_location

drv = SeleniumDriver()
drv.options.headless = False

f = datafile()
f.filename = 'last_session'
f.location = session_file_location
if f.file_exists():
    drv.session_exists = True
    url = input('Session file found: ' + f.full_path() + '. \nWill connect to existing session. \nEnter url:....-> ')
    drv.launch()
    drv.get(url)
    input('Press enter to close the browser:....->')
    drv.quit()
else:
    input('Creating a new browser session (click enter).....->')
    drv.launch()
    drv.session.save_to_file()

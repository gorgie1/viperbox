import os
from .. import logger
import json

class jsondata():

    _f = None
    _dir = None
    _contents = {}

    def __init__(self):
        pass

    @property
    def filename(self):
        return self._f

    @filename.setter
    def filename(self, val):
        if val is not None:
            if not '.json' in val:
                val = val + '.json'
            self._f = val
        else:
            self._f = None

    @property
    def location(self):
        return self._dir

    @location.setter
    def location(self, val):
        self._dir = val

    def full_path(self):
        assert self.location != None, 'File location is not set.'
        return self.location + os.sep + self.filename

    @property
    def contents(self):
        return self._contents

    @contents.setter
    def contents(self, obj):
        self._contents = obj

    def file_exists(self):
        try:
            res = os.path.exists(self.full_path())
            return res
        except:
            return False

    def is_empty(self):
        return self.contents == {}

    def get_from_file(self):
        with open(self.full_path(), 'r') as f:
            self.contents = json.load(f)

    def save_to_file(self):
        with open(self.full_path(), 'w') as f:
            json.dump(self.contents, f)

    def clear(self):
        self.contents = {}
        logger.debug('Contents cleared.')


    def destroy(self):
        self.clear()
        if not self.file_exists() == None:
            try:
                os.remove(self.full_path())
                logger.debug(self.full_path() + ' deleted.')
            except FileNotFoundError:
                pass

    def reset(self):
        self.clear()
        self.destroy()
        self.filename = None
        self.location = None

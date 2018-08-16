import time
from functools import wraps
import unittest
from database.db import Db
from interface.client import Client
from .logger import Log

class TestCase(unittest.TestCase):
    def __init__(self,*args):
        self.logger=Log()
        super().__init__(*args)
    def setUp(self,client, db):
        self.client = Client()
        self.client.read_config(client)
        self.db=Db.read_config(db)







class Timer:
    def __init__(self, func=time.perf_counter):
        self.elapsed = 0.0
        self._start = None
        self._func = func
        
    def start(self):
        if self._start is not None:
            raise RuntimeError('Already started!')
        self._start = self._func()
        
    def stop(self):
        if self._start == None:
            raise RuntimeError('Not started!')
        end = self._func()
        self.elapsed += end - self._start
        self._start = None
        
    def reset(self):
        self.elapsed = 0.0

    @property    
    def running(self):
        return self._start is not None

    def __enter__(self):
        self.start()
        return self
    def __exit__(self, *args):
        self.stop()

def timethis(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        t = Timer()
        t.start()
        result = func(*args, **kwargs)
        t.stop()
        print('{} time spend: {}'.format(func.__name__,t.elapsed))
        return result
    return wrapper


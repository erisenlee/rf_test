import time
import os.path
from functools import wraps
from database.db import Db
from interface.client import Client
# from .logger import Log



def new_report(report_dir):
    dir_list=os.listdir(report_dir)
    dir_list.sort(key=lambda fn: os.path.getmtime(os.path.join(report_dir, fn)))
    file_new = os.path.join(report_dir, dir_list[-1])
    print(file_new)
    return file_new


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


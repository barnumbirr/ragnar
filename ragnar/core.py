#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading

class Threadator(threading.Thread):
    """ The key part to accessing the return value of a thread
        is adding *args and **kwargs to join() in order to handle
        the timeout. See: http://stackoverflow.com/a/25072068
    """

    def __init__(self, *args, **kwargs):
        super(Threadator, self).__init__(*args, **kwargs)
        self._return = None

    def run(self):
        if self._Thread__target is not None:
            self._return = self._Thread__target(*self._Thread__args, **self._Thread__kwargs)

    def join(self, *args, **kwargs):
        super(Threadator, self).join(*args, **kwargs)
        return self._return

def threaded(daemon=False):
    """ @threaded runs a function in a separate thread that can be
        flagged as a 'daemon thread'.
    """

    def decorator(fn):
        def wrapper(*args, **kwargs):
            t = Threadator(target=fn, args=args, kwargs=kwargs)
            t.daemon = daemon
            t.start()
            return t.join()
        return wrapper
    return decorator

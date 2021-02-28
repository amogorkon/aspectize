
import re
from enum import Flag
from inspect import isclass, isfunction, ismethod, ismodule
from time import monotonic

try:
    import q  # type: ignore
except ImportError:
    q = print

ASPECT = Flag("Aspect", "property_set property_get property_del class function method")

last_called = 0

def logged(func):
    def wrapper(*args, **kwargs):
        if type(func) is property:
            q(args[0], "=>",  func.fget.__name__)
            res = func.fget(*args, **kwargs)
            q(args[0], func.fget.__name__, "->", res)
            return res
        q("called", func.__name__, "with", args, kwargs, "->", (res := func(*args, **kwargs)))
        return res
    return wrapper

def cached(func):
    cache = {}  # (args[0] -> (last_called, result)
    
    def wrapper(*args, **kwargs):
        global last_sql_access
        nonlocal cache
        try:
            if cache[args[0]][0] <= last_called:
                res = func.fget(*args, **kwargs)
                cache[args[0]] = monotonic(), res
                return res
            return cache[args[0]][1]
        except KeyError:
            res = func.fget(*args, **kwargs)
            cache[args[0]] = monotonic(), res
            return res
    return wrapper

def aspectize(decorator, aspects=ASPECT.property_get, pattern="^[^__].*"):
    def wrapping (target):
        if isclass(target):
            for name, attr in target.__dict__.items():
                if type(attr) is property and re.match(pattern, name):
                    print(23, name)
                    if ASPECT.property_get in aspects:
                        fget = decorator(attr)
                    if ASPECT.property_set in aspects:
                        setattr(target, name, property(decorator(attr), attr.fset))
        if isfunction(target) and re.match(pattern, target.__name__):
            return decorator(target)
    return wrapping

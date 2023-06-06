#!/usr/bin/python3
LockedClass = __import__('101-locked_class').LockedClass

lc = LockedClass()
lc.first_name = "John"
print(lc.first_name)
try:
    print(lc.last_name)
    lc.last_name = "Snow"
    print(lc.last_name)
    lc.gere = "ty"
    print(lc.gere)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

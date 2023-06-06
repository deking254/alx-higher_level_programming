#!/usr/bin/python3
class LockedClass:
    def __init__(self):
        type(self).first_name = None

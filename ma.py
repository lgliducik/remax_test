# -*- coding: utf-8 -*-
class First():
    pass


class Second():
    pass


class Parent():
    pass


class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


class RevealAccess(object):

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        return self.val

    def __set__(self, obj, val):
        if val == 2:
            raise AttributeError("isSecond = 2")
        self.val = val


class A(First, Parent, object):
    i = 0
    isSecond = RevealAccess(0, 'var "isSecond"')

    def __init__(self):
        self.i = 3
        self.isSecond = 0

    def isFirst(self):
        if self.isSecond == 0:
            return self.isSecond + 1

    def fnc(self, value):
        if value == 7:
            raise MyError("Error text")
        else:
            return value * value * self.i

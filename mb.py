# -*- coding: utf-8 -*-
from ma import *


class B(Second, Parent):
    isSecond = 1

    def __init__(self, value):
        self.value = value
        self.isSecond = 1

    def isFirst(self):
        if self.isSecond == 1:
            return 0

    def fnc(self, value1, value2):
        return value1 * value2 * self.value

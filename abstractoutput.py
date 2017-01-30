#! /usr/local/bin/python
# -*- coding:utf-8 -*-
from abc import *

class AbstractOutput(object):

    def __init__(self):
        pass

    @abstractmethod
    def send(self, data):
        raise NotImplementedError()

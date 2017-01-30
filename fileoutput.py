# -*- coding:utf-8 -*-
from abstractoutput import AbstractOutput
import codecs
#import json

class LocalFileOutput(AbstractOutput):

    def __init__(self, path):
        self.__path = path

    def setFilePath(self, path):
        self.__path = path

    def getFilePath(self):
        return self.__path

    def send(self, data):
        with codecs.open(self.__path, 'a', 'utf-8') as fp:
            fp.write(data)

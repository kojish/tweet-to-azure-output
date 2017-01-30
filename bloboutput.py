# -*- coding:utf-8 -*-
from azure.storage.blob import AppendBlobService
from abstractoutput import AbstractOutput

class BlobStorageOutput(AbstractOutput):

    def __init__(self, accountName, key, container, blobName):
        self.__accountName = accountName
        self.__key = key
        self.__container = container
        self.__blobName = blobName
        self.__service = AppendBlobService(self.__accountName, self.__key)
        self.__service.create_blob(self.__container, self.__blobName)

    def send(self, data):
        self.__service.append_blob_from_text(self.__container,
                                             self.__blobName,
                                             data)

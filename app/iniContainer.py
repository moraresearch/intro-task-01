#!/usr/bin/env python
# encoding: utf-8
"""This module uses for prepare filesystem before container start"""

import os
from fileModule import fileModule
from sqlModule import sqlModule

storageType = os.getenv('STORAGE_TYPE')
if storageType == "fileModule":
    currentClass = fileModule()
if storageType == "sqlModule":
    currentClass = sqlModule()

currentClass.checkIfExists()

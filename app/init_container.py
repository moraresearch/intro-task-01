#!/usr/bin/env python
# encoding: utf-8

import os
from fileModule import fileModule
from sqlModule import sqlModule

STORAGE_TYPE = os.getenv('STORAGE_TYPE')
if STORAGE_TYPE == "fileModule":
    CURRENT_CLASS = fileModule()
if STORAGE_TYPE == "sqlModule":
    CURRENT_CLASS = sqlModule()

CURRENT_CLASS.checkIfExists()

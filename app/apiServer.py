#!/usr/bin/env python
# encoding: utf-8
"""This module uses for main part of apiserver """
import os, time
from flask import Flask, request, Response
from fileModule import fileModule
from sqlModule import sqlModule


app = Flask(__name__)

storageType=os.getenv('STORAGE_TYPE')
if storageType == "fileModule":
  currentClass = fileModule()
if storageType == "sqlModule":
  currentClass = sqlModule()

def resultPlain(resultMessage, statusCode):
    """Func for answer preparation """
    result = Response(response=resultMessage, status=statusCode)
    result.headers["content-type"] = "text/plain"   
    return result

@app.route('/hello',  methods=['GET'])
def helloGet():
    """Hello get handler """
    return resultPlain("Hello Page", 200)


@app.route('/user', methods=['POST'])
def userPost():
    """user post handler """
    args = request.args
    if not args['name']:
        return resultPlain("You shouldn't trying this things.", 400)
    currentTime = time.localtime()
    currentTimeFormat = time.strftime('%H:%M:%S - %d.%m.%Y', currentTime)
    currentClass.insertPostData(args['name'],currentTimeFormat)
    return resultPlain("Message processed", 200)

@app.route('/user', methods=['GET'])
def userPut():
    """user get handler """
    args = request.args
    if not args['name']:
        return resultPlain("You shouldn't trying this things.", 400)
    currentClass.insertGetData()
    return resultPlain(args['name'], 200)

@app.route('/metrics', methods=['GET'])
def metrics():
    """metrics get handler """
    getCounter, postCounter = currentClass.getMetrics()
    getMetric = "intro_get_counter{app=\"intro\"} "+str(getCounter)
    postMetric = "intro_post_counter{app=\"intro\"} "+str(postCounter)
    metricPage = getMetric+"\n"+postMetric
    return resultPlain(metricPage, 200)

app.run(host='0.0.0.0', port=80)

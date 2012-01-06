from flask import Blueprint, render_template, session, redirect, url_for, \
     request, g, jsonify, abort
from functools import wraps
import time
import requests 
import os
import simplejson as json

from flask import Flask, request, Response, jsonify
from flask import json
mod = Blueprint('api', __name__)

@mod.route("/",methods=['POST','PATCH','GET'])
def index():
    return render_template("index.html")
    
@mod.route("/demo/",methods=['POST'])
def demo():
    import envoy
    import heroku
    print 11
    user = request.values['user'].encode("utf-8")
    print 12
    repo = request.values['repo'].encode("utf-8")
    print 13
    username = os.environ['HEROKU_USER']
    print 14
    password = os.environ['HEROKU_PASS']
    print 15
    cloud = heroku.from_pass(username, password)
    print 16
    app = cloud.apps.add()
    try:
        print 1
        r = envoy.run("git clone %s %s" % (repo, app.name.encode("utf-8")), timeout=15)
        print 2
        os.chdir(app.name.encode("utf-8"))
        print 3
        r = envoy.run("git remote add heroku git@heroku.com:%s.git" % app.name.encode("utf-8"))
        print 4
        r = envoy.run('git push heroku master')
        print 5
        app = cloud.apps[app.name]
        print 6
        print user
        app.collaborators.add(user)
        print 7
        app.transfer(user)
        print 8
        result = Response(response = json.dumps({'result': "success", 'name': app.name}), mimetype="application/json")
        print 9
    except Exception, e:
        print e
        app.destroy()
        result = Response(response = json.dumps({'result': "failed"}), mimetype="application/json")
    finally:
        os.chdir("..")
        r = envoy.run("rm -r %s" % app.name.encode("utf-8"))
    return result
        

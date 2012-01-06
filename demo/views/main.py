from flask import Blueprint, render_template, session, redirect, url_for, \
     request, flash, g, jsonify, abort
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
    user = request.values['user'].encode("utf-8")
    repo = request.values['repo'].encode("utf-8")
    username = os.environ['HEROKU_USER']
    password = os.environ['HEROKU_PASS']
    cloud = heroku.from_pass(username, password)
    app = cloud.apps.add()
    try:
        stur = "git clone %s %s" % (repo, str(app.name))
        r = envoy.run("git clone %s %s" % (repo, str(app.name)), timeout=15)
        os.chdir(app.name)
        r = envoy.run("git remote add heroku git@heroku.com:%s.git" % str(app.name))
        r = envoy.run('git push heroku master')
        app = cloud.apps[app.name]
        app.collaborators.add(user)
        app.transfer(user)
        return json.dumps({'result': 'success'})
    except Exception, e:
        os.chdir("..")
        r = envoy.run("rm -r %s" % app.name)
        app.destroy()
        return json.dumps({'result': 'failed'})

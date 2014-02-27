#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import sys,os

BASE_PATH = os.path.dirname(__file__)
LIBS_PATH = os.path.join(BASE_PATH, 'libs')
##设置环境变量
sys.path.append(LIBS_PATH)

from bottle import default_app, run
from bottle import route, mako_template as template, redirect, request, response
from pony.orm import *
from model.user import *

from controller import * #导入所有的控制器
from middleware.session import *
#from setting import site_opt


##首页
@route('/', method='GET')
@db_session
def default():	
	save_user()
	#redirect('list')

@route('/list', method='GET')
@db_session
def list_user():
	users = load_user()
	return template('tpl/user_list',data = users)

def save_user():
	user = User(name="Tset 1",age = 30, sex = "F")
	#user.save()
	studio = Studio(name = 'umessage',user = user)
	#studio.commit()

def load_user():
	return User.select()[:2]

if __name__ == '__main__':
    run(host='localhost', port=8000, debug=True,reloader=True, app = app_middlware)
else:
    application = app_middlware
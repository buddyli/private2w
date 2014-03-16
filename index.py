#!/usr/bin/env python
# -*- encoding:utf-8 -*-

import sys,os

BASE_PATH = os.path.dirname(__file__)
LIBS_PATH = os.path.join(BASE_PATH, 'libs')
##设置环境变量
sys.path.append(LIBS_PATH)

from bottle import default_app, run
from bottle import route, mako_template as template, redirect, request, response, get, post
from bottle import static_file, view #为了不经过controller直接返回诸如html，css等静态文件引入
from bottle import error

from pony.orm import *
from model.tables import *

from controller import * #导入所有的控制器
from middleware.session import *
#from setting import site_opt
from datetime import datetime

# 自定义库
from controller.db_oper import *
from controller.type_oper import *
from controller.item_oper import *
from controller.content_oper import *
from controller.type_oper2 import *

bottle.debug(True)

@error(404)
def error404(error):
    return 'Nothing here, sorry'

#静态资源加载
@route('/static/<filename:path>')
def send_html(filename):
	html_path = os.path.join(BASE_PATH, 'views')
	return static_file(filename, root = html_path)

##首页
@route('/', method='GET')
def default():	
	return template('index', {})

if __name__ == '__main__':
    run(host='localhost', port=8000, debug=True,reloader=True, app = app_middlware)
else:
    application = app_middlware
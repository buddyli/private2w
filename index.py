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
from db_oper import *
from type_oper import *

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
	# save_user()
	# redirect('index.html')
	return template('index', {})

@post('/addItem', method = 'POST')
@db_session
def add_item():
	#request.params可以同时获取到GET或者POST方法传入的参数
	name = request.params.get('name')
	#0：索引；1：非索引
	indexed = request.params.get('indexed')
	if indexed == None:
		indexed = 1
	else:
		indexed = 0

	print name, type(name), indexed
	save_item(name, indexed)
	return template('index', {})

@route('/list_item')
@db_session
def list_item():
	start = request.params.get('start') or '0'
	size = request.params.get('size') or '10'
	items = Item.select()[int(start):(int(start) + int(size))]
	return template('item_list',data = items)

@route('/del_item')
@db_session
def del_item():
	id = request.params.get('id')
	Item[id].delete()
	commit() # 需要手动提交删除
	redirect('/list_item')

@route('/modify_item', method = 'POST')
@db_session
def modify_item():
	id = request.params.get('id')
	name = request.params.get('name')
	#0：索引；1：非索引
	indexed = request.params.get('indexed')
	if indexed == None:
		indexed = 1
	else:
		indexed = 0

	print 'modify item=====%s, %s ,%s' % (id, name, indexed)
	item = Item[id]
	item.set(name = unicode(name, 'utf8'), indexed = int(indexed))
	commit() # 需要手动提交删除
	redirect('/list_item')

@route('/to_modify_item')
@db_session
@view('item_modify')
def to_modify_item():
	id = request.params.get('id')
	item = Item[id]
	return dict(data = item)

if __name__ == '__main__':
    run(host='localhost', port=8000, debug=True,reloader=True, app = app_middlware)
else:
    application = app_middlware
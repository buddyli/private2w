#!/usr/bin/env python
#-*- encoding:utf-8 -*-

from bottle import route, mako_template as template, redirect, request, response, get, post
from bottle import static_file, view #为了不经过controller直接返回诸如html，css等静态文件引入

# from pony.orm import *
# from model.tables import *
from model.documents import *

DATE_FORMAT = '%Y-%m-%d %H:%M:%S' # 入库格式化时间

@post('/add_type', method = 'POST')
# @db_session
def add_item():
	#request.params可以同时获取到GET或者POST方法传入的参数
	name = request.params.get('name')

	# typeObj = Type(name = unicode(name, 'utf8'), addTime = datetime.now())
	# commit()
	return template('index', {})

@route('/list_type')
# @db_session
def list_item():
	start = request.params.get('start') or '0'
	size = request.params.get('size') or '10'
	# items = Type.select()[int(start):(int(start) + int(size))]
	# return template('type_list',data = items)
	return None

@route('/del_type')
# @db_session
def del_item():
	id = request.params.get('id')
	# Type[id].delete()
	# commit() # 需要手动提交删除
	redirect('/list_type')

@route('/modify_type', method = 'POST')
# @db_session
def modify_item():
	id = request.params.get('id')
	name = request.params.get('name')

	# item = Type[id]
	# item.set(name = unicode(name, 'utf8'))
	# commit() # 需要手动提交删除
	redirect('/list_type')

@route('/to_modify_type')
# @db_session
@view('type_modify')
def to_modify_item():
	id = request.params.get('id')
	# item = Type[id]
	# return dict(data = item)
	return None
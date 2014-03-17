#!/usr/bin/env python
#-*- encoding:utf-8 -*-

from datetime import datetime

from bottle import route, mako_template as template, redirect, request, response, get, post
from bottle import static_file, view #为了不经过controller直接返回诸如html，css等静态文件引入

from pony.orm import *
from model.tables import *

@post('/add_item', method = 'POST')
@db_session
def add_item():
	DATE_FORMAT = '%Y%m%d%H%M%S'
	innerName = 'attr_%s' % datetime.now().strftime(DATE_FORMAT)
	#request.params可以同时获取到GET或者POST方法传入的参数
	name = request.params.get('name')
	#0：索引；1：非索引
	indexed = request.params.get('indexed')
	if indexed == None:
		indexed = 1
	else:
		indexed = 0

	dt = datetime.now()
	item = Item(name = unicode(name, 'utf8'), indexed = int(indexed), addTime = dt, innerName = innerName)
	commit()
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
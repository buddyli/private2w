#!/usr/bin/env python
#-*- encoding:utf-8 -*-

from bottle import route, mako_template as template, redirect, request, response, get, post
from bottle import static_file, view #为了不经过controller直接返回诸如html，css等静态文件引入

from pony.orm import *
from model.tables import *

@post('/add_content', method = 'POST')
@db_session
def add_item():
	#request.params可以同时获取到GET或者POST方法传入的参数
	name = request.params.get('name')
	indexed = request.params.get('indexed') or None

	print name, indexed

	if indexed == None:
		indexed = '1'
	else:
		indexed = '0'

	typeObj = Content(name = unicode(name, 'utf8'), addTime = datetime.now(), indexed = int(indexed), itemValue = '{}')
	commit()
	return template('index', {})

@route('/list_content')
@db_session
def list_item():
	start = request.params.get('start') or '0'
	size = request.params.get('size') or '10'
	items = Content.select()[int(start):(int(start) + int(size))]
	return template('content_list',data = items)

@route('/del_content')
@db_session
def del_item():
	id = request.params.get('id')
	Content[id].delete()
	commit() # 需要手动提交删除
	redirect('/list_content')

@route('/modify_content', method = 'POST')
@db_session
def modify_item():
	id = request.params.get('id')
	name = request.params.get('name')
	indexed = request.params.get('indexed') or None

	if indexed == None:
		indexed = '1'
	else:
		indexed = '0'

	item = Content[id]
	item.set(name = unicode(name, 'utf8'), addTime = datetime.now(), indexed = int(indexed))
	commit() # 需要手动提交删除
	redirect('/list_content')

@route('/to_modify_content')
@db_session
@view('content_modify')
def to_modify_item():
	id = request.params.get('id')
	item = Content[id]
	return dict(data = item)

# 跳转到添加内容，级联加载类型及其对应的条目
@route('/to_add_content')
@db_session
@view('content_add')
def to_add_content():
	types = Type.select()
	# items = Item.select()
	# typeItems = TypeItem.select()

	return dict(types = types)

@route('/selectItems', method = 'POST')
@db_session
def selectItems():
	# from json_encoder_decoder import MyEncoder, MyDecoder
	import json
	from MyEncoder import MyEncoder

	typeId = request.params.get('typeId')
	print typeId
	sql = "select * from tbl_type_item where type_id = %s " % typeId
	typeItems = TypeItem.select_by_sql(sql)

	itemId = '('
	size = 0
	for tmp in typeItems:
		size += 1
		itemId += str(tmp.itemId)

		if size != len(typeItems):
			itemId += ','
	itemId += ')'

	items = Item.select_by_sql("select * from tbl_item where id in %s" % itemId)
	itemList = []
	for item in items:
		print MyEncoder().default(item)
		itemList.append(MyEncoder().default(item))

	response.content_type = 'application/json'
	return json.dumps(itemList)

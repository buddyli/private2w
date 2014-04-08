#!/usr/bin/env python
#-*- encoding:utf-8 -*-

from bottle import route, mako_template as template, redirect, request, response, get, post
from bottle import static_file, view #为了不经过controller直接返回诸如html，css等静态文件引入

# from pony.orm import *
# from model.tables import *
from model.documents import *

@route('/to_add_type_item')
# @db_session
@view('type_item')
def add_type_item():
	typeId = request.params.get('id')
	# typeObj = Type[typeId]
	# # raw sql
	# sql = "select * from tbl_type_item where type_id = %s " % typeId
	# typeItems = TypeItem.select_by_sql(sql)
	# print typeItems

	# items = Item.select()

	# return dict(data = typeObj, items = items, selectedItems = typeItems)

	typeObj = Type.objects(id=typeId)[0]
	items = Item.objects();

	return dict(data = typeObj, items = items)


@route('/add_type_item', method = "POST")
# @db_session
@view('index')
def add_type_item():
	id = request.params.get('id')
	# 新的关联条目ID
	selectedItems = request.params.getall('items')
	itemList = []

	if selectedItems==None or len(selectedItems)==0:#如果取消了关联，将item清空
		pass
	else:#更新关联关系
		for itemId in selectedItems:
			itemList.append(itemId)

	Type.objects(id=id).update(set__items=itemList)
	# # 关联表中已经存在的所有条目
	# itemsInDB = TypeItem.select()

	# # 删除中间表旧的关联关系
	# try:
	# 	for item in itemsInDB:
	# 		# print id, type(id), item.typeId, type(item.typeId)
	# 		if item.typeId == int(id):
	# 			print item.id, item.typeId, item.itemId
	# 			TypeItem[item.id].delete()
	# except Exception, e:
	# 	print 'Exception when delete old type_item relations... %s' % e

	# # 依次保存类型-条目对应关系
	# if selectedItems != None and len(selectedItems) > 0:
	# 	try:
	# 		for item in selectedItems:
	# 			#保存新的映射关系
	# 			typeItem = TypeItem(typeId = int(id), itemId = int(item))

	# 	except CommitException, e:
	# 		print '依次保存类型-条目对应关系异常: %s' % e

	# commit()
	# return {}
	redirect('/list_type')
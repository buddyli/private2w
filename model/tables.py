#!/usr/bin/env python
#-*- encoding:utf-8 -*-
#Filename: item.py, 条目对象

from datetime import datetime
from pony.orm import *
from pony.converting import str2datetime#用来将字符串形式的日期转换成datetime类型的变量
from database import db

# db = Database('mysql', host='172.16.22.77', user='root', passwd='root', db='private2w')

class Type(db.Entity):
	_table_ = 'tbl_type'

	id = PrimaryKey(int, auto = True, column = 'id')
	name = Required(unicode, column = 'name')
	addTime = Optional(datetime, column = 'add_time')

class Item(db.Entity):
	_table_ = 'tbl_item'

	id = PrimaryKey(int, auto = True, column = 'id')
	name = Required(unicode, column = 'name')
	indexed = Optional(int, column = 'indexed', default = 0)
	addTime =  Optional(datetime, column = 'add_time')

class TypeItem(db.Entity):
	_table_ = 'tbl_type_item'

	typeId = Required(int, column = 'type_id')
	itemId = Required(int, column = 'column_id')
	PrimaryKey(typeId, itemId)

class Content(db.Entity):
	_table_ = 'tbl_content'

	id = PrimaryKey(int, auto = True, column = 'id')
	name  = Required(unicode, column = 'name')
	typeId = Optional(int, column = 'type_id')
	# addTime = Required(datetime, column = 'add_time', sql_default = 'CURRENT_TIMESTAMP')
	# 由于sql_default编译不通过，这里需要使用str2datetime将当前时间字符串转换成datetime类型再插入表中
	addTime = Optional(datetime, column = 'add_time')
	indexed = Optional(int, column = 'indexed', default = 0)
	itemValue = Optional(unicode, column = 'item_value')

#创建表格并且生成映射关系
db.generate_mapping(create_tables = True)
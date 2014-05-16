#!/usr/bin/env python
#-*- encoding:utf-8 -*-
import os
from datetime import datetime

from bottle import route, mako_template as template, redirect, request, response, get, post
from bottle import static_file, view #为了不经过controller直接返回诸如html，css等静态文件引入

from setting import *
from model.documents import *

DATE_FORMAT = '%Y-%m-%d %H:%M:%S' # 入库格式化时间

@route('/to_add_pic')
def to_add_item():
	pic_dir = site_opt['pic_dir']

	return template('views/system/pic/add', site_opt = site_opt)

@route('/add_pic', method = 'POST')
def add_item():
	name = request.forms.get('name')
	upload = request.files.get('file')
	name, ext = os.path.splitext(upload.filename)
	
	save_path = site_opt['pic_dir']
	print name, ext, save_path
	upload.save(save_path)

	# item = Pic(name=unicode(name, 'utf8'))
	# item.save()
	redirect('list_pic')

@route('/list_pic')
# @db_session
def list_item():
	start = request.params.get('start') or '0'
	size = request.params.get('size') or '1000'
	items = Pic.objects[int(start):(int(start) + int(size))]
	data = {
		'items': items
	}
	return template('views/system/pic/list', data = data, site_opt = site_opt)

@route('/del_pic')
# @db_session
def del_item():
	id = request.params.get('id')
	# commit() # 需要手动提交删除
	Pic.objects(id=id).delete()
	redirect('/list_pic')
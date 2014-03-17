#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import json
from model.tables import Item

class MyEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, Item):
			return [obj.id, obj.name, obj.indexed, obj.innerName]
		else:
			return json.JSONEncoder.default(self, obj)
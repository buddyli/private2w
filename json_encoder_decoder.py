#!/usr/bin/env python
# -*- encoding:utf-8 -*-
'''
Created on 2014-03-03
@author: lichuanbao.buddy@gmail.com

自定义的Object-JSON互相转换的工具类。因为json.dumps()方法支持的是字典，直接传入对象会报错，因此这里转换一下。
'''
# import Person
import json
 
# p = Person.Person('Peter',22)
 
class MyEncoder(json.JSONEncoder):
    def default(self,obj):
        #convert object to a dict
        d = {}
        d['__class__'] = obj.__class__.__name__
        d['__module__'] = obj.__module__
        d.update(obj.__dict__)
        return d
 
class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self,object_hook=self.dict2object)
    def dict2object(self,d):
        #convert dict to object
        if'__class__' in d:
            class_name = d.pop('__class__')
            module_name = d.pop('__module__')
            module = __import__(module_name)
            class_ = getattr(module,class_name)
            args = dict((key.encode('ascii'), value) for key, value in d.items()) #get args
            inst = class_(**args) #create new instance
        else:
            inst = d
        return inst
 
 
# d = MyEncoder().encode(p)
# o =  MyDecoder().decode(d)
#  
# print d
# print type(o), o
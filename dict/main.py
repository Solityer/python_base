##字典

#创建字典
a = {}
print(type(a))
b = dict()
print(type(b))
#可以在创建的同时指定初始值
#键值对之间使用 , 分割   键和值之间使用 : 分割. (冒号后面推荐加一个空格)
student = {
    'id': 1,
    'name': 'zhangsan'  #最后一个键值对的都逗号可写可不写
}

#查找key
#使用in可以判定key是否在字典中存在.返回布尔值(与value无关)
print('id' in student)
print('score' in student)
print('score' not in student)

#使用 [ ] 可以根据 key 来新增/修改 value
c = {
    'id': 1,
    'name': 'zhangsan',  #最后一个键值对的都逗号可写可不写
    100: 'list'
}
print(c['id'])
print(c['name'])
print(c[100])
#如果 key 在字典中不存在, 则会抛出异常.
#print(c['classid'])

##新增/修改元素
d = {
    'id': 1,
    'name': 'solity'
}
print(f'原始值:{d}')
#使用 [ ] 可以根据 key 来新增/修改 value.
d['score'] = 90  #往字典中加入新的键值对
print(f'新增键值后:{d}')
d['score'] = 100  #不存在就新增键值对,存在的话就是修改value
print(f'修改新增键值后:{d}')

##删除元素
#使用 pop 方法根据 key 删除对应的键值对.
e = {
    'id': 1,
    'name': 'solity',
    'score': 100
}
print(f'原始元素:{e}')
e.pop('score')
print(f'删除元素后:{e}')

##遍历字典元素
g = {
    'id': 1,
    'name': 'solity',
    'score': 20
}
for key in g:
    print(key,g[key]) #print(key,value)

#使用 keys 方法可以获取到字典中的所有的 key
#此处 dict_keys 是一个特殊的类型, 专门用来表示字典的所有 key. 大部分元组支持的操作对于dict_keys 同样适用
print(g.keys())
#使用 values 方法可以获取到字典中的所有 value
print(g.values())
#使用 items 方法可以获取到字典中所有的键值对
print(g.items())
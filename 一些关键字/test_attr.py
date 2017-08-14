# -*- coding:itf-8 -*-

print getattr(Instance, 'name', 'not find') # 如果Instance 对象中有属性name则self.name的值，否则打印"not find"
print getattr(a, 'method', 'default') # 如果有方法method,打印其地址，否则打印default
print getattr(a, 'method', 'default')() # 如果有方法method，运行函数并打印None，否则打印default

hasattr(object, name) # 判断object是否包含name属性

setattr(object, name, value) # 设置object中name属性为value

delattr(object, name) # 删除object中的name属性
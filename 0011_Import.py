# 模块是.py文件
import pizza_0011 as p  # 导入整个模块 as取别名
from fun_0011 import fun1 as f1  # 导入部分函数 as可以给函数取别名
from fun_0011 import *  # 导入模块中所有函数

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

fun1()
fun2('syb')

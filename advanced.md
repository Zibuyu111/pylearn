# Python Advanced: Underlying Principles & Engineering Practices

## Garbage Collection

> 编程语言自动管理内存机制，程序运行时不再使用的变量、对象、数据称之为垃圾。GC自动识别并释放他们占用的内存，无需在编程时手动编写。
> programming languages feature automatic memory management,g
> garbage refers to unused values,objects and data during program execution.GC automatically identifies garbage and frees the memory they occupy,so developers do not need to write manual memory management code during coding.

- C/C++:需要手动管理 / need manual memory management
- Python/Java/JS 自带GC自动回收 / built-in automatic garbage collection

### 垃圾判别核心逻辑/Core logic of Garbage Identification

`核心规则：引用计数 / core rules: reference counting`
每个对象自带一个引用计数器：

- 变量赋值、传入函数、存入列表 -> 引用计数 + 1
- 变量删除 del x、变量生命周期结束、重新赋值 x=None -> 引用计数 -1

Every objects is equipped with an embedded reference counter:

- variable assignment,pass into a function,store in a list -> reference count + 1
- variable deletion del x,end of variable lifetime,reasignment x=None -> reference count - 1

当引用计数=0被判别为垃圾，进回收
When an object's reference count equals zero,it is marked as garbage and will be reclaimed immediately.

在python中采取两种回收方案
Two garbage collection strategies are implemented in Python.

- Reference Counting 引用计数法回收
- Mark/Sweep 标记-清除分代回收

通过混合方案，即实现及时回收，又兜底循环引用

```python
#获取对象的引用计数
  import sys
  ls = list(range(0,3))
  sys.getrefcount(ls) - 1
#在函数调用ls时会增加一次

  a = 11
  sys.getrefcount(a)
#a 指向这个小整数池 -5～256 CPython解释器启动时会一次性创建好-5 到 256 所有整数对象，存入全局缓存池、全局复用、不会销毁。
```

```python
  import gc
  gc.get_count()
  #获取到0-2代数目
  gc.collect()
  #触发一次回收
```

## Generator

> 惰性迭代器，一次只产生一个entity。在python中不存在脱离yield而存在的generator。
> Lazy iterator generates only one entity at a time.In python, every generator relies on the `yield` keyword.

- 生成器函数，明文写yield / generator function, visible writing
- 生成器表达式，隐藏在语法糖当中 / Generator expressions are wrapped in syntactic sugar

惰性迭代由于是懒加载，故而不能进行索引跳转，不具备连续序列的随机访问能力。在原生环境下惰性迭代器一次只有一个entity，单次产生一个hashable。

Since lazy iterators adopt lazy loading, they cannot index jump and lack the random access capability of contiguous sequences. In native environments, a lazy iterator holds only one entity at any time and yields one hashable object per iteration.

```python
del f():
    for i in range(3):
        yield i

g = f()
for _ in range(3):
    print(next(g))
"""echo
0
1
2
"""
```

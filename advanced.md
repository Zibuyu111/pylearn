# Python Advanced: Underlying Principles & Engineering Practices

## Garbage Collection
> 编程语言自动管理内存机制，程序运行时不再使用的变量、对象、数据称之为垃圾。GC自动识别并释放他们占用的内存，无需在编程时手动编写。

- C/C++:需要手动管理
- Python/Java/JS 自带GC自动回收

### 垃圾判别核心逻辑

`核心规则：引用计数`
每个对象自带一个引用计数器：- 变量赋值、传入函数、存入列表 -> 引用计数 + 1 - 变量删除 del x、变量生命周期结束、重新赋值 x=None -> 引用计数 -1

当引用计数=0被判别为垃圾，进回收

在python中采取两种回收方案

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

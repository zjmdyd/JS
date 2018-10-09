#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random, time, queue
from multiprocessing.managers import BaseManager

# 创建类似的QueueManager
class QueueManager(BaseManager):
    pass

# 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字
QueueManager.register("get_task_queue")
QueueManager.register("get_result_queue")

# 连接到服务器，也就是运行task_master.py的机器
# 端口和验证码注意保持与task_master.py设置的完全一致

manager = QueueManager(address=("localhost", 5000), authkey=b"abc")

# 从网络连接
manager.connect()

# 获取Queue的对象
task = manager.get_task_queue()
result = manager.get_result_queue()

# 从task队列取任务,并把结果写入result队列
for i in range(10):
    n = task.get(timeout=1)
    print("获取任务：%s"% n)
    time.sleep(2)
    result.put(n*n)

if hasattr(manager, "shutdown"):
    manager.shutdown()
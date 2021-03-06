#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# 很多时候，子进程并不是自身，而是一个外部进程。我们创建了子进程后，还需要控制子进程的输入和输出
import subprocess
print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)
print('\n')
# class subprocess.Popen(args, bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None, 
#     preexec_fn=None, close_fds=True, shell=False, cwd=None, env=None, universal_newlines=False,
#     startup_info=None, creationflags=0, restore_signals=True, start_new_session=False, pass_fds=())
# 参数说明：

# args： 要执行的shell命令，可以是字符串，也可以是命令各个参数组成的序列。当该参数的值是一个字符串时，该命令的解释过程是与平台相关的，因此通常建议将args参数作为一个序列传递。
# bufsize： 指定缓存策略，0表示不缓冲，1表示行缓冲，其他大于1的数字表示缓冲区大小，负数 表示使用系统默认缓冲策略。
# stdin, stdout, stderr： 分别表示程序标准输入、输出、错误句柄。
# preexec_fn： 用于指定一个将在子进程运行之前被调用的可执行对象，只在Unix平台下有效。
# close_fds： 如果该参数的值为True，则除了0,1和2之外的所有文件描述符都将会在子进程执行之前被关闭。
# shell： 该参数用于标识是否使用shell作为要执行的程序，如果shell值为True，则建议将args参数作为一个字符串传递而不要作为一个序列传递。
# cwd： 如果该参数值不是None，则该函数将会在执行这个子进程之前改变当前工作目录。
# env： 用于指定子进程的环境变量，如果env=None，那么子进程的环境变量将从父进程中继承。如果env!=None，它的值必须是一个映射对象。
# universal_newlines： 如果该参数值为True，则该文件对象的stdin，stdout和stderr将会作为文本流被打开，否则他们将会被作为二进制流被打开。
# startupinfo和creationflags： 这两个参数只在Windows下有效，它们将被传递给底层的CreateProcess()函数，用于设置子进程的一些属性，如主窗口的外观，进程优先级等。

child = subprocess.Popen(['ping', '-c', '4', 'www.baidu.com'])
print('parent process')
# Popen对象创建后，主程序不会自动等待子进程完成。我们必须调用对象的wait()方法，父进程才会等待 (也就是阻塞block)

print('\n')
child2 = subprocess.Popen('ping -c4 www.baidu.com',shell=True)
child2.wait()
print('parent process')

# child.poll() # 检查子进程状态
# child.kill() # 终止子进程
# child.send_signal() # 向子进程发送信号
# child.terminate() # 终止子进程

# 子进程的PID存储在child.pid

# 可以在Popen()建立子进程的时候改变标准输入、标准输出和标准错误，并可以利用subprocess.PIPE将多个子进程的输入和输出连接在一起，构成管道(pipe)


# ping命令参数:
# -d：使用Socket的SO_DEBUG功能；
# -c<完成次数>：设置完成要求回应的次数；
# -f：极限检测；
# -i<间隔秒数>：指定收发信息的间隔时间；
# -I<网络界面>：使用指定的网络界面送出数据包；
# -l<前置载入>：设置在送出要求信息之前，先行发出的数据包；
# -n：只输出数值；
# -p<范本样式>：设置填满数据包的范本样式；
# -q：不显示指令执行过程，开头和结尾的相关信息除外；
# -r：忽略普通的Routing Table，直接将数据包送到远端主机上；
# -R：记录路由过程；
# -s<数据包大小>：设置数据包的大小；
# -t<存活数值>：设置存活数值TTL的大小；
# -v：详细显示指令的执行过程。


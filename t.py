# !usr/bin/env python  
# -*- coding:utf-8 _*-  
""" 
@author:dandan.zheng 
@file: t.py 
@time: 2018/03/19 
"""
import os, time, threading
from multiprocessing import Process, Pipe, Queue, Value, Lock, Pool
# 多线程
def Hello(name):
    print('child threading: {}'.format(threading.get_ident()))
    print ('Hello '+name)

# 进程池
def f(i):
    print(i, end = ' ')

# 进程同步
def func(val, lock):
    for i in range(50):
        time.sleep(0.1)
        with lock:
            val.value += 1


# 进程通信
conn1, conn2 = Pipe()
queue = Queue()


def f1(conn):
    # print ('f1')
    conn.send('Hello')


def f2(conn):
    # print ('f2')
    data = conn.recv()
    print(data)


def f3(queue):
    queue.put('world')


def f4(queue):
    data = queue.get()
    print(data)


def main():
    # 多线程
    t = threading.Thread(target=Hello, args=('shiyanlou',))
    t.start()
    t.join()
    print('main {} stop'.format(threading.get_ident()))
    # 进程池
    # pool = Pool(processes=3)
    # for i in range(30):
    #     pool.apply(f, (i,))
    # pool.close()
    # pool.join()

    # 进程同步
    # v = Value('i', 0)
    # lock = Lock()
    # procs = [Process(target=func, args=(v, lock)) for i in range(10)]
    # for p in procs:
    #     p.start()
    # for p in procs:
    #     p.join()
    # print(v.value)

    # Process(target=f1, args=(conn1,)).start()
    # Process(target=f2, args=(conn2,)).start()
    # Process(target=f3, args=(queue,)).start()
    # Process(target=f4, args=(queue,)).start()

if __name__ == '__main__':
    main()
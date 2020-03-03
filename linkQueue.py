# -*- coding: utf-8 -*-
"""
@author: 唐帆
@time: 2020/02/03 17:00
链接队列
静态查找

"""

from uuid import uuid1


class LinkQueue(object):
    def __init__(self):
        self.front = None
        self.rear = None
        self.elem = {}
        self.node = {"data": None, "next": None}


class LinkQueuePublic(LinkQueue):
    def destructor(self):
        """
        析构函数
        :return:
        """
        self.elem = {}
        self.front = None
        self.rear = None

    def enqueue(self, data):
        key = str(uuid1())
        self.node["data"] = data
        if self.rear is None:
            self.front = key
        else:
            self.elem[self.rear]["next"] = key
        self.rear = key
        self.elem[key] = self.node
        self.node = {"data": None, "next": None}

    def dequeue(self):
        front = self.front
        front_unit = self.elem[front]
        front_data = front_unit["data"]
        self.front = front_unit["next"]
        if front_unit["next"] is None:
            self.rear = None
        del self.elem[front]
        return front_data

    def top(self):
        front = self.front
        front_unit = self.elem[front]
        front_data = front_unit["data"]
        return front_data

    def is_empty(self):
        return self.rear == self.front == None


if __name__ == "__main__":
    link_queue = LinkQueuePublic()
    for i in range(0, 15):
        link_queue.enqueue(i)
    print(link_queue.elem)
    print('front', link_queue.front, 'rear', link_queue.rear)
    print('dequeue', link_queue.dequeue())
    print('dequeue', link_queue.dequeue())
    print('top', link_queue.top())
    print('is_empty', link_queue.is_empty())
    for i in range(0, 13):
        link_queue.dequeue()
    print(link_queue.elem)
    print('is_empty', link_queue.is_empty())

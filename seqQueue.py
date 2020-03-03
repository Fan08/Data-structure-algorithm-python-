# -*- coding: utf-8 -*-
"""
@author: 唐帆
@time: 2020/01/31 21:43
循环队列（顺序实现）
静态查找

"""


class SeqQueue(object):
    def __init__(self):
        self.elem = []
        self.max_size = 10
        for i in range(0, self.max_size):
            self.elem.append(None)
        self.front = 0
        self.rear = 0


class SeqQueuePublic(SeqQueue):
    def double_space(self):
        old_elem = self.elem
        new_elem = []
        for i in range(0, self.max_size * 2):
            new_elem.append(None)
        for i in range(0, len(old_elem)):
            new_elem[i] = old_elem[(self.front + i) % self.max_size]
        self.elem = new_elem
        self.front = 0
        self.rear = self.max_size - 1
        self.max_size *= 2

    def enqueue(self, new_one):
        if (self.rear + 1) % self.max_size == self.front:
            SeqQueuePublic().double_space()
        self.rear = (self.rear + 1) % self.max_size
        self.elem[self.rear] = new_one

    def dequeue(self):
        front = (self.front + 1) % self.max_size
        first_one = self.elem[front]
        self.elem[front] = None
        return first_one

    def is_empty(self):
        return self.front == self.rear


if __name__ == "__main__":
    seq_queue = SeqQueuePublic()
    seq_queue.enqueue(1)
    print("入队", seq_queue.elem)
    seq_queue.double_space()
    print("翻倍", seq_queue.elem)
    seq_queue.dequeue()
    print("判空", seq_queue.is_empty())
    print("出队", seq_queue.elem)

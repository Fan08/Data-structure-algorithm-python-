# -*- coding: utf-8 -*-
"""
@author: 唐帆
@time: 2020/02/21 19:15

优先级队列的实现，最小堆
实现失败

"""
import random


class PriorityQueue(object):
    def __init__(self):
        self.maxSize = 9
        self.currentSize = 0
        # 0位不使用
        self.array = [-1] * 10

    def double_size(self):
        size = len(self.array)
        self.array.extend([-1] * size)
        self.maxSize = len(self.array)-1

    def create_queue_with_old_queue(self, old_queue):
        self.array = old_queue
        self.currentSize = 1

    def destructor(self):
        """
        析构函数
        :return:
        """
        self.array = [-1]
        self.currentSize = 0

    def is_empty(self):
        return self.currentSize == 0

    def get_head(self):
        # 舍零位不使用
        return self.array[1]

    def enqueue(self, x):
        x = int(x)
        if self.currentSize == self.maxSize:
            self.double_size()
        hole = self.currentSize + 1
        self.currentSize += 1
        while hole > 1 and x < self.array[hole//2]:
            self.array[hole] = self.array[hole//2]
            hole //= 2
        self.array[hole] = x

    def dequeue(self):
        max_item = self.array[1]
        self.array[1] = self.array[self.currentSize]
        self.array[self.currentSize] = -1
        self.currentSize -= 1
        self.percolate_down(1)
        return max_item

    def percolate_down(self, hole):
        """
        向下过滤
        :return:
        """
        tmp = self.array[hole]
        while hole*2 <= self.currentSize:
            child = hole * 2
            print("self.array[child]", self.array[child], hole, self.currentSize)
            if child != self.currentSize and self.array[child+1] > self.array[child]:
                child += 1
            if self.array[child] > tmp:
                print(hole, child)
                self.array[hole] = self.array[child]
            # else:
            #     break
            hole = child
        print("hole", hole)
        self.array[hole] = tmp


if __name__ == "__main__":
    priority_queue = PriorityQueue()
    for i in range(0, 10):
        a = random.randint(0, 100)
        priority_queue.enqueue(a)
    print(priority_queue.array)
    print(priority_queue.dequeue())
    print(priority_queue.array)


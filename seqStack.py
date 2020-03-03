# -*- coding: utf-8 -*-
"""
@author: 唐帆
@time: 2020/01/29 12:44
顺序栈
静态查找

"""


class SeqStack(object):
    def __init__(self):
        self.elem = []
        self.top_p = -1
        self.max_size = 10


class SeqStackPublic(SeqStack):
    def destructor(self):
        """
        析构函数
        :return:
        """
        index = 0
        while index < len(self.elem):
            del self.elem[index]
            index += 1
        self.top_p = -1
        self.max_size = 10

    def is_empty(self):
        return self.top_p == -1

    def push(self, new_elem):
        if self.top_p == self.max_size - 1:
            SeqStackPublic().double_size()
        self.top_p += 1
        self.elem.append(new_elem)
        return True

    def pop(self):
        if self.top_p == -1:
            return "Stack is empty."
        top_one = self.elem[self.top_p]
        del self.elem[self.top_p]
        self.top_p -= 1
        return top_one

    def top(self):
        if self.top_p == -1:
            return "Stack is empty."
        return self.elem[self.top_p]

    def double_size(self):
        return self.max_size * 2


if __name__ == "__main__":
    seq_stack = SeqStackPublic()
    print("isEmpty", seq_stack.is_empty())
    print("push", seq_stack.push({"12": "12"}))
    print("top", seq_stack.top())
    print("double_size", seq_stack.double_size())
    print("pop", seq_stack.pop())

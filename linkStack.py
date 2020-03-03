# -*- coding: utf-8 -*-
"""
@author: 唐帆
@time: 2020/02/03 18:49
链接栈
静态查找

"""

from uuid import uuid1


class LinkStack(object):
    def __init__(self):
        """
        elem：所有节点的集合
        node：单个节点的定义
            data：节点数据
            next：指向后继节点的指针
        """
        self.elem = {}
        self.node = {"data": None, "next": None}
        self.top_p = None


class LinkStackPublic(LinkStack):
    def destructor(self):
        """
        析构函数
        :return:
        """
        self.elem = {}

    def is_empty(self):
        if self.elem:
            return False
        else:
            return True

    def push(self, new_data):
        key = str(uuid1())
        old_head = self.top_p
        self.top_p = key
        self.node["data"] = new_data
        if self.top_p is None:
            self.node["next"] = None
        else:
            self.node["next"] = old_head
        self.elem[key] = self.node
        self.node = {"data": None, "next": None}

    def pop(self):
        old_head = self.top_p
        head = self.elem[old_head]
        next_head = head["next"]
        del self.elem[old_head]
        self.top_p = next_head
        return head["data"]

    def top(self):
        top_p = self.top_p
        head = self.elem[top_p]
        return head["data"]


if __name__ == "__main__":
    link_stack = LinkStackPublic()
    link_stack.push("1")
    print("is_empty", link_stack.is_empty())
    link_stack.push("2")
    print("elem", link_stack.elem)
    print("top_p", link_stack.top_p)
    print("pop", link_stack.pop())
    print("top", link_stack.top())
    link_stack.destructor()
    print("elem", link_stack.elem)
    print("is_empty", link_stack.is_empty())

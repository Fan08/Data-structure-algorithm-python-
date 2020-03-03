# -*- coding: utf-8 -*-
"""
@author: 唐帆
@time: 2020/02/04 13:25
二叉树
树是由节点构成的，因此没有统一的字典

"""

from 数据结构和算法.浙大课程.linkQueue import LinkQueuePublic
from 数据结构和算法.浙大课程.linkStack import LinkStackPublic


class BinaryTree(object):
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None


class BinaryTreePublic(BinaryTree):
    def make_tree(self, data, left_tree, right_tree):
        """
        两树变一树
        :param data:
        :param left_tree:
        :param right_tree:
        :return:
        """
        self.data = data
        elem_of_left_tree = left_tree.elem
        elem_of_right_tree = right_tree.elem
        self.left = elem_of_left_tree
        self.right = elem_of_right_tree

    @staticmethod
    def pre_order(tree):
        """
        前序遍历
        :param tree:
        :return:
        """
        if tree is not None:
            if tree.left is not None or tree.right is not None:
                print(tree.data)
                BinaryTreePublic.pre_order(tree.left)
                BinaryTreePublic.pre_order(tree.right)
            else:
                print(tree.data)

    @staticmethod
    def pre_order_without_recursion(tree):
        link_stack = LinkStackPublic()
        link_stack.push(tree)
        while link_stack.is_empty() is False:
            current = link_stack.pop()
            print(current.data)
            if current.right is not None:
                link_stack.push(current.right)
            if current.left is not None:
                link_stack.push(current.left)


def create_tree():
    """
    以命令行输入的方式获取每个节点的值，从而产生树
    :return:
    """
    start = input("输入根节点：")
    binary_tree = BinaryTree()
    binary_tree.data = start
    queue = LinkQueuePublic()
    queue.enqueue(binary_tree)
    while queue.is_empty() is False:
        tmp = queue.dequeue()
        left_child = input("输入左子节点：")
        right_child = input("输入右子节点：")
        if left_child != "@":
            left_child_tree = BinaryTree()
            left_child_tree.data = left_child
            tmp.left = left_child_tree
            queue.enqueue(left_child_tree)
        if right_child != "@":
            right_child_tree = BinaryTree()
            right_child_tree.data = right_child
            tmp.right = right_child_tree
            queue.enqueue(right_child_tree)
    print("创建完成！")
    BinaryTreePublic().pre_order_without_recursion(binary_tree)


create_tree()

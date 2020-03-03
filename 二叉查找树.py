# -*- coding: utf-8 -*-
"""
@author: 唐帆
@time: 2020/02/29 20:12

动态查找

"""

from random import randint


class BinarySearchTree(object):
    def __init__(self):
        self.root = None
        self.node_type = {
            "data": None,
            "left": None,
            "right": None,
        }

    def make_empty(self):
        self.root = None

    def insert(self, x, binary_node):
        # x = float(x)
        if binary_node is None:
            self.node_type["data"] = x
            binary_node = self.node_type
            self.node_type = {
                "data": None,
                "left": None,
                "right": None,
            }
            return binary_node
        elif x < binary_node["data"]:
            binary_node["left"] = BinarySearchTree().insert(x, binary_node["left"])
            return binary_node
        elif x > binary_node["data"]:
            binary_node["right"] = BinarySearchTree().insert(x, binary_node["right"])
            return binary_node

    @staticmethod
    def remove(x, binary_node):
        if binary_node is None:
            return "树为空！"
        if x < binary_node["data"]:
            binary_node["left"] = BinarySearchTree().remove(x, binary_node["left"])
            return binary_node
        elif x > binary_node["data"]:
            binary_node["right"] = BinarySearchTree().remove(x, binary_node["right"])
            return binary_node
        elif binary_node["right"] is not None and binary_node["left"] is not None:
            tmp = binary_node["right"]
            while tmp["left"] is not None:
                tmp = tmp["left"]
            binary_node["data"] = tmp["data"]
            binary_node["right"] = BinarySearchTree().remove(binary_node["data"], binary_node["right"])
            return binary_node
        else:
            if binary_node["left"] is not None:
                binary_node = binary_node["left"]
            else:
                binary_node = binary_node["right"]
            return binary_node

    @staticmethod
    def find(x, binary_node):
        if binary_node is None:
            return False
        elif x < binary_node["data"]:
            result = BinarySearchTree().find(x, binary_node["left"])
            return result
        elif x > binary_node["data"]:
            result = BinarySearchTree().find(x, binary_node["right"])
            return result
        else:
            return True


if __name__ == "__main__":
    binary_search_tree = BinarySearchTree()
    int_list = []
    for i in range(0, 10):
        a = randint(0, 100)
        int_list.append(a)
        new_tree = binary_search_tree.insert(a, binary_search_tree.root)
        binary_search_tree.root = new_tree
    print(binary_search_tree.root)
    print(int_list[2])
    print(binary_search_tree.remove(int_list[2], binary_search_tree.root))
    print(binary_search_tree.find(int_list[2], binary_search_tree.root))

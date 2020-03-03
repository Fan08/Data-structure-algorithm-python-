# -*- coding: utf-8 -*-
"""
@author: 唐帆
@time: 2020/02/06 13:59
表达式树
特点：二叉树
遍历：中序遍历
缺陷：1) 91行
     2) 由于在for循环中无法对遍历对象进行操作，导致括号内的内容会被重复

"""

from uuid import uuid1
from re import compile

from 数据结构和算法.浙大课程.binaryTree import BinaryTreePublic, BinaryTree
from 数据结构和算法.浙大课程.seqStack import SeqStackPublic


class ExpressionTree(object):
    def __init__(self):
        super().__init__()
        self.float_data = compile(r'^[-+]?[0-9]+\.[0-9]+$')
        self.int_data = compile(r'^[0-9]+$')
        self.add = "ADD"
        self.sub = "SUB"
        self.multi = "MULTI"
        self.div = "DIV"
        self.left_paren = "LEFT_PAREN"
        self.right_paren = "RIGHT_PAREN"
        self.data = "DATA"
        self.number_stack = SeqStackPublic()
        self.single_stack = SeqStackPublic()
        self.expression = []

        self.node = {"type": None, "data": None, "left_child": None, "right_child": None}
        self.root = None

    def input_expression(self):
        expression = []
        expression_str = []
        input_value = True
        while input_value:
            print("".join(expression_str))
            inputted = input("输入字符（以end结尾）：")
            expression_str.append(inputted)
            if inputted == "end":
                input_value = None
            else:
                if self.int_data.match(inputted):
                    expression.append(int(inputted))
                elif self.float_data.match(inputted):
                    expression.append(float(inputted))
                else:
                    expression.append(inputted)
        return expression

    def get_token(self, value):
        value_type = None
        if self.int_data.match(str(value)):
            value_type = self.data
        elif self.float_data.match(str(value)):
            value_type = self.data
        elif value == "/":
            value_type = self.div
        elif value == "*":
            value_type = self.multi
        elif value == "+":
            value_type = self.add
        elif value == "-":
            value_type = self.sub
        elif value == "(" or value == "（":
            value_type = self.left_paren
        elif value == ")" or value == "）":
            value_type = self.right_paren
        return value_type

    def create_expression_tree(self, expression, skip_number=None):
        for i in expression:
            return_type = self.get_token(i)
            self.node["data"] = i
            self.node["type"] = return_type
            if return_type == self.data or return_type == self.left_paren:
                if return_type == self.left_paren:
                    self.node = ExpressionTree().create_expression_tree(expression[expression.index(i)+1:])
                if self.root is None:
                    self.root = self.node
                elif self.root['right_child'] is None:
                    self.root['right_child'] = self.node
                else:

                    # 下一行是根据上交的课件直接做的，但是不合理，无法实现
                    # 使用1+2*3测试时，2会被3覆盖
                    self.root['right_child']['right_child'] = self.node

            elif return_type == self.right_paren:
                return self.root
            elif return_type == self.add or return_type == self.sub:
                old_root = self.root
                self.root = self.node
                self.root["left_child"] = old_root
            elif return_type == self.multi or return_type == self.div:
                if self.root["type"] == self.data or self.root["type"] == self.multi or self.root["type"] == self.div:
                    old_root = self.root
                    self.root = self.node
                    self.root["left_child"] = old_root
                else:
                    old_root_right = self.root["right_child"]
                    self.node["right_child"] = old_root_right
                    self.root["right_child"] = self.node
            self.node = {"type": None, "data": None, "left_child": None, "right_child": None}
        return self.root

    @staticmethod
    def pre_order(tree):
        """
        前序遍历
        :param tree:
        :return:
        """
        if tree is not None:
            if tree["left_child"] is not None or tree["right_child"] is not None:
                ExpressionTree.pre_order(tree["left_child"])
                print(tree["data"])
                ExpressionTree.pre_order(tree["right_child"])
            else:
                print(tree["data"])


expression_1 = ExpressionTree()
expression_1.expression = expression_1.input_expression()
a = expression_1.create_expression_tree(expression_1.expression)
ExpressionTree().pre_order(a)
# print(a["left_child"]["left_child"])
# a = ExpressionTree().get_token("+")
# print(a)

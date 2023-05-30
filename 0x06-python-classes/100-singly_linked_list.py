#!/usr/bin/python3
"""This is a module for greeting and performing square calculations."""


class Node:
    """Node class"""
    __data = None
    __next_node = None

    def __init__(self, data, next_node=None):
        """init func"""
        self.data = data
        self.next_node

    @property
    def data(self):
        """data property"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """data setter"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """next_node getter"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """next node setter"""
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise("next_node must be a Node object")


class SinglyLinkedList:
    """SinglyLinkedList class"""

    def __init__(self):
        """init func"""
        self.__head = None

    def sorted_insert(self, value):
        """sorted insert func"""
        node = Node(value)
        if self.__head is None:
            node.next_node = None
            self.__head = node
        elif self.__head.data > value:
            node.next_node = self.__head
            self.__head = node
        else:
            new = self.__head
            while (new.next_node is not None and new.next_node.data < value):
                new = new.next_node
                node.next_node = new.next_node
                new.next_node = node

    def __str__(self):
        """make class printable"""
        values = []
        temp = self.__head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))

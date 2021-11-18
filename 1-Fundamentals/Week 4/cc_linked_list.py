#!/usr/bin/env python

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print(f"Head note created: {self.head.value}")
            return

        node = self.head
        while node.next is not None:
            node = node.next
        print(f"Appended new node with value: {node.next.value}")

    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            print(f"Head note created: {self.head.value}")
            return

        if self.head is not None:
            new_node.next = self.head
            print(f"Prepended new Head Node with value: {new_node.value}")
            print(f"Node following Head is: {self.head.value}")
            return


node1 = Node("node1")
node2 = Node("node2")
node3 = Node("node3")

llist = LinkedList()
llist.prepend("First Node")
llist.prepend("Inserted New First Node")

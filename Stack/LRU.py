# https://leetcode.com/problems/lru-cache/description/

class LRUCache:

    class Node:
        def __init__(self, key, val):
            self.key = key
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}

        self.head = self.Node(-1, -1)
        self.tail = self.Node(-1, -1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def addNode(self, node):
        temp = self.head.next

        node.next = temp
        node.prev = self.head

        self.head.next = node
        temp.prev = node

    def deleteNode(self, node):
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = nextNode
        nextNode.prev = prevNode

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]
        self.deleteNode(node)
        self.addNode(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            node = self.map[key]
            node.val = value
            self.deleteNode(node)
            self.addNode(node)
            return

        if len(self.map) == self.capacity:
            lru = self.tail.prev
            self.deleteNode(lru)
            del self.map[lru.key]

        newNode = self.Node(key, value)
        self.addNode(newNode)
        self.map[key] = newNode
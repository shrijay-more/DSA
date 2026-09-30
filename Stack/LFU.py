class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.freq = 1
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def addFront(self, node):
        temp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp
        temp.prev = node
        self.size += 1

    def removeNode(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        self.size -= 1


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.keyNode = {}   # key -> node
        self.freqList = {}  # freq -> DLL
        self.minFreq = 0
        self.currSize = 0

    def updateFreq(self, node):
        freq = node.freq
        self.freqList[freq].removeNode(node)

        if freq == self.minFreq and self.freqList[freq].size == 0:
            self.minFreq += 1

        node.freq += 1

        if node.freq not in self.freqList:
            self.freqList[node.freq] = DLL()

        self.freqList[node.freq].addFront(node)

    def get(self, key: int) -> int:

        if key not in self.keyNode:
            return -1

        node = self.keyNode[key]
        self.updateFreq(node)
        return node.value
    

    def put(self, key: int, value: int) -> None:

        if self.capacity == 0:
            return

        if key in self.keyNode:

            node = self.keyNode[key]
            node.value = value

            self.updateFreq(node)
            return

        if self.currSize == self.capacity:

            dll = self.freqList[self.minFreq]

            nodeToRemove = dll.tail.prev

            dll.removeNode(nodeToRemove)

            del self.keyNode[nodeToRemove.key]

            self.currSize -= 1

        newNode = Node(key, value)

        self.minFreq = 1

        if 1 not in self.freqList:
            self.freqList[1] = DLL()

        self.freqList[1].addFront(newNode)

        self.keyNode[key] = newNode

        self.currSize += 1
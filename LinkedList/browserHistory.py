class Node:
    def __init__(self, url):
        self.url = url
        self.prev = None
        self.next = None


class BrowserHistory:
    def __init__(self, homepage):
        self.curr = Node(homepage)

    def visit(self, url):
        newNode = Node(url)

        # remove forward history
        self.curr.next = None

        # connect new page
        self.curr.next = newNode
        newNode.prev = self.curr

        # move current to new page
        self.curr = newNode

    def back(self, steps):
        while steps > 0 and self.curr.prev is not None:
            self.curr = self.curr.prev
            steps -= 1

        return self.curr.url

    def forward(self, steps):
        while steps > 0 and self.curr.next is not None:
            self.curr = self.curr.next
            steps -= 1

        return self.curr.url
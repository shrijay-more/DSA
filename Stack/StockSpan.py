# https://leetcode.com/problems/online-stock-span/description/
class StockSpanner:

    def __init__(self):
        self.st = []
        self.ind = -1

    def next(self, price: int) -> int:
        self.ind += 1

        while self.st and self.st[-1][0] <= price:
            self.st.pop()

        if not self.st:
            span = self.ind + 1
        else:
            span = self.ind - self.st[-1][1]

        self.st.append((price, self.ind))

        return span
    
stock = StockSpanner()


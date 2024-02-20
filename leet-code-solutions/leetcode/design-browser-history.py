class URLNode():
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = URLNode(homepage)
        self.tail = self.head

    def visit(self, url: str) -> None:
        nodo = URLNode(url)
        self.tail.next = nodo
        nodo.prev = self.tail
        self.tail = nodo
        curr = self.head
        while curr:
            print(curr.val, end = ",")
            curr = curr.next
        print()

    def back(self, steps: int) -> str:
        while self.tail and self.tail.prev and steps != 0:
            self.tail = self.tail.prev
            steps-=1
        return self.tail.val

    def forward(self, steps: int) -> str:
        while self.tail and self.tail.next and steps != 0:
            self.tail = self.tail.next
            steps-=1
        return self.tail.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = ListNode(homepage)
        
        

    def visit(self, url: str) -> None:
        new_node = ListNode(url)
        # yourself
        new_node.prev= self.curr
        self.curr.next = new_node
        self.curr = self.curr.next

        

    def back(self, steps: int) -> str:
        curr = self.curr

        while curr.prev and steps > 0:
            curr = curr.prev
            steps -=1

        self.curr = curr
        return curr.val

    def forward(self, steps: int) -> str:
        curr = self.curr

        while curr.next and steps > 0:
            curr = curr.next
            steps-=1

        self.curr = curr
        return curr.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
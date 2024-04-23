# Problem: Design browser history  - https://leetcode.com/problems/design-browser-history/

class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = 0
        self.history = [homepage]

    def visit(self, url: str) -> None:
        self.cur += 1
        if self.cur < len(self.history):
            self.history[self.cur] = url
            self.history = self.history[:self.cur+1]  # Truncate the history beyond current position
        else:
            self.history.append(url)



    def back(self, steps: int) -> str:
        self.cur = max(self.cur - steps, 0)
        return self.history[self.cur]

    def forward(self, steps: int) -> str:
        self.cur = min(self.cur + steps, len(self.history) - 1)
        return self.history[self.cur]
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
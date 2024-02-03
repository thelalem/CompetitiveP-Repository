class Solution:
    def defangIPaddr(self, address: str) -> str:
        defanged = ""
        for s in address:
            if s == ".":
                new += "[.]"
            else:
                new += s
        return new
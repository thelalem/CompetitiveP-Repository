class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        var = 0
        for operation in operations:
            if operation[1] == "+":
                var += 1
            else:
                var -= 1
        return var
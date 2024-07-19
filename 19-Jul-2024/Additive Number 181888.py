# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        for i in range(1, n):
            for j in range(i+1, n):
                num1, num2 = num[:i], num[i:j]

                if (num1.startswith('0') and len(num1) > 1) or (num2.startswith('0') and len(num2) > 1):
                    continue
                
                num1, num2 = int(num1), int(num2)
                
                start = j
                while start < n:
                    num3 = num1 + num2
                    num3_str = str(num3)
                    num3_len = len(num3_str)
                    
                    if not num.startswith(num3_str, start):
                        break
                
                    start += num3_len
                    num1, num2 = num2, num3
                
                if start == n:
                    return True
        return False

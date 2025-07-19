class Solution:
    def isArmstrong(self, n):

        x = n
        count = 0
        
        while x > 0:
            x //= 10  
            count += 1

        y = n
        add = 0
        while y > 0:
            digit = y % 10
            sq = digit ** count
            add += sq
            y //= 10
        
        if add == n:
            print("the num is armstrong num")
        else:
            print("the num is not armstrong num")

s = Solution()
s.isArmstrong(153)

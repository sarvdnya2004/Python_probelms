class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        let = s.split()

        print(len(let[len(let)-1]))

s = Solution()
sen = "sam is my name"
s.lengthOfLastWord(sen)

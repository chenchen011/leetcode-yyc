#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文�?
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # ����һ��ֱ�ӷ�ת�ж��Ƿ����
        # s = str(x)
        # if (s == s[::-1]):
        #     return True
        # else:
        #     return False

        # �ֶ���ת����
        num = x
        res = 0

        if (x < 0):
            return False

        while (num != 0):
            res = res*10+num % 10
            num = num//10

        return res == x

# @lc code=end

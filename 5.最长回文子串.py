#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子�?
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:

        res = ""

        # i��ʾ���ģ� ö��ÿ�������ַ�����
        # ����������ָ��l��r�ֱ������ƶ�
        for i in range(len(s)):

            # �����ַ�Ϊ����
            l, r = i-1, i+1
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                l = l-1
                r = r+1
            # ����res
            if (r-l-1 > len(res)):
                res = s[l+1:r]

            # �����ַ�Ϊż��
            l, r = i, i+1
            while (l >= 0 and r < len(s) and s[l] == s[r]):
                l = l-1
                r = r+1
            if (r-l-1 > len(res)):
                res = s[l+1:r]

        return res

# @lc code=end

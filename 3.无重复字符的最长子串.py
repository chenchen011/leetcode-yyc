#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子�?
#

# @lc code=start

# �������ڷ�
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        w = []  # ��������
        max_length = 0

        # �����ַ���
        for c in s:
            # ����ַ����ڻ��������У������ַ������봰��
            if c not in w:
                w.append(c)

            # ����ַ����ڴ������Ѿ�����
            else:
                # �Ӵ������Ƴ��ظ��ַ���֮ǰ���ַ������֣����ַ�����Ϊ���ظ��ַ����ַ���
                w[:] = w[w.index(c)+1:]
                # ����ǰ�ַ����봰��
                w.append(c)

            max_length = max(len(w), max_length)

        return max_length


# @lc code=end

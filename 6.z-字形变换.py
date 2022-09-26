#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        res = [""]*(numRows)  # ����['', '', '', '']��ÿһ�������洢���е�����
        flag = -1  # ��������һ�������һ��flag�ı�
        i = 0  # ��ʾ��

        if (numRows < 2):
            return s

        # ģ��z�ֹ��̣��ȴ��ϵ����ٴ��µ��ϣ���������һ�������һ��ʱ��i���򣬼�flagȡ��
        # ����ŵ�res�У�n���ַ�����ÿ���ַ����ֱ�洢һ�е��ַ�
        for c in s:
            res[i] = res[i]+c

            if (i == 0 or i == numRows-1):
                flag = -flag

            i = i+flag*1

        return "".join(res)

        # @lc code=end

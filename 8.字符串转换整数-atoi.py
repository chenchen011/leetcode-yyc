#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整�? (atoi)
#

# @lc code=start

class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2147483647
        INT_MIN = -2147483648

        str = s.lstrip()  # �����߶���Ŀո�
        num_re = re.compile(r'^[\+\-]?\d+')  # �����������
        #  ^��ʾ���еĿ�ͷƥ�䣬��֤��+-0-9��ͷ������ֻ�����������֡�
        num = num_re.findall(str)  # ����ƥ�������

        # ^[\+\-]?\d+
        # ^ ��ʾƥ���ַ�����ͷ������ƥ��ľ��� '+'  '-'  ��
        # [] ��ʾƥ���������һ�ַ�������[0-9]����ƥ�������ַ� 0 - 9 �е�һ��
        # ? ��ʾǰ��һ���ַ�������λ���һ�Σ������� ? ����Ϊ '+' �ſ���ʡ��
        # \d ��ʾһ������ 0 - 9 ��Χ
        # + ��ʾǰ��һ���ַ�����һ�λ��߶�Σ�\d+ ��һ�����ƥ��һ����������

        # �޷���list��Ԫ��ֱ��ת��Ϊint��������Ҫ�Ƚ��
        num = int(*num)  # ���ڷ��ص��Ǹ��б����������ת��������

        return max(min(num, INT_MAX), INT_MIN)  # ����ֵ
# @lc code=end

#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # ģ����ʽ�ӷ���ȡ��������ÿһλ����ֵ����Ӻ�����µ������м��ɣ���Ҫע���λ
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # ��ʼ���������������
        # ����ListNode��class��Ҫ��ʼ����֮��ֵ��ʱ��ͬ��
        dummy = ListNode(0)
        node = dummy

        node_1 = l1
        node_2 = l2
        carry = 0  # ��λ

        while (node_1 or node_2 or carry):

            num_1 = 0
            num_2 = 0

            if node_1:
                num_1 = node_1.val  # ��ȡ��ǰ�ڵ��ֵ
                node_1 = node_1.next  # ǰ������һ���ڵ�
            if node_2:
                num_2 = node_2.val
                node_2 = node_2.next

            if (num_1+num_2+carry > 9):  # ��Ҫ��λ��ʱ��
                res = num_1+num_2+carry-10
                node.next = ListNode(res)  # �³�ʼ��һ���ڵ㣬Ȼ�����ӵ�node��
                carry = 1
            else:
                res = num_1+num_2+carry
                node.next = ListNode(res)
                carry = 0

            node = node.next  # ǰ������һ���ڵ�

        return dummy.next  # һ��Ҫ���س�ʼ����ͷ
# @lc code=end

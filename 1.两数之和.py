#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # ����ѭ��Ч�ʽϵͣ����ù�ϣ���Ż�
        # ÿ��ѭ�������ݷ����ϣ���У��ж�target-num�Ƿ��ڹ�ϣ���м���
        hashmap = {}  # �ֵ�
        for index, item in enumerate(nums):     # enumerate��ͬʱ�о���������ֵ
            if (target-item in hashmap):        # ���target-item��hashmap�У�
                return hashmap[target-item], index    # �򷵻�target-item��item������
            # ����ֵ�洢��hashmap�У��ֵ���ʽ{item1:index1 ,item2:index2, ...}��
            hashmap[item] = index

# @lc code=end

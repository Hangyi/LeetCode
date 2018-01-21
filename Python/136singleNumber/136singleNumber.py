# time: O(n)
# space: O(1)

class Solution(object):
    def singleNumber(self, nums):
        chs = 0 
        for i in nums:
            chs ^= i  # XOR
        return chs

    # solution2 math
    # def singleNumber(self, nums):
    #     return 2 * sum(set(nums)) - sum(nums)

    # solution3
    # def singleNumber(self, nums):
    #     hash_table = {}
    #     for i in nums:
    #         try:
    #             hash_table.pop(i)
    #         except:
    #             hash_table[i] = 1
    #     return hash_table.popitem()[0]
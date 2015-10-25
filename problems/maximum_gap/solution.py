#!/usr/bin/env python

class Solution(object):
    # Radix sort
    def MaxGap(self, nums):
        if len(nums) < 2:
            return 0
        num_strs = []
        max_size = 1
        for s in nums:
            num_strs.append(str(s)[::-1])
            max_size = max(max_size, len(str(s)))
        print num_strs
        for i in range(max_size):
            buckets = [[] for j in range(10)]
            for s in num_strs:
                # Move smaller number to left most bucket
                if len(s) <= i:
                    buckets[0].append(s)
                else:
                    buckets[int(s[i])].append(s)
            print buckets
            num_strs = []
            for j in range(10):
                num_strs.extend(buckets[j])
        nums = [int(x[::-1]) for x in num_strs]
        print nums
        max_gap = 0
        for x in range(len(nums) - 1):
            max_gap = max(max_gap, nums[x+1] - nums[x])

        return max_gap



l1 = [123, 78, 457, 234, 345, 320]

if __name__ == '__main__':
    s = Solution()
    print s.MaxGap(l1)




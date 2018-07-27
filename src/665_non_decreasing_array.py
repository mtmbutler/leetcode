# https://leetcode.com/problems/non-decreasing-array/description/

class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        divs = [[nums[0]]]
        arr_num = 0
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                divs.append([])
                arr_num += 1
            divs[arr_num].append(nums[i])

        # print(str(nums))
        # print(str(divs))

        if len(divs) < 2:
            return True
        elif len(divs) > 2:
            return False
        elif len(divs) == 2:
            if len(divs[0]) < 2 or len(divs[1]) < 2:
                return True
            elif divs[0][-2] <= divs[1][0] or divs[0][-1] <= divs[1][1]:
                return True
            else:
                return False
        else:
            return False

if __name__ == '__main__':
    sol = Solution()
    nums = [0,2,4,2,3,4,5,6,9]
    print(sol.checkPossibility(nums))
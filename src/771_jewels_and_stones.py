# https://leetcode.com/problems/jewels-and-stones/description/

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """

        count = 0
        for char in S:
            if char in J:
                count += 1

        return count

if __name__ == '__main__':
    sol = Solution()
    print(sol.numJewelsInStones('aA', 'aAAbbbb'))
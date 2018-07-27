# https://leetcode.com/problems/valid-number/description/

class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            f = float(s)
            return True
        except:
            return False

def main():
    sol = Solution()
    test_cases = ['0','0.1','abc','1 a','2e10']
    for case in test_cases:
        print('Input: {}\nOutput: {}'.format(case, sol.isNumber(case)))

if __name__ == '__main__':
    main()
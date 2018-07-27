# https://leetcode.com/problems/string-to-integer-atoi/description/

class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = str.strip()

        neg = False
        if s.startswith('-'):
            s = s[1:]
            neg = True
        elif s.startswith('+'):
            s = s[1:]

        digits = ''
        for char in s:
            if char in ['0','1','2','3','4','5','6','7','8','9']:
                digits += char
            else:
                break
        if not digits:
            return 0

        try:
            if neg:
                return max(-2**31,-1*int(digits))
            else:
                return min(2**31-1,int(digits))
        except:
            return 0

def main():
    sol = Solution()
    test_cases = ['42','   -42','4193 with words','words and 987','-91283472332']
    for case in test_cases:
        print('Input: {}\nOutput: {}\n------------'.format(case, sol.myAtoi(case)))

if __name__ == '__main__':
    main()
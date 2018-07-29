"""
https://leetcode.com/problems/integer-to-roman/description/

Roman numerals are represented by seven different symbols: I, V, X, L,
C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added
together. Twelve is written as, XII, which is simply X + II. The number
twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to
right. However, the numeral for four is not IIII. Instead, the number
four is written as IV. Because the one is before the five we subtract it
making four. The same principle applies to the number nine, which is
written as IX. There are six instances where subtraction is used:

 - I can be placed before V (5) and X (10) to make 4 and 9.
 - X can be placed before L (50) and C (100) to make 40 and 90.
 - C can be placed before D (500) and M (1000) to make 400 and 900.

Given an integer, convert it to a roman numeral. Input is guaranteed to
be within the range from 1 to 3999.

Example 1:

Input: 3
Output: "III"

Example 2:

Input: 4
Output: "IV"

Example 3:

Input: 9
Output: "IX"

Example 4:

Input: 58
Output: "LVIII"
Explanation: C = 100, L = 50, XXX = 30 and III = 3.

Example 5:

Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
"""


class Solution:
    def get_roman_digit(self, digit, order):
        if not isinstance(order, int) or order < 0:
            raise ValueError('{} is not a valid order.'.format(order))
        if digit not in range(10):
            raise ValueError('{} is not a valid digit.'.format(digit))

        d = {
            0: ('I', 'V', 'X'),
            1: ('X', 'L', 'C'),
            2: ('C', 'D', 'M')
        }
        if order in d:
            one, five, ten = d[order]
            if digit == 9:
                return one + ten
            elif digit in [5, 6, 7, 8]:
                return five + one * (digit % 5)
            elif digit == 4:
                return one + five
            elif digit in [0, 1, 2, 3]:
                return one * (digit % 5)
            else:
                print(f'Something odd happened with digit = {digit}.')

        elif order > 2:
            return 'M' * (digit * 10**(order - 3))

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        li = list(str(num))
        li.reverse()
        out_li = []

        for order in range(len(li)):
            out_li.append(self.get_roman_digit(int(li[order]), order))

        out_li.reverse()
        return ''.join(out_li)


def main():
    """Summary
    """
    sol = Solution()
    test_cases = [3, 4, 9, 58, 1994]
    for case in test_cases:
        print('Input: {}\nOutput: {}\n------------'
              .format(case, sol.intToRoman(case)))


if __name__ == '__main__':
    main()

"""
https://leetcode.com/problems/unique-morse-code-words/description/

International Morse Code defines a standard encoding where each letter
is mapped to a series of dots and dashes, as follows: "a" maps to ".-",
"b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English
alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-.
.","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..
-","-.--","--.."]

Now, given a list of words, each word can be written as a concatenation
of the Morse code of each letter. For example, "cab" can be written as
"-.-.-....-", (which is the concatenation "-.-." + "-..." + ".-"). We'll
call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2

Explanation:
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".

Note:

* The length of words will be at most 100.
* Each words[i] will have length in range [1, 12].
* words[i] will only consist of lowercase letters.
"""

import string


class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        alph_morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
                      "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
                      "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
                      "-.--", "--.."]
        legend = dict(zip(list(string.ascii_lowercase), alph_morse))

        print(legend)

        words_morse = []
        for word in words:
            word_morse = ''
            for char in word:
                word_morse += legend[char]
            words_morse.append(word_morse)

        return len(list(set(words_morse)))


def main():
    """Summary
    """
    sol = Solution()
    test_cases = [["gin", "zen", "gig", "msg"]]
    for case in test_cases:
        print('Input: {}\nOutput: {}\n------------'
              .format(case, sol.uniqueMorseRepresentations(case)))


if __name__ == '__main__':
    main()

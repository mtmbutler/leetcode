# https://leetcode.com/problems/word-ladder-ii/description/


class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList or len(beginWord) != len(endWord):
            return []

        elif endWord == beginWord:
            return [[endWord]]

        tier_sort = [[beginWord]]
        while True:
            tier_sort.append([])
            for word_left in tier_sort[-2]:
                tier_sort[-1] += [word for word in wordList if
                                  one_letter_separates(word, word_left)]
            for word in tier_sort[-1]:
                if one_letter_separates(word, endWord):
                    return paths(tier_sort + [endWord])


def paths(tier_sort):
    ret = []
    tiers_rev = tier_sort[::-1]
    tiers_rev_pruned = [[tiers_rev[0]]]
    for word in tiers_rev_pruned[-1]:
        if one_letter_separates():
            assert False
    for i, tier in enumerate(tier_sort):
        tiers_rev_pruned.append([word for word in tier_sort[-1-i] if one_letter_separates(word, )])

    pass


def one_letter_separates(one, two):
    if one == two:
        return False
    diff_count = 0
    for i, char in enumerate(one):
        if diff_count > 1:
            return False
        if char != two[i]:
            diff_count += 1
    return True


def main():
    sol = Solution()
    test_cases = [
        ['hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']],
        ['hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']]
    ]
    for begin, end, words in test_cases:
        print(('Input: {}, {}, {}\n'
               'Output: {}\n------------').format(
                   begin, end, words, sol.findLadders(begin, end, words)))


if __name__ == '__main__':
    main()

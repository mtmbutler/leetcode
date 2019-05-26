"""
https://leetcode.com/problems/reconstruct-itinerary/

Given a list of airline tickets represented by pairs of departure and
arrival airports [from, to], reconstruct the itinerary in order. All of
the tickets belong to a man who departs from JFK. Thus, the itinerary
must begin with JFK.

Note:x

If there are multiple valid itineraries, you should return the itinerary
that has the smallest lexical order when read as a single string. For
example, the itinerary ["JFK", "LGA"] has a smaller lexical order than
["JFK", "LGB"].

All airports are represented by three capital letters (IATA code).

You may assume all tickets form at least one valid itinerary.

Example 1:
Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Example 2:
Input:
[["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is
["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical
order.
"""
from collections import defaultdict
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """Credit to Stefan Pochmann: https://leetcode.com/stefanpochmann

        https://leetcode.com/problems/reconstruct-itinerary/discuss/78768/Short-Ruby-Python-Java-C%2B%2B
        """
        targets = defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []

        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)

        visit('JFK')
        return route[::-1]


if __name__ == '__main__':
    sol = Solution()
    test_cases = (
        [[['MUC', 'LHR'],
          ['JFK', 'MUC'],
          ['SFO', 'SJC'],
          ['LHR', 'SFO']],
         ['JFK', 'MUC', 'LHR', 'SFO', 'SJC']],
        [[['JFK', 'SFO'],
          ['JFK', 'ATL'],
          ['SFO', 'ATL'],
          ['ATL', 'JFK'],
          ['ATL', 'SFO']],
         ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']],
        [[['JFK', 'KUL'],
          ['JFK', 'NRT'],
          ['NRT', 'JFK']],
         ['JFK', 'NRT', 'JFK', 'KUL']]
    )
    for arg, out in test_cases:
        result = sol.findItinerary(arg)
        print(arg, result, out)
        assert result == out

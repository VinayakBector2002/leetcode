'''

Input : List[List[int]]
    the array costs where costs[i] = [aCosti, bCosti]
Output: Int
    cost to fly every person to a city

A company is planning to interview 2n people. 
    Given the array costs where costs[i] = [aCosti, bCosti], 
    the cost of flying the ith person to city a is aCosti, 
    and the cost of flying the ith person to city b is bCosti.

Return the minimum cost to fly every person to a city such that exactly n people arrive in each city.

Doubt:
    - 2n <-> even number of ppl
    - can n be zero? no 
    - Can the cost be negative or zero? no


[10,10],[30,200],[400,50],[30,20]

- [10,10] A ,[30,20],[30,200] A ,[400,50] 40
- [10,10],[30,20] B ,[400,50] B,[30,200] 70

- [10,10],[30,20],[30,200]  ,[400,50]  40
- [10,10] B,[30,20]   ,[400,50] ,[30,200] 70
'''

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key = lambda x: x[0] - x[1])
        n = len(costs) // 2
        return sum([costs[x][0] for x in range(n)]) + sum([costs[x][1] for x in range(n, 2*n)])
        
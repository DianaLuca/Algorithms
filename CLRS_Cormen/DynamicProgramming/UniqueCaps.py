"""
There 100 different types of caps each having a unique id from 1 to 100. 
Also, there ‘n’ persons each having a collection of variable number of caps. 
One day all of these persons decide to go in a party wearing a cap but 
to look unique they decided that none them will wear the same type of cap. 
So, count the total number of arrangements or ways such that none of them is wearing same type of cap.

Constraints: 1 <= n <= 10 

source: GeeksforGeeks
"""


from collections import defaultdict

class AssignCap(object):

    def __init__(self):
        self.allmask = 0
        self.total_caps = 100
        self.caps = defaultdict(list)

    # Mask is the set of persons, i is the current cap number
    def countWaysUtil(self, dp, mask, cap_no):
        if mask == self.allmask:
            return 1

        # not everyone is wearing a cap and also there are no more caps to wear
        if cap_no > self.total_caps:
            return 0

        # if we already solved this problem return the result
        if dp[mask][cap_no] != -1:
            return dp[mask][cap_no]

        ways = self.countWaysUtil(dp, mask, cap_no + 1)

        if cap_no in self.caps:
            for ppl in self.caps[cap_no]:
                if mask & (1 << ppl):  # if person ppl is already wearing a cap
                    continue

                ways += self.countWaysUtil(dp, mask | (1 << ppl), cap_no + 1)
                ways = ways % (10**9 + 7)

        dp[mask][cap_no] = ways

        return dp[mask][cap_no]


    def countWays(self, N):
        for ppl in range(N):
            cap_possessed_by_person = map(int, input().strip().split())

            for i in cap_possessed_by_person:
                self.caps[i].append(ppl)

        self.allmask = (1 << N) - 1

        # Initialize all entries in dp as -1
        dp = [[-1 for j in range(self.total_caps + 1)] for i in range(2 ** N)]

        # Call recursive function countWaysUtil
        # result will be in dp[0][1]
        print(self.countWaysUtil(dp, 0, 1, ))

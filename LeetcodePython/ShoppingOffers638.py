"""In LeetCode Store, there are some kinds of items to sell. Each item has a price.
However, there are some special offers, and a special offer consists of 
one or more different kinds of items with a sale price.
You are given the each item's price, a set of special offers, and the number we need to buy for each item.'
The job is to output the lowest price you have to pay for exactly certain items as given, 
where you could make optimal use of the special offers.
Each special offer is represented in the form of an array, the last number represents the price you need to pay 
for this special offer, other numbers represents how many specific items you could get if you buy this offer.
You could use any of special offers as many times as you want.

Example 1:
Input: [2,5], [[3,0,5],[1,2,10]], [3,2]
Output: 14
Explanation: 
There are two kinds of items, A and B. Their prices are $2 and $5 respectively. 
In special offer 1, you can pay $5 for 3A and 0B
In special offer 2, you can pay $10 for 1A and 2B. 
You need to buy 3A and 2B, so you may pay $10 for 1A and 2B (special offer #2), and $4 for 2A.
"""


class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        d = {}

        def solve(tup):
            # print "solve: tup =", tup
            if tup in d:
                return d[tup]  # d[tup](aka total_price) = price*quantity
            d[tup] = sum(t * p for t, p in zip(tup, price))

            for sp in special:
                new_tup = tuple(t - s for t, s in zip(tup, sp))
                if min(new_tup) < 0: continue
                d[tup] = min(d[tup], solve(new_tup) + sp[-1])
            return d[tup]

        return solve(tuple(needs))

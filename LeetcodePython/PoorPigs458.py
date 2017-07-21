"""There are 1000 buckets, one and only one of them contains poison, the rest are filled with water. 
They all look the same. If a pig drinks that poison it will die within 15 minutes. 
What is the minimum amount of pigs you need to figure out which bucket contains the poison within one hour.

Answer this question, and write an algorithm for the follow-up general case.

Follow-up:

If there are n buckets and a pig drinking poison will die within m minutes, 
how many pigs (x) you need to figure out the "poison" bucket within p minutes? There is exact one bucket with poison.
"""


class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        # we need one pig / per dimension, looking by poisoned intersection
        pigs_aka_dimensions = 0
        rounds = minutesToTest // minutesToDie
        while (rounds + 1) ** pigs_aka_dimensions < buckets:
            pigs_aka_dimensions += 1
        return pigs_aka_dimensions
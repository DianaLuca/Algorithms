# In LLP world, there is a hero called Teemo and his attacking can make his enemy Ashe be in poisoned condition.
# Now, given the Teemo's attacking ascending time series towards Ashe and
# the poisoning time duration per Teemo's attacking,
# you need to output the total time that Ashe is in poisoned condition.
# You may assume that Teemo attacks at the very beginning of a specific time point,
# and makes Ashe be in poisoned condition immediately.


class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        res = 0
        time = -1
        for tim in timeSeries:
            if time >= tim:
                res -= time - tim + 1
            res += duration
            time = tim + duration - 1
        return res

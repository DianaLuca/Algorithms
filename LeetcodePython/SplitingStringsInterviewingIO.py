"""

"""
from collections import defaultdict, Counter

# linear
def splstr(S):
    d = Counter(S)
    nr_different = len(d)

    answer = 0
    pref = set()

    for s in S:
        pref.add(s)
        d[s] -= 1
        if len(pref) == nr_different and d[s] != 0:
            answer += 1
        elif not d[s]:
            return answer

    return answer



# O(N) = N**2
def splstrBruteForce(str):
    res = 0
    for i in range(len(str)):
        if set(str[:i]) == set(str[i:]):
            res += 1
    return res

print(splstr("abaab"), "2")
#print(splstr("noon"), "1\n", splstr("a"), "0\n", splstr("abc"), 0)
print (splstr("abcabc"))
print (splstr("abb"))

set("abx") ^ set("sdf")
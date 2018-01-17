from heapq import heappop, heappush, heapify

ls = [2 * _ for _ in range(5)] + [2 * _ + 1 for _ in range(5)]
print("given initial list:", ls)

# transform list ls into a heap: 2 methods
hp = []
for el in ls:
    heappush(hp, el)

heapify(ls)
print("new heapified list", ls)

print("heap list:", hp)
print(hp[0], hp[len(hp)-1])

print("heap list:", hp)

ordered = []
while hp:
    ordered.append(heappop(hp))

print(ordered)



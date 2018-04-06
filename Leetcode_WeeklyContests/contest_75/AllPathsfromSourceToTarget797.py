"""
Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  
graph[i] is a list of all nodes j for which the edge (i, j) exists.

Example:
Input: [[1,2], [3], [3], []] 
Output: [[0,1,3],[0,2,3]] 
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.

Note:

The number of nodes in the graph will be in the range [2, 15].
You can print different paths in any order, but you should keep the order of nodes inside one path.
"""


class Solution:
    def __init__(self, graph, target):
        self.graph = graph
        self.target = target
        self.res = []

    def all_paths_source_target(self, node, path):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        if node == self.target:
            self.res.append(path)
            return
        for v in sorted(self.graph[node]):
            if v not in path:
                self.all_paths_source_target(v, path + [v])


    def all_paths_source_target_iterative(self):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(graph) - 1
        source = 0
        stack = [(source, [source])]
        results = []
        path = [source]

        while stack:
            node, path = stack.pop()
            if node == n:
                results.append(path[:])
            for i in graph[node]:
                if i not in path:
                    stack.append((i, path + [i]))

        return results




#test
#graph = [[2,1,3], [4], [4], [4], []]

N = 6
graph = []
for i in range(N):
    graph.append([])
    for j in range(N):
        if i != j:
            graph[i].append(j)
    graph[i] = graph[i][::-1]

s = Solution(graph, N - 1)
s.all_paths_source_target(0, [0])
print("backtracking: ", s.res)
# print("dfs with stack: ", s.all_paths_source_target_iterative())

#s2 = Solution(graph, 3)
#print("dfs with stack: ", s2.all_paths_source_target_iterative())


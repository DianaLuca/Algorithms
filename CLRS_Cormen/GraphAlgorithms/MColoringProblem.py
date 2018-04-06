class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for col in range(vertices)] for line in range(vertices)]

    # Utility function to check if the current color assignment is safe for vertex v
    def isSafe(self, v, color, c):
        for i in range(self.V):
            if self.graph[v][i] == 1 and color[i] == c:
                return False
        return True

    def graphColor(self, m, colour, v):
        if v == self.V:
            return True

        for c in range(1, m+1):
            if self.isSafe(v, colour, c):
                colour[v] = c
                if self.graphColor(m, colour, v+1):
                    return True
                colour[v] = 0

    def graphColoring(self, m):
        colour = [0] * self.V
        if not self.graphColor(m, colour, 0):
            return False
            # Print the solution
        print("Following are the assigned colours:")
        for c in colour:
            print(c)
        return True

g = Graph(4)
g.graph = [[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]]
m = 3
print(g.graphColoring(m))



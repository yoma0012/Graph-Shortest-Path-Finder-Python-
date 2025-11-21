# Student Name: YOUR NAME
# Student Number: 9017169
# Course: PROG2349 - Lab 2
# Problem 2: Find Shortest Flight Route using BFS on an adjacency matrix

class Graph:
    def __init__(self, size):
        # Create adjacency matrix and list for city names
        self.adj_matrix = [[0] * size for _ in range(size)]
        self.vertex_data = [''] * size
        self.size = size

    def add_edge(self, u, v):
        # Add directed flight u -> v
        self.adj_matrix[u][v] = 1

    def add_vertex_data(self, vertex, data):
        # Store city name at a vertex
        self.vertex_data[vertex] = data

    def print_graph(self, space=3):
        # Print matrix with city names
        print("Adjacency Matrix:\n")
        header = " " * (space + 1) + " ".join(f"{d:>{space}}" for d in self.vertex_data)
        print(header)
        for i, row in enumerate(self.adj_matrix):
            row_str = " ".join(f"{x:>{space}}" for x in row)
            print(f"{self.vertex_data[i]:>{space}} {row_str}")

    def shortest_path(self, start_city, goal_city):
        # Convert names to indices
        try:
            start = self.vertex_data.index(start_city)
            goal = self.vertex_data.index(goal_city)
        except ValueError:
            return None

        # BFS storing full paths
        queue = [[start]]
        visited = [False] * self.size
        visited[start] = True

        while queue:
            path = queue.pop(0)
            current = path[-1]

            if current == goal:
                return [self.vertex_data[i] for i in path]

            # Check neighbors
            for i in range(self.size):
                if self.adj_matrix[current][i] == 1 and not visited[i]:
                    visited[i] = True
                    new_path = path + [i]
                    queue.append(new_path)

        return None


if __name__ == "__main__":
    g = Graph(6)

    g.add_vertex_data(0, 'Lagos')
    g.add_vertex_data(1, 'Accra')
    g.add_vertex_data(2, 'Nairobi')
    g.add_vertex_data(3, 'Cairo')
    g.add_vertex_data(4, 'Johannesburg')
    g.add_vertex_data(5, 'Addis Ababa')

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(2, 5)
    g.add_edge(5, 4)

    g.print_graph(8)

    print("\nShortest path from Lagos to Johannesburg:")
    print(g.shortest_path('Lagos', 'Johannesburg'))
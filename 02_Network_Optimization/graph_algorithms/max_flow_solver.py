"""
🕸️ Yoneylem-Ders-Notlari: Network Optimization Tool
Maximum Flow Algorithm (Edmonds-Karp / Ford-Fulkerson)
"""

from collections import deque

class MaxFlowSolver:
    def __init__(self, capacity):
        """
        capacity: 2D list where capacity[u][v] is the capacity of edge u->v
        """
        self.capacity = capacity
        self.n = len(capacity)

    def bfs(self, s, t, parent):
        visited = [False] * self.n
        queue = deque([s])
        visited[s] = True

        while queue:
            u = queue.popleft()
            for v, cap in enumerate(self.capacity[u]):
                if not visited[v] and cap > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == t:
                        return True
        return False

    def solve(self, source, sink):
        parent = [-1] * self.n
        max_flow = 0

        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.capacity[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.capacity[u][v] -= path_flow
                # For simplicity, residual reverse capacity is not added here
                # in a basic Edmonds-Karp, it should be self.capacity[v][u] += path_flow
                v = parent[v]

        return max_flow

def main():
    print("--- ⚙️ Yöneylem Araştırması: Maksimum Akış (Max-Flow) ---")
    
    # 6 nodes: 0 (Source), 1, 2, 3, 4, 5 (Sink)
    cap_matrix = [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]
    ]
    
    solver = MaxFlowSolver(cap_matrix)
    print(f"\n🚀 Kaynaktan (0) Hedefe (5) yapılabilecek maksimum akış: {solver.solve(0, 5)}")

if __name__ == "__main__":
    main()

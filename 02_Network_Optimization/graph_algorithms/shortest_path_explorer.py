"""
🕸️ Yoneylem-Ders-Notlari: Network Optimization Tool
Shortest Path Algorithm (Dijkstra)
"""

import heapq

class DijkstraExplorer:
    def __init__(self, graph):
        """
        graph: Dictionary where keys are nodes and values are lists of (neighbor, weight)
        """
        self.graph = graph

    def find_shortest_path(self, start_node, end_node):
        distances = {node: float('infinity') for node in self.graph}
        distances[start_node] = 0
        priority_queue = [(0, start_node)]
        previous_nodes = {node: None for node in self.graph}

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph.get(current_node, []):
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        # Reconstruct path
        path = []
        curr = end_node
        while curr is not None:
            path.append(curr)
            curr = previous_nodes[curr]
        path.reverse()

        return distances[end_node], path

def main():
    print("--- ⚙️ Yöneylem Araştırması: En Kısa Yol (Dijkstra) ---")
    
    # Example Graph (Nodes A-G)
    graph = {
        'A': [('B', 4), ('C', 3)],
        'B': [('D', 5), ('E', 10)],
        'C': [('E', 2), ('A', 3)],
        'D': [('F', 3)],
        'E': [('F', 5)],
        'F': [('G', 2)],
        'G': []
    }
    
    explorer = DijkstraExplorer(graph)
    dist, path = explorer.find_shortest_path('A', 'G')
    
    print(f"\n✅ Rotasyon Analizi Tamamlandı:")
    print(f"🔹 Başlangıç: A | Hedef: G")
    print(f"🔹 Toplam Minimum Mesafe/Maliyet: {dist}")
    print(f"🔹 İzlenen Yol: {' -> '.join(path)}")

if __name__ == "__main__":
    main()

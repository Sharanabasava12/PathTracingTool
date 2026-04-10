import networkx as nx

class PacketTracer:
    def __init__(self):
        self.graph = nx.Graph()

    def build_topology(self):
        self.graph.add_edges_from([
            ("h1", "s1"),
            ("s1", "s2"),
            ("s2", "s4"),
            ("s1", "s3"),
            ("s3", "s4"),
            ("s4", "h2")
        ])

    def find_path(self, src, dst):
        return nx.shortest_path(self.graph, src, dst)

if __name__ == "__main__":
    tracer = PacketTracer()
    tracer.build_topology()

    path = tracer.find_path("h1", "h2")

    print("\n  PACKET PATH TRACE ")
    print("Source      : h1")
    print("Destination : h2")
    print("Path        : " + " -> ".join(path))
    print("Hop Count   :", len(path)-1)

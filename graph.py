from hash_table import HashTable
from linked_list import LinkedList


class Edge:
    def __init__(self, to):
        self.to = to


class Graph:
    def __init__(self, directed=False):
        self.directed = directed
        self._vertices = HashTable()
        self._num_edges = 0

    def add_vertex(self, name):
        if not isinstance(name, str):
            raise TypeError
        
        if name == "":
            raise ValueError

        if self._vertices.contains(name):
            return False

        self._vertices.put(name, LinkedList())
        return True

    def add_edge(self, u, v):
        if not self._vertices.contains(u) or not self._vertices.contains(v):
            raise KeyError

        if u == v:
            raise ValueError

        edges_of_u = self._vertices.get(u)

        for edge in edges_of_u: # type: ignore
            if edge.to == v:
                return False

        edges_of_u.append(Edge(v)) # type: ignore

        if not self.directed:
            edges_of_v = self._vertices.get(v)
            edges_of_v.append(Edge(u)) # type: ignore
        self._num_edges += 1
        return True

    def remove_edge(self, u, v):
        if not self._vertices.contains(u) or not self._vertices.contains(v):
            raise KeyError

        edges_of_u = self._vertices.get(u)
        removed = False

        index = 0
        for edge in edges_of_u: # type: ignore
            if edge.to == v:
                edges_of_u.remove_at(index) # type: ignore
                removed = True
                break
            index += 1

        if not removed:
            return False
        
        if not self.directed:
            v_edges = self._vertices.get(v)
            index = 0
            for edge in v_edges: # type: ignore
                if edge.to == u:
                    v_edges.remove_at(index) # type: ignore
                    break
                index += 1

        self._num_edges -= 1
        return True

    def remove_vertex(self, name):
        if not self._vertices.contains(name):
            return False

        all_vertices = self.vertices() # type: ignore
        for vert in all_vertices:
            if vert != name and self._vertices.contains(vert):
                v_edges = self._vertices.get(vert)
                index = 0
                while index < len(v_edges): # type: ignore
                    edge = v_edges.get(index) # type: ignore
                    if edge.to == name:
                        v_edges.remove_at(index) # type: ignore
                        if self.directed:
                            self._num_edges -= 1
                    else:
                        index += 1

        self._num_edges -= len(self._vertices.get(name)) # type: ignore

        self._vertices.remove(name)
        return True

    def has_vertex(self, name):
        if self._vertices.contains(name):
            return True
        return False
            
    def has_edge(self, u, v):
        if not self._vertices.contains(u) or not self._vertices.contains(v):
            return False
        
        edges_of_u = self._vertices.get(u)
        for edge in edges_of_u: # type: ignore
            if edge.to == v:
                return True
        return False

    def neighbors(self, name):
        if not self._vertices.contains(name):
            raise KeyError

        edges_of_name = self._vertices.get(name)
        neighbors_list = []

        for edge in edges_of_name: # type: ignore
            neighbors_list.append(edge.to)

        return neighbors_list

    
    def degree(self, name):
        if not self._vertices.contains(name):
            raise KeyError

        edges_of_u = self._vertices.get(name)
        return len(edges_of_u) # type: ignore

    
    def vertices(self):
        return self._vertices.keys()

    def edges(self):
        edge_list = []
        all_vertices = self.vertices()

        for u in all_vertices:
            edges_of_u = self._vertices.get(u)
            for edge in edges_of_u: # type: ignore
                v = edge.to
                if self.directed:
                    edge_list.append((u, v))
                else:
                    if u < v:
                        edge_list.append((u, v))
        return edge_list

    def vertex_count(self):
        return len(self._vertices)

    def edge_count(self):
        return self._num_edges

    def __len__(self):
        return self.vertex_count()

    def __str__(self):
        lines = []
        for u in self.vertices():
            nbrs = self.neighbors(u)
            lines.append(f"{u} -> {', '.join(nbrs)}")
        return "\n".join(lines)
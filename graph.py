from hash_table import HashTable
from linked_list import LinkedList


class Edge:
    """An edge leading to a destination vertex.

    Attributes:
        to: The target vertex name.
    """

    def __init__(self, to):
        """Initializes a graph edge.

        Args:
            to: Target vertex name string.
        """
        self.to = to


class Graph:
    """An unweighted graph stored via adjacency lists.

    Attributes:
        directed: Flag checking whether graph is directed.
        _vertices: HashTable mapping vertex names to LinkedLists of Edges.
        _num_edges: Total number of active edges in the graph.
    """

    def __init__(self, directed=False):
        """Initializes a new Graph instance.

        Args:
            directed: Sets directed mode if True (defaults to False).
        """
        self.directed = directed
        self._vertices = HashTable()
        self._num_edges = 0

    def add_vertex(self, name):
        """Adds a new vertex to the graph.

        Args:
            name: Non-empty string identifier for the vertex.

        Returns:
            True if added successfully, False if vertex already exists.

        Raises:
            TypeError: If vertex name is not a string.
            ValueError: If vertex name is an empty string.
        """
        if not isinstance(name, str):
            raise TypeError

        if name == "":
            raise ValueError

        if self._vertices.contains(name):
            return False

        self._vertices.put(name, LinkedList())
        return True

    def add_edge(self, u, v):
        """Adds an edge connecting vertex u to vertex v.

        Args:
            u: Source vertex name.
            v: Destination vertex name.

        Returns:
            True if edge was added, False if duplicate.

        Raises:
            KeyError: If either vertex does not exist in the graph.
            ValueError: If trying to add a self-loop (u == v).
        """
        if not self._vertices.contains(u) or not self._vertices.contains(v):
            raise KeyError

        if u == v:
            raise ValueError

        edges_of_u = self._vertices.get(u)

        for edge in edges_of_u:
            if edge.to == v:
                return False

        edges_of_u.append(Edge(v))

        if not self.directed:
            edges_of_v = self._vertices.get(v)
            edges_of_v.append(Edge(u))
        self._num_edges += 1
        return True

    def remove_edge(self, u, v):
        """Removes an edge between vertex u and vertex v.

        Args:
            u: Source vertex name.
            v: Target vertex name.

        Returns:
            True if removed, False if edge didn't exist.

        Raises:
            KeyError: If either vertex isn't in the graph.
        """
        if not self._vertices.contains(u) or not self._vertices.contains(v):
            raise KeyError

        edges_of_u = self._vertices.get(u)
        removed = False

        index = 0
        for edge in edges_of_u:
            if edge.to == v:
                edges_of_u.remove_at(index)
                removed = True
                break
            index += 1

        if not removed:
            return False

        if not self.directed:
            v_edges = self._vertices.get(v)
            index = 0
            for edge in v_edges:
                if edge.to == u:
                    v_edges.remove_at(index)
                    break
                index += 1

        self._num_edges -= 1
        return True

    def remove_vertex(self, name):
        """Deletes a vertex and clears all incident edges.

        Args:
            name: Target vertex to remove.

        Returns:
            True if vertex was deleted, False if missing.
        """
        if not self._vertices.contains(name):
            return False

        all_vertices = self.vertices()
        for vert in all_vertices:
            if vert != name and self._vertices.contains(vert):
                v_edges = self._vertices.get(vert)
                index = 0
                while index < len(v_edges):
                    edge = v_edges.get(index)
                    if edge.to == name:
                        v_edges.remove_at(index)
                        if self.directed:
                            self._num_edges -= 1
                    else:
                        index += 1

        self._num_edges -= len(self._vertices.get(name))

        self._vertices.remove(name)
        return True

    def has_vertex(self, name):
        """Checks if a vertex exists in the graph.

        Args:
            name: Vertex name to query.

        Returns:
            True if present, False otherwise.
        """
        if self._vertices.contains(name):
            return True
        return False

    def has_edge(self, u, v):
        """Checks if an edge exists from u to v.

        Args:
            u: Source vertex.
            v: Destination vertex.

        Returns:
            True if edge exists, False otherwise.
        """
        if not self._vertices.contains(u) or not self._vertices.contains(v):
            return False

        edges_of_u = self._vertices.get(u)
        for edge in edges_of_u:
            if edge.to == v:
                return True
        return False

    def neighbors(self, name):
        """Gets all outgoing neighbor vertices for a given vertex.

        Args:
            name: Target vertex name.

        Returns:
            A list of neighbor vertex names.

        Raises:
            KeyError: If vertex doesn't exist.
        """
        if not self._vertices.contains(name):
            raise KeyError

        edges_of_name = self._vertices.get(name)
        neighbors_list = []

        for edge in edges_of_name:
            neighbors_list.append(edge.to)

        return neighbors_list

    def degree(self, name):
        """Gets the total number of outgoing edges for a vertex.

        Args:
            name: Target vertex name.

        Returns:
            Integer degree count.

        Raises:
            KeyError: If vertex is missing.
        """
        if not self._vertices.contains(name):
            raise KeyError

        edges_of_u = self._vertices.get(name)
        return len(edges_of_u)

    def vertices(self):
        """Gathers all vertex names present in the graph.

        Returns:
            A list of vertex name strings.
        """
        return self._vertices.keys()

    def edges(self):
        """Retrieves all edges in the graph as tuples.

        Returns:
            List of (u, v) edge pairs.
        """
        edge_list = []
        all_vertices = self.vertices()

        for u in all_vertices:
            edges_of_u = self._vertices.get(u)
            for edge in edges_of_u:
                v = edge.to
                if self.directed:
                    edge_list.append((u, v))
                else:
                    if u < v:
                        edge_list.append((u, v))
        return edge_list

    def vertex_count(self):
        """Returns total number of vertices in the graph."""
        return len(self._vertices)

    def edge_count(self):
        """Returns total edge count in the graph."""
        return self._num_edges

    def __len__(self):
        """Returns vertex count."""
        return self.vertex_count()

    def __str__(self):
        """Formats graph adjacency structure into a readable string."""
        lines = []
        for u in self.vertices():
            nbrs = self.neighbors(u)
            lines.append(f"{u} -> {', '.join(nbrs)}")
        return "\n".join(lines)
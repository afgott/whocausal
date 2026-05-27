import networkx as nx

class CausalGraph:
    """Class for building and validating DAGs"""
    
    def __init__(self):
        self.graph = nx.DiGraph()
        
    def add_edge(self, cause: str, effect: str):
        """Adds a directed edge from cause to effect, ensuring the graph remains acyclic"""
        self.graph.add_edge(cause, effect)
        self._validate_dag(cause, effect)
        
    def add_edges_from(self, edges: list):
        """Adds a list of edges in the format [('Cause', 'Effect'), ...]"""
        self.graph.add_edges_from(edges)
        
        # Validate the graph after mass addition
        if not nx.is_directed_acyclic_graph(self.graph):
            self.graph.remove_edges_from(edges) # Rollback changes
            raise ValueError("Error: Cycle detected")
            
    def _validate_dag(self, cause: str, effect: str):
        """Internal method for validating the acyclicity of the graph"""
        if not nx.is_directed_acyclic_graph(self.graph):
            self.graph.remove_edge(cause, effect) # Remove problematic edge
            raise ValueError(f"Adding edge {cause} -> {effect} creates a cycle")
            
    def get_nodes(self) -> list:
        return list(self.graph.nodes())
        
    def get_edges(self) -> list:
        return list(self.graph.edges())
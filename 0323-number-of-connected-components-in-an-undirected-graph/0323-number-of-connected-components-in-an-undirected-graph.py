class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        G = defaultdict(list)
        for node, adj in edges:
            G[node].append(adj)
            G[adj].append(node)

        visited = set()
        connected_components = 0
        def dfs(node):
            visited.add(node)
            for adj in G[node]:
                if adj not in visited:
                    dfs(adj)
            
        for node in range(n):
            if node not in visited:
                connected_components += 1
                dfs(node)
        return connected_components
            
                    
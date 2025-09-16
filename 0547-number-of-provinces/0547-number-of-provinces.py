from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        #visualize the graph G (turn the matrix into hashmap)
        G = defaultdict(list)
        n = len(isConnected)
        for curr_node in range (n):
            for adj in range (curr_node + 1, n):
                if isConnected[curr_node][adj]:
                    G[curr_node].append(adj)
                    G[adj].append(curr_node)

        #every node should count once (set visited)
        visited = set()
        #traverse nodes (use dfs) -> O
        def dfs(node):
            for number in G[node]:
                if number not in visited:
                    visited.add(number)
                    dfs(number)
        #count the number in visited
        ans = 0
        for i in range(n):
            if i not in visited:
                ans +=1
                dfs(i)
        return ans




        
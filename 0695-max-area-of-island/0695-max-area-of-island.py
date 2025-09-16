class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        G = defaultdict(list)
        lengthOfRow = len(grid)
        lengthOfCol = len(grid[0])

        for r in range(lengthOfRow):
            for c in range(lengthOfCol):
                if grid[r][c] == 1:
                    node = (r,c)
                    G[node]
                    for i, j in [(-1,0),(1,0),(0,-1),(0,1)]:
                        adj_row, adj_col = r + i, c + j
                        if 0<=adj_row<lengthOfRow and 0<=adj_col<lengthOfCol and grid[adj_row][adj_col] == 1:
                            G[node].append((adj_row,adj_col))
        visited = set()
        #count area of one land
        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)   # mark the current node
            area = 1
            for adj in G[node]:
                area += dfs(adj)
            return area


        #compare between lands
        biggest_area = 0
        for node in G:
            if node not in visited:
                land = dfs(node)
                biggest_area = max(biggest_area, land)
        return biggest_area
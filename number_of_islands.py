from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        island_count = 0

        def dfs(r: int, c: int):
            # Base Cases for stopping recursion:
            # Out of bounds OR the current cell is water ("0")
            if (r < 0 or r >= rows or
                    c < 0 or c >= cols or
                    grid[r][c] == "0"):
                return

            # "Sink" the island: mark current cell as "0" so we don't visit it again
            grid[r][c] = "0"

            # Recursively visit all 4 adjacent neighbors (Up, Down, Left, Right)
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        # Scan the entire grid
        for r in range(rows):
            for c in range(cols):
                # When we hit an unvisited piece of land, we found a new island!
                if grid[r][c] == "1":
                    island_count += 1
                    # Trigger DFS to completely clear/sink this specific island
                    dfs(r, c)

        return island_count


# --- TEST CODE ---
test_grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

validator = Solution()
total_islands = validator.numIslands(test_grid)

print(f"Total number of islands discovered: {total_islands}")
# Should output: 3
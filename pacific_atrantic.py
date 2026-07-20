from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])

        # Sets to keep track of which cells can reach each ocean
        pacific_reachable = set()
        atlantic_reachable = set()

        # Our DFS helper function to explore the continent (going uphill)
        def dfs(r: int, c: int, reachable_set: set, prev_height: int):
            # Base Cases to stop:
            # 1. Out of bounds
            # 2. Cell already visited and marked as reachable
            # 3. The current cell is lower than the previous one (water can't flow uphill in reverse check)
            if (r < 0 or r >= rows or
                    c < 0 or c >= cols or
                    (r, c) in reachable_set or
                    heights[r][c] < prev_height):
                return

            # Mark the current cell as reachable for this specific ocean
            reachable_set.add((r, c))

            # Walk to all 4 neighbors passing the current height as 'prev_height'
            dfs(r + 1, c, reachable_set, heights[r][c])  # Down
            dfs(r - 1, c, reachable_set, heights[r][c])  # Up
            dfs(r, c + 1, reachable_set, heights[r][c])  # Right
            dfs(r, c - 1, reachable_set, heights[r][c])  # Left

        # Step 1: Trigger DFS from the horizontal borders (Top and Bottom rows)
        for c in range(cols):
            # Top row touches Pacific (heights[0][c])
            dfs(0, c, pacific_reachable, heights[0][c])
            # Bottom row touches Atlantic (heights[rows-1][c])
            dfs(rows - 1, c, atlantic_reachable, heights[rows - 1][c])

        # Step 2: Trigger DFS from the vertical borders (Left and Right columns)
        for r in range(rows):
            # Left column touches Pacific (heights[r][0])
            dfs(r, 0, pacific_reachable, heights[r][0])
            # Right column touches Atlantic (heights[r][cols-1])
            dfs(r, cols - 1, atlantic_reachable, heights[r][cols - 1])

        # Step 3: Find the intersection (cells that are in BOTH sets)
        result = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pacific_reachable and (r, c) in atlantic_reachable:
                    result.append([r, c])

        return result


# --- TEST CODE ---
# A small island setup where the middle element '5' can flow everywhere
matrix = [
    [1, 2, 2],
    [3, 5, 3],
    [2, 4, 1]
]

validator = Solution()
coordinates = validator.pacificAtlantic(matrix)

print(f"Coordinates that can flow to both oceans:\n{coordinates}")
# Should output coordinates like [1, 1] (the middle point 5) among others
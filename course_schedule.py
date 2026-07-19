from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Map the prerequisites into an adjacency list (graph representation)
        # course -> list of its prerequisites
        pre_map = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            pre_map[course].append(pre)

        # A set to keep track of courses along the current DFS path (to detect cycles)
        visit_set = set()

        def dfs(course: int) -> bool:
            # If the course is already in our current path, we detected a cycle!
            if course in visit_set:
                return False
            # If the course has no prerequisites left, it's safe to take
            if pre_map[course] == []:
                return True

            # Add to current DFS path
            visit_set.add(course)

            # Recursively check all prerequisites for this course
            for pre in pre_map[course]:
                if not dfs(pre):
                    return False

            # Backtrack: remove from current path since we are done checking its branches
            visit_set.remove(course)

            # Optimization: Mark this course as completely safe by clearing its pre-list
            pre_map[course] = []
            return True

        # Since the graph might not be fully connected, we must run DFS for every single course
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True


# --- TEST CODE ---
validator = Solution()

# Example: 2 courses, circular dependency (0 -> 1 -> 0)
num_courses = 2
prereqs = [[1, 0], [0, 1]]

result = validator.canFinish(num_courses, prereqs)
print(f"Is it possible to finish all courses? {result}")
# Should output: False
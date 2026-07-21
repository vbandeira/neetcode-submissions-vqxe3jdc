class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Build graph with its dependencies
        graph = [ [] for _ in range(numCourses)]

        for dep, course in prerequisites:
            graph[course].append(dep)

        # Run DFS for each node and keep its 
        # dependencies in a cache (hashmap)

        def dfs(course):
            if course not in deps_map:
                for n in graph[course]:
                    deps_map[course] |= dfs(n)
                deps_map[course].add(course)
            return deps_map[course]

        deps_map = defaultdict(set)
        for course in range(numCourses):
            dfs(course)

        ans = []
        for u, v in queries:
            ans.append(u in deps_map[v])
        
        return ans
        
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Time: O(...) - Space: O(...)
        # TODO: Check Topological Sort alternative
        graph = [ [] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for dep, course in prerequisites:
            graph[dep].append(course)
            indegree[course] += 1
        
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        dep_map = defaultdict(set)

        while queue:
            course = queue.popleft()
            for n in graph[course]:
                dep_map[n].add(course)
                dep_map[n] |= dep_map[course]
                indegree[n] -= 1
                if indegree[n] == 0:
                    queue.append(n)

        ans = []
        for u, v in queries:
            ans.append(u in dep_map[v])

        return ans

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        in_degree = [0] * numCourses
        graph = [[] for _ in range(numCourses)]

        for course, dep in prerequisites:
            in_degree[course] += 1
            graph[dep].append(course)

        q = deque([i for i in range(numCourses) if in_degree[i] == 0])
        result = []

        while q:
            course = q.popleft()
            result.append(course)

            for dep in graph[course]:
                in_degree[dep] -= 1
                if in_degree[dep] == 0:
                    q.append(dep)
        
        return result if len(result) == numCourses else []
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses
        graph = [ [] for _ in range(numCourses)]

        for course, dep in prerequisites:
            in_degree[course] += 1
            graph[dep].append(course)

        q = deque([i for i in range(numCourses) if in_degree[i] == 0])

        counter = 0
        while q:
            course = q.popleft()
            counter += 1

            for c in graph[course]:
                in_degree[c] -= 1
                if in_degree[c] == 0:
                    q.append(c)
        
        return counter == numCourses
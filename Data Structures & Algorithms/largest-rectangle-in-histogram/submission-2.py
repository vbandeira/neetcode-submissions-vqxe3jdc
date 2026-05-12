class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Stack

        n = len(heights)
        stack = []

        # Busca barra utilizável mais a esquerda e salva em leftMost
        leftMost = [-1] * n
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftMost[i] = stack[-1]
            stack.append(i)
        
        # Repete processo acima buscando a barra mais a direita e salvando em rightMost
        stack = []
        rightMost = [n] * n
        for i in range(n -1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i)

        maxArea = 0
        # Itera sobre leftMost e rightMost, calcula a area e salva o resultado
        for i in range(n):
            # Corrige índices
            leftMost[i] += 1
            rightMost[i] -= 1
            area = heights[i] * (rightMost[i] - leftMost[i] + 1)
            maxArea = max(maxArea, area)
        
        return maxArea
"""
     DFS(Depth First Search : 깊이 우선 탐색)
     : 갈 수 있는 한 끝까지 탐색해 리프 노드를 방문하고, 이전 갈림길에서 선택하지 않았던 노드를 방문하는 식 탐색
     : Stack 사용(stack overflow 조심), 재귀함수로 구현 가능
     : back-tracking - 자식이 없으면 한단계 이전으로 돌아가 부모의 또 다른 자식을 찾음
     : 활용 예제 ) 자동미로 생성, 싸이클 탐지, 위상 정렬
"""

input = {
    'A': ['B'],
    'B': ['A', 'C', 'H'],
    'C': ['B', 'D'],
    'D': ['C', 'E', 'G'],
    'E': ['D', 'F'],
    'F': ['E'],
    'G': ['D'],
    'H': ['B', 'I', 'J', 'M'],
    'I': ['H'],
    'J': ['H', 'K'],
    'K': ['J', 'L'],
    'L': ['K'],
    'M': ['H']
}


def dfs(graph, start):
    visit = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    return visit


print(dfs(input, 'A'))

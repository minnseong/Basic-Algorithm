"""
    BFS(Breath First Search : 너비 우선 탐색)
     : 시작점인 루트 노드와 같은 거리에 있는 도르를 우선 방문
     : Queue 사용 -> append, pop(0) 구현가능하나 pop(0) 시간복잡도(O(N))가 매우 비효율적!
     : collections 라이브러리의 deque 이용하면 효율적임!
     : 재귀적으로 동작 x , 어떤 노드를 방문했었는지 여부를 반드시 검사
     : 활용 예제 ) 두 노드 사이의 최단 경로 or 임의의 경로를 찾고 싶을 때
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


# 1. append, pop(0)을 이용
def list_bfs(graph, root):
    visit = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])

    return visit


# 2. collections 라이브러리의 deque 사용
from collections import deque


def deque_bfs(graph, root):
    visit = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])

    return visit


print(list_bfs(input, 'A'))
print(deque_bfs(input, 'A'))

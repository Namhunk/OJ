import sys
sys.setrecursionlimit(400000)
from collections import defaultdict
def set_depth_subtree(n, prev) :
    sub_trees, depths = [], []
    for child in graph[n] :
        if child == prev : continue
        set_depth_subtree(child, n)
        sub_trees.append((sub_tree[child], child))
        depths.append((depth[child], child))
        depth[n] = max(depth[n], depth[child] + 1)
    sub_trees.sort(reverse=True)
    depths.sort(reverse=True)
    if len(sub_trees) >= 2 :
        if sub_trees[0][1] != depths[0][1] : sub_tree[n] = sub_trees[0][0] + depths[0][0] + 1
        else : sub_tree[n] = max(sub_trees[0][0] + depths[1][0] + 1, sub_trees[1][0]+depths[0][0] + 1)
    elif len(sub_trees) == 1 : sub_tree[n] = sub_trees[0][0] + 1



def DFS(n, prev, height) :
    global answer
    sub_trees, depths = [], []
    for child in graph[n] :
        if child == prev : continue
        sub_trees.append((sub_tree[child], child))
        depths.append((depth[child], child))
    sub_trees.sort(reverse=True)
    depths.sort(reverse=True)
    for child in graph[n] :
        if child == prev : continue
        next_height = height + 1
        if depths[0][1] != child :
            next_height = max(next_height, depths[0][0] + 2)
        elif len(depths) >= 2 and depths[0][1] == child :
            next_height = max(next_height, depths[1][0] + 2)
        DFS(child, n, next_height)
    if (len(sub_trees) >= 3) :
        answer = max(answer, 
                     sub_trees[0][0]+sub_trees[1][0]+height, 
                     sub_trees[0][0]+sub_trees[2][0]+depths[1][0]+1, 
                     sub_trees[0][0]+sub_trees[1][0]+depths[2][0]+1)
    elif (len(sub_trees) == 2) :
        answer = max(answer, sub_trees[0][0]+sub_trees[1][0]+height) 

def solution(t):
    global  answer, N, graph, sub_tree, depth
    N = len(t) + 1
    graph = defaultdict(list)
    sub_tree, depth = [1]*N, [1]*N
    answer = 0
    for v1, v2 in t:
        graph[v1].append(v2)
        graph[v2].append(v1)
    set_depth_subtree(0, -1)
    DFS(0, -1, 1)
    return answer
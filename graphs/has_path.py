# using dfs
def hasPathDFS(graph, src, dst):
    if (src == dst):
        return True
    
    for neighbour in graph[src]:
        if (hasPathDFS(graph, neighbour, dst) == True):
            return True
    
    return False

def hasPathBFS(graph, src, dst):
    queue = [src]

    while (len(queue) > 0):
        current = queue.pop(0)
        if current == dst:
            return True
        for neighbour in graph[current]:
            queue.append(neighbour)

    return False


graph = {
    "a": ['b', 'c'],
    "b": ['d'],
    "c": ['e'],
    "d": [],
    "e": [],
    "f": ['d']
}

result = hasPathDFS(graph, "a", "f")
print(result)

result = hasPathBFS(graph, "a", "f")
print(result)
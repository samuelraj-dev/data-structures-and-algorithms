def depthFirst(graph, source): 
    stack = [source]

    while (len(stack) > 0):
        current = stack.pop()
        print(current)
        for neighbour in graph[current]:
            stack.append(neighbour)
            
graph = {
    "a": ['b', 'c'],
    "b": ['d'],
    "c": ['e'],
    "d": ['f'],
    "e": [],
    "f": []
}

depthFirst(graph, "a")
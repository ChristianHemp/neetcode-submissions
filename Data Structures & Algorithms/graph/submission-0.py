class Graph:
    
    def __init__(self):
        self.adj_list = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj_list:
            self.adj_list[src] = []
        if dst not in self.adj_list:
            self.adj_list[dst] = []
        
        if dst not in self.adj_list[src]:
            self.adj_list[src].append(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj_list or dst not in self.adj_list:
            return False
        
        if dst in self.adj_list[src]:
            self.adj_list[src].remove(dst)
            return True
        
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        q = deque()
        visited = set()

        q.append(src)
        visited.add(src)

        while q:
            for _ in range(len(q)):
                curr = q.popleft()

                if curr == dst:
                    return True
                
                for neighbor in self.adj_list[curr]:
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)
        
        return False


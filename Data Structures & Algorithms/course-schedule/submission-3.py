class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {}

        for i in range(numCourses):
            prereqs[i] = []
        
        for crs1, crs2 in prerequisites:
            prereqs[crs1].append(crs2)
        
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            
            if prereqs[course] == []:
                return True
            
            visited.add(course)

            for neighbor in prereqs[course]:
                if not dfs(neighbor):
                    return False
            
            visited.remove(course)
            prereqs[course] = []

            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True


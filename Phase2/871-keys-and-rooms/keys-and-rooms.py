class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        visited = set()
        visited.add(0)
        queue = deque()
        queue.extend(rooms[0])
        while queue:
            for i in range(len(queue)):
                ind = queue.popleft()
                if ind not in visited:
                    visited.add(ind)
                    queue.extend(rooms[ind])

        if len(visited) == len(rooms):
            return True
        
        return False

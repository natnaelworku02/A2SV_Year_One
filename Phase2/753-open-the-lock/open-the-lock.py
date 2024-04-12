class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        lock = ["0","0","0","0"]

        queue = deque()
        visited = set()
        for deadend in deadends:
            visited.add(deadend)
        if ''.join(lock) not in visited:
            queue.append(lock)
            visited.add("".join(lock))
        count = 0

        while queue:
            for ind in range(len(queue)):
                lock = queue.popleft()

                if ''.join(lock) == target:
                    return count
                
                for i in range(4):

                    lock_copy = lock.copy()
                    lock_copy[i] = str((int(lock_copy[i]) + 1) % 10)
                    sttr = ''.join(lock_copy)

                    if sttr not in visited:
                        queue.append(lock_copy.copy())
                        visited.add(sttr)
                        
                    
                    lock_copy = lock.copy()
                    lock_copy[i] = str((int(lock_copy[i]) - 1) % 10)
                    sttr = ''.join(lock_copy)

                    if sttr not in visited:
                        queue.append(lock_copy.copy())
                        visited.add(sttr)
                    
            count += 1
        
        return -1

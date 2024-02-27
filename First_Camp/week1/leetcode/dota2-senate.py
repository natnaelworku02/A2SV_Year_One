class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque()
        d_count = 0
        r_count = 0
        counter = Counter(senate)
        for i in range(len(senate)):
            if d_count and senate[i] == 'D' :
                d_count -= 1 
                counter[senate[i]] -=1
                # print(i,"R")
                continue
            elif r_count and senate[i] == 'R':
                r_count -= 1
                counter[senate[i]] -=1
                # print(i,"D")
                continue
            if  senate[i] == 'D' and  counter['R']:
                # print(i)
                r_count += 1
                queue.append(senate[i])
            elif senate[i] == 'R' and  counter['D']:
                d_count += 1
                # print(i)

                queue.append(senate[i])
        if not counter['D']:
            return "Radiant"
        elif not counter['R']:
            return "Dire"
        while queue and counter['D'] and counter['R']:
            if d_count and queue[0] == 'D' :
                d_count -= 1 

                counter[queue[0]] -=1
                queue.popleft()
                # print("R",queue)
                continue
            elif r_count and queue[0] == 'R':
                r_count -= 1

                counter[queue[0]] -=1
                queue.popleft()
                # print("D", queue)
                continue
                # print(queue,counter['R'])

            if  queue[0] == 'D' and  counter['R']:
                r_count += 1
                val = queue.popleft()
                queue.append(val)
                # print(queue)
            elif queue[0] == 'R' and  counter['D']:
                d_count += 1

                val = queue.popleft()
                queue.append(val)
                # print(queue)
        if not counter['D']:
            return "Radiant"
        elif not counter['R']:
            return "Dire"
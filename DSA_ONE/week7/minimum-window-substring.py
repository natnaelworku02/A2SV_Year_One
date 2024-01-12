class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def check(new_dic, t_count):
            for key, val in t_count.items():
                if new_dic[key] < val:
                    return False
            return True

        t_count = Counter(t)
        s_count = defaultdict(int)
        ans = deque()
        res = ""
        length = float("inf")
        l, n = 0, len(s)
        for r in range(n):
            # print(ans)
            s_count[s[r]] += 1
            ans.append(s[r])
    
            while check(s_count, t_count):
                # print("HI")
                if length > len(ans):
                    res = "".join(ans)
                    length = len(ans)
                ans.popleft()
                s_count[s[l]] -= 1
                if s_count[s[l]] == 0:
                    s_count.pop(s[l])
                l += 1

        return res
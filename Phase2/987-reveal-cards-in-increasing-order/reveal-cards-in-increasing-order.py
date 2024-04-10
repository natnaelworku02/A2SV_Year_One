class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        ans = deque()
        while deck:
            val = deck.pop()
            if ans:
                ans.appendleft(ans.pop())
            ans.appendleft(val)
        return ans
            
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse =True)
        ans_deq = deque()
        for card in deck:
            if not ans_deq:
                ans_deq.append(card)
            else:
                val = ans_deq.pop()
                ans_deq.appendleft(val)
                ans_deq.appendleft(card)
        return list(ans_deq)




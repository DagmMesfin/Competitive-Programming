class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        senatequeue = deque(senate)
        counter = Counter(senate)
        banD,banR = 0,0

        while counter["R"] and counter["D"]:
            val = senatequeue.popleft()
            if val == "R":
                if banR == 0:
                    senatequeue.append(val)
                    banD+=1
                else:
                    banR-=1
                    counter["R"]-=1
            elif val == "D":
                if banD == 0:
                    senatequeue.append(val)
                    banR+=1
                else:
                    banD-=1
                    counter["D"]-=1

        lastman = senatequeue.pop()

        return "Radiant" if lastman == "R" else "Dire"
                

        
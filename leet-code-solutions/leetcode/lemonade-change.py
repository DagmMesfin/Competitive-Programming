class Solution:
    def lemonadeChange(self, a: List[int]) -> bool:
        notes = defaultdict(int)

        for note in a:
            if note == 5:
                notes[note]+=1
            elif note == 10:
                if notes[5] <= 0:
                    return False
                notes[5]-=1
                notes[10]+=1
            elif note == 20:
                if notes[5] <= 0:
                    return False
                if notes[10] <= 0:
                    if notes[5] > 2:
                        notes[5]-=3
                    else:
                        return False
                else:
                    notes[10]-=1
                    notes[5]-=1
                    
                notes[20]+=1

        return True

                    

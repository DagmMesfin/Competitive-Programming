class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        maxo = max(costs)
        counter = 0
        sum = 0
        dicto = {i:0 for i in range(1,maxo+1)}

        for i in range(len(costs)):
            dicto[costs[i]] += 1

        for price,count in dicto.items():
            if coins-(price*count)>0:
                counter+=count
                coins-=price*count
            else:
                for i in range(count):
                    coins-=price
                    if coins < 0:
                        break
                    counter+=1
            if coins <= 0:
                break
                
        return counter
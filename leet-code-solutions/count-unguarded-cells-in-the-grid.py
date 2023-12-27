class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guards = set((x,y) for x,y in guards)
        walls = set((x,y) for x,y in walls)
        matrix = []
        count = 0
        for i in range(m):
            listo = []
            for j in range(n):
                if (i,j) in guards:
                    listo.append("G")
                elif (i,j) in walls:
                    listo.append("W")
                else:
                    count+=1
                    listo.append("A")
            matrix.append(listo)

        seen = set()
        for guard in guards:
            r = int(guard[0])
            c = int(guard[1])


            for north in range(r-1,-1,-1):
                if matrix[north][c] == "W":
                    break
                if matrix[north][c] == "G":
                    break
                if (north,c) not in seen:
                    matrix[north][c] = "S"
                    count-=1
                    seen.add((north,c))
                else:
                    continue

            for south in range(r+1,m):
                if matrix[south][c] == "W":
                    break
                if matrix[south][c] == "G":
                    break
                if (south,c) not in seen:
                    matrix[south][c] = "S"
                    count-=1
                    seen.add((south,c))
                else:
                    continue

            for east in range(c+1,n):
                if matrix[r][east] == "W":
                    break
                if matrix[r][east] == "G":
                    break
                if (r,east) not in seen:
                    matrix[r][east] = "S"
                    count-=1
                    seen.add((r,east))
                else:
                    continue

            for west in range(c-1,-1, -1):
                if matrix[r][west] == "W":
                    break
                if matrix[r][west] == "G":
                    break
                if (r,west) not in seen:
                    matrix[r][west] = "S"
                    count-=1
                    seen.add((r,west))
                else:
                    continue

        return count
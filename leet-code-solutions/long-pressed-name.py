class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        m = 0
        name_len = len(name)
        typed_len = len(typed)

        for n in range(typed_len):
            if m < name_len and name[m] == typed[n]:
                m+=1
            elif n == 0 or typed[n] != typed[n-1]:
                return False

        return m == name_len

            
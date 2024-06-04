class Solution:
    def simplifyPath(self, path: str) -> str:
        pathstack = path.split("/")
        endstack = []

        for item in pathstack:
            if not item or item == ".":
                continue
            if item == "..":
                if endstack:
                    endstack.pop()
            else:
                endstack.append(item)


        return "/" + "/".join(endstack)
        
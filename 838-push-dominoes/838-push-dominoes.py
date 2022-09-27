class Solution:
    def pushDominoes(self, domi: str) -> str:
        n = len(domi)
        domi = list(domi)
        flag = True
        while flag:
            flag = False
            temp = domi[::]
            for i in range(n):
                if domi[i] == "L":
                    if i == 0:
                        continue
                    elif i == 1 and domi[i-1] == ".":
                        flag = True
                        temp[i-1] = 'L'
                    elif i>1 and domi[i-1] == '.' and domi[i-2]!="R":
                        flag = True
                        temp[i-1] = "L"
                if domi[i] == "R":
                    if i == n-1:
                        continue
                    elif i == n-2 and domi[i+1] == ".":
                        flag = True
                        temp[i+1] = 'R'
                    elif i<n-2 and domi[i+1] == '.' and domi[i+2]!="L":
                        flag = True
                        temp[i+1] = "R"
            domi = temp
        domi = "".join(domi)
        return domi
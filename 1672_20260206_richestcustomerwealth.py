from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        #w = 0
        #new_arr = accounts[0]
        #for i in range(1, len(accounts))
            #for j in range(1, len(accounts[0]))
                #w=accounts[j]+w
            #new_arr[i] = w
        new_arr = [0] * len(accounts)
        for i in range(0,len(accounts)):
            w = 0
            #print(accounts[i])
            for j in range(0,len(accounts[i])):
                w = accounts[i][j] + w
                #print(accounts[i][j], w)
            new_arr[i] = w
            #print(new_arr)
        return max(new_arr)

print(Solution().maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))

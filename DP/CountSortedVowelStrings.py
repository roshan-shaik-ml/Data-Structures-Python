class Solution:
    
    def countVowelStrings(self, n):

        strings = [[0 for col in range(6)] for row in range(n+1)]

        
        for stringLength in range(1, n+1):
            
            for index in range(1, 6):
                
                if stringLength == 1:

                    strings[stringLength][index] = strings[stringLength][index-1] + 1
                else:
                    strings[stringLength][index] = strings[stringLength-1][index] + strings[stringLength][index-1]
                print(strings)
        return strings[n][5]

if __name__ == "__main__":

    sol = Solution()
    val = sol.countVowelStrings(2)
    print(val)
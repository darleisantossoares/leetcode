class Solution:
    def numDecodings(self, s: str) -> int:

        @cache
        def ways(s, i=0):
            if i == len(s):
                return 1
            elif s[i] == "0":
                return 0
            elif i+1 < len(s) and "10" <= s[i] + s[i+1] <= "26":
                return ways(s,i+1) + ways(s,i+2)
            else:
                return ways(s, i+1)

        return ways(s,0)

###
#        |1 :if i = |s|
#        |0 :if s[i] = "0"
# ways(i)|
#        |ways(i+1)+ways(i+2) :if i + 1 < |s| and "10" <= s[i] + s[i+1] <= "26"
#        |ways(i+1) :otherwise
###

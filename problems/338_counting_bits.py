class Solution:
    def countBits(self, n: int) -> List[int]:

        answer = list()

        for n in range(0, n+1):
            binary_representation= str(bin(n)[2:])
            answer.append( len( str( binary_representation ).replace('0','') ) )

        return answer

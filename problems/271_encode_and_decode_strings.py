class Codec:
    def encode(self, strs: List[str]) -> str:
        return 'ç'.join(strs)
    def decode(self, s:str) -> List[str]:
        return s.split('ç')

## Solution 2

class Codec2:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return ''.join('%d:' % len(s) + s for s in strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        strs = []
        i = 0
        while i < len(s):
            j = s.find(':', i)
            i = j + 1 + int(s[i:j])
            strs.append(s[j+1:i])
        return strs

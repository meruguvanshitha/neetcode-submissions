class Solution:
    def encode(self, strs: List[str]) -> str:
        # Encode as length + # + word for every string
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            # Find the # separator
            j = s.find('#', i)
            # Read the string length
            length = int(s[i:j])
            # Extract string and jump to the next item
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res
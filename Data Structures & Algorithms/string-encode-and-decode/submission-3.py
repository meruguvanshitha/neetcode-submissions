class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        while s:
            length, s = s.split("#", 1)  # Split at the first '#' only
            length = int(length)
            res.append(s[:length])      # Take the exact word length
            s = s[length:]              # Slice off the processed word
        return res
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        table = [".-", "-...", "-.-.", "-..", ".", "..-.", \
                "--.", "....", "..", ".---", "-.-", ".-..", \
                "--", "-.", "---", ".--.", "--.-", ".-.", \
                "...", "-", "..-", "...-", ".--", "-..-", \
                "-.--", "--.."]
        transforms = set()
        for w in words:
            curr = []
            for c in w:
                curr.append(table[ord(c)-97])
            transforms.add("".join(curr))
        return len(transforms)

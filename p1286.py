class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.combos = []
        characters = list(characters)
        
        def generateCombos(curr, chars, start):
            if len(curr) == combinationLength:
                self.combos.append(''.join(curr))
                return
            for i in range(start, len(chars)):
                c = chars.pop(i)
                curr.append(c)
                generateCombos(curr, chars, i)
                curr.pop(-1)
                chars.insert(i, c)
        
        generateCombos([], characters, 0)
        
    def next(self) -> str:
        return self.combos.pop(0)

    def hasNext(self) -> bool:
        return not not self.combos
class Solution:
    def toGoatLatin(self, S: str) -> str:
        arr = S.split()

        for i, s in enumerate(arr):
            first_letter = s[0].lower()
            if first_letter not in {'a', 'e', 'i', 'o', 'u'}:
                arr[i] = s[1:] + s[0]
            arr[i] += 'ma'
            arr[i] += 'a'*(i+1)

        return ' '.join(arr)

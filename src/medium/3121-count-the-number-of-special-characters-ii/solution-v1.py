class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = set()
        upper = set()
        impossible = set()

        out = 0

        for i in range(0, len(word)):
            if word[i].islower():
                if word[i].upper() in upper and not (word[i] in impossible) and word[i] in lower:
                    out -= 1
                    impossible.add(word[i])
                elif not (word[i].upper() in upper):
                    lower.add(word[i])

            elif word[i].isupper():
                if word[i].lower() in lower and not (word[i] in upper):
                    upper.add(word[i])
                    out += 1
                elif not (word[i].lower() in lower):
                    upper.add(word[i])

        if out < 0:
            return 0
        return out
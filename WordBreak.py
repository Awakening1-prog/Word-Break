class Solution:
    def solve(self, words, s):
        q = [0]
        visited = [0]
        while q:
            curr = q.pop(0)
            if curr == len(s):
                return True
            for word in words:
                if (
                    curr + len(word) not in visited
                    and curr + len(word) <= len(s)
                    and s[curr : curr + len(word)] == word
                ):
                    q.append(curr + len(word))
                    visited.append(curr + len(word))
        return False

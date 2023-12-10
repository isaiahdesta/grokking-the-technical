class Solution:
    def findPrimePairs(self, n):
        pairs = []

        if n < 3:
            return []
        sieve = [True] * (n+1)
        sieve[0], sieve[1] = False, False
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i*i, n+1, i):
                    sieve[j] = False
        for x in range(1, n // 2 + 1):
            if sieve[x] and sieve[n - x]:
                pairs.append([x, n - x])
        return pairs

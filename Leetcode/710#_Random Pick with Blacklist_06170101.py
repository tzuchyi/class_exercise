import random
import bisect


class Solution:
    def __init__(self, N, blacklist):
        self.N = N - 1
        self.black = sorted(blacklist)
        self.range = []
        self.weight = []
        self.blacklen = len(self.black)
        if self.blacklen:
            s = 0
            for r in self.black:
                if r - s >= 1:
                    self.range.append([s, r - 1])
                s = r + 1
            if s < self.N + 1:
                self.range.append([s, self.N])

            weight = 0
            for r in self.range:
                weight = weight + r[1] - r[0] + 1
                self.weight.append(weight)

    def pick(self) -> int:
        if self.blacklen:
            r = self.range[bisect.bisect_left(
                self.weight, random.randint(1, self.weight[-1]))]
            return random.randint(r[0], r[1]) if r[1] > r[0] else r[0]

        else:
            return random.randint(0, self.N)

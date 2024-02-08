class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        dc = defaultdict(int)
        for match in matches:
            for element in match:
                dc[element] = 0
        for match in matches:
            dc[match[1]] += 1

        sorted_dc = dict(sorted(dc.items(), key=lambda item: item[1]))

        zero = []
        one = []
        for key, value in sorted_dc.items():
            if value == 0:
                zero.append(key)
            elif value == 1:
                one.append(key)
        return [sorted(zero),sorted(one)]
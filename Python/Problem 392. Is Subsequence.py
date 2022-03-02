class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        places = defaultdict(list)
        for i, symbol in enumerate(t):
            places[symbol].append(i)
        
        current_place = 0
        for symbol in s:
            current_ind = bisect.bisect_left(places[symbol], current_place)
            if current_ind >= len(places[symbol]):
                return False
            current_place = places[symbol][current_ind] + 1
            
        return True
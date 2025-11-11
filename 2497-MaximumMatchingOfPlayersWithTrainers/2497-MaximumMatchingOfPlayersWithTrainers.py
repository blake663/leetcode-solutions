# Last updated: 11/10/2025, 8:01:04 PM
class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        res = 0

        t, p = 0, 0
        while t < len(trainers) and p < len(players):
            if players[p] <= trainers[t]:
                res += 1
                p += 1
                t += 1
            else:
                t += 1
        
        return res
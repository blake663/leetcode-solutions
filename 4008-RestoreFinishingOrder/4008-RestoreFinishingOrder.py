# Last updated: 11/10/2025, 7:59:32 PM
class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        n = len(order)
        position_of = {}

        for pos, id in enumerate(order):
            position_of[id] = pos

        friends.sort(key=lambda id: position_of[id])
        return friends
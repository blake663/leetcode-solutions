# Last updated: 11/10/2025, 8:01:06 PM
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.sl = defaultdict(SortedList) # (-rating, food)
        self.cuisine_of = {}
        self.rating_of = {}

        for i in range(len(foods)):
            self.sl[cuisines[i]].add((-ratings[i], foods[i]))
            self.cuisine_of[foods[i]] = cuisines[i]
            self.rating_of[foods[i]] = ratings[i]

    def changeRating(self, food: str, newRating: int) -> None:
        if self.rating_of[food] == newRating: return
        cuisine = self.cuisine_of[food]
        sl = self.sl[cuisine]

        sl.remove((-self.rating_of[food], food))
        self.rating_of[food] = newRating
        sl.add((-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        return self.sl[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)

# heap: [(mcdouble: 9), (fish fillet: 6), (fish fillet: 5), (fish fillet: 6), (fish fillet: 5)], deleted: {(fish fillet, 6): 2, (fish fillet, 5): 1}
# approach 1: heaps with lazy deletion
# time: O(m log(m+n)), space: O(m + n)


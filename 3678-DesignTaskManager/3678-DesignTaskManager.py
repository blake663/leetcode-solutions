# Last updated: 11/10/2025, 8:00:28 PM
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        # (userId, taskId, priority) []
        self.sd = SortedDict() # (priority, taskId)
        self.task_to_priority = {}
        
        for userId, taskId, priority in tasks:
            self.sd[(priority, taskId)] = userId
            self.task_to_priority[taskId] = priority

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.sd[(priority, taskId)] = userId
        self.task_to_priority[taskId] = priority

    def edit(self, taskId: int, newPriority: int) -> None:
        priority = self.task_to_priority[taskId]
        self.task_to_priority[taskId] = newPriority
        userId = self.sd.pop((priority, taskId))
        self.sd[(newPriority, taskId)] = userId

    def rmv(self, taskId: int) -> None:
        priority = self.task_to_priority[taskId]
        del self.sd[(priority, taskId)]

    def execTop(self) -> int:
        return self.sd.popitem()[1] if self.sd else -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()

# time:
#   init => O(T log(T)), 
#   calls => O(C log(T+C))
# space: O(T)
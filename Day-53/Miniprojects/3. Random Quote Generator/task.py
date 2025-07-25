class Task:
    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed
        }

# Sample task list
task_list = [
    Task(1, "Fix CORS issues").to_dict(),
    Task(2, "Implement DELETE endpoint").to_dict(),
    Task(3, "Test with Thunder Client").to_dict()
]

def get_task_by_id(task_id):
    return next((t for t in task_list if t["id"] == task_id), None)
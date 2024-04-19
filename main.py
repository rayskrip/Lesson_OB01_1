class Task():
    tasks = []

    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.done_status = False
        Task.tasks.append(self)

    def add_task(description, deadline):
        Task(description, deadline)
        print(f"Задача '{description}' добавлена.")

    def mark_task_as_done(description):
        for task in Task.tasks:
            if task.description == description:
                if not task.done_status:
                    task.done_status = True
                    print(f"Задача '{description}' отмечена как выполнена.")
                    return
                else:
                    print(f"Задача '{description}' уже выполнена.")
                    return
        print(f"Задача '{description}' не найдена.")

        def show_current_tasks():
        current_tasks = [task for task in Task.tasks if not task.done_status]
        if current_tasks:
            print("Текущие задачи:")
            for task in current_tasks:
                print(
                    f"Описание: {task.description}, Срок: {task.deadline}, Статус: {'Выполнено' if task.done_status else 'Не выполнено'}")
        else:
            print("Нет текущих задач.")

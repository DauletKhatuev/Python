from django.db import models


class Category(models.Model):
    """Категория выполнения задачи"""
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    """Основная ззадача."""

    class Status(models.TextChoices):
        NEW = "NEW", "New"
        IN_PROGRESS = "IN_PROGRESS", "In progress"
        PENDING = "PENDING", "Pending"
        BLOCKED = "BLOCKED", "Blocked"
        DONE = "DONE", "Done"

    title = models.CharField(
        max_length=200,
        unique_for_date="deadline", #уникально для конкретной даты дедлайна
        help_text="Название задачи (уникально для  даты дедлайна)",
    )
    description = models.TextField(blank=True)

    #многие-ко-многим к Category
    categories = models.ManyToManyField(
        Category,
        related_name="tasks",
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
    )

    deadline = models.DateTimeField(
        auto_now_add=True,
        help_text="Дата и время создания",
    )

    def __str__(self) -> str:
        return f"{self.title} ({self.get_status_display()})"


class SubTask(models.Model):
    """Подзадача, связанная с основной задачей."""

    class Status(models.TextChoices):
        NEW = "NEW", "New"
        IN_PROGRESS = "IN_PROGRESS", "In progress"
        PENDING = "PENDING", "Pending"
        BLOCKED = "BLOCKED", "Blocked"
        DONE = "DONE", "Done"

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)

    # связь "один Task -> много SubTask"
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="substasks",
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
    )

    deadline = models.DateTimeField(
        auto_now_add=True,
        help_text="Дата и время создания подзадачи",
    )

    def __str__(self) -> str:
        return f"{self.title} -> {self.task.title}"

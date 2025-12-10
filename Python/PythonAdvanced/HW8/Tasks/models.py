from django.db import models


class Category(models.Model):
    """Категория выполнения задачи (дом, работа, учеба и т.п.)."""
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        db_table = "task_manager_category"
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        constraints = [
            models.UniqueConstraint(
                fields=["name"],
                name="unique_category_name",
            )
        ]

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    """Основная задача."""

    class Status(models.TextChoices):
        NEW = "NEW", "New"
        IN_PROGRESS = "IN_PROGRESS", "In progress"
        PENDING = "PENDING", "Pending"
        BLOCKED = "BLOCKED", "Blocked"
        DONE = "DONE", "Done"

    title = models.CharField(
        max_length=200,
        unique=True,  # уникальность по title
        help_text="Название задачи (уникально)",
    )
    description = models.TextField(blank=True)

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
        help_text="Дата и время дедлайна",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Дата и время создания",
    )

    class Meta:
        db_table = "task_manager_task"
        ordering = ["-created_at"]        # сортировка по убыванию даты создания
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
        constraints = [
            models.UniqueConstraint(
                fields=["title"],
                name="unique_task_title",
            )
        ]

    def __str__(self) -> str:
        return self.title


class SubTask(models.Model):
    """Подзадача, связанная с основной задачей."""

    class Status(models.TextChoices):
        NEW = "NEW", "New"
        IN_PROGRESS = "IN_PROGRESS", "In progress"
        PENDING = "PENDING", "Pending"
        BLOCKED = "BLOCKED", "Blocked"
        DONE = "DONE", "Done"

    title = models.CharField(
        max_length=200,
        unique=True,  # уникальность по title
    )
    description = models.TextField(blank=True)

    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name="subtasks",
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
    )

    deadline = models.DateTimeField(
        help_text="Дата и время дедлайна подзадачи",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Дата и время создания подзадачи",
    )

    class Meta:
        db_table = "task_manager_subtask"
        ordering = ["-created_at"]       # сортировка по убыванию даты создания
        verbose_name = "SubTask"
        verbose_name_plural = "SubTasks"
        constraints = [
            models.UniqueConstraint(
                fields=["title"],
                name="unique_subtask_title",
            )
        ]

    def __str__(self) -> str:
        return self.title

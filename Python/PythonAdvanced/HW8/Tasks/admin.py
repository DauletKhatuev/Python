from django.contrib import admin
from  .models import Task, SubTask, Category

class SubTaskInline(admin.TabularInline):
    model = SubTask
    extra = 1

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "deadline", "created_at")
    list_filter = ("status", "deadline",  "created_at", "categories")
    search_fields = ("title", "description")
    date_hierarchy = "deadline"
    filter_horizontal = ("categories",)
    inlines = [SubTaskInline]

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ("title", "task", "status", "deadline", "created_at")
    list_filter = ("status", "deadline", "created_at", "task")
    search_fields = ("title", "description")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
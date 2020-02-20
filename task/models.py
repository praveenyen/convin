from django.db import models


class Task(models.Model):
    task_type = models.IntegerField()
    task_desc = models.CharField(max_length=140)

    def __str__(self):
        return '{} - {}'.format(self.task_type, self.task_desc)


class TaskTracker(models.Model):
    TASK_UPDATE_TYPES = [
        ('Monthly', 'Monthly'),
        ('Weekly', 'Weekly'),
        ('Daily', 'Daily'),
    ]
    task_type = models.ForeignKey(Task, on_delete=models.DO_NOTHING)
    update_type = models.CharField(max_length=10, choices=TASK_UPDATE_TYPES)
    email = models.EmailField()

    def __str__(self):
        return '{} - {}'.format(self.task_type, self.update_type)
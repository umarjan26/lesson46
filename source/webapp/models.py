from django.db import models


from django.db import models

# Create your models here.
STATUS_CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]


class Task(models.Model):
    task = models.CharField(max_length=50, null=False, blank=False, verbose_name="Задача")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name="Статус", default=STATUS_CHOICES[0][0])
    description = models.CharField(max_length=3000, null=False, blank=False, verbose_name="описание")
    created_at = models.DateField(default="",  verbose_name="Дата")

    def __str__(self):
        return f"{self.id}. {self.task}: {self.status}: {self.description}"

    class Meta:
        db_table = "Tasks"
        verbose_name = "task"
        verbose_name_plural = "tasks"


from django.db import models


class Task(models.Model):
    title = models.CharField("Название", max_length=50)
    task = models.TextField("Описание")
    task_date = models.DateTimeField(auto_now=True, verbose_name="Дата создания")
    is_complete = models.BooleanField('Задание закончено', default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"


class Comment(models.Model):
    # task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# Create your models here.

#   task = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)

# name = models.ForeignKey(Task, related_name='comments', on_delete=models.CASCADE)

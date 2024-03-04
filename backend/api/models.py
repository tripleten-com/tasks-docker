from django.db import models


class Task(models.Model):
    title = models.CharField(verbose_name='Title', max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title

from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Kategóriák"

    def __str__(self):
        return self.title


from django.db import models


class Note(models.Model):
    Title = models.CharField(max_length=500)
    Body = models.TextField()

    def __str__(self):
        return self.Title


# Create your models here.

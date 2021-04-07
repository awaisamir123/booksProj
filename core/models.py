from django.db import models

class Book(models.Model):
    author = models.CharField("Author", max_length=255)
    title = models.CharField("Title", max_length=255)
    description = models.CharField("Description", max_length=255)
    poster_image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title
from django.db import models
from django.utils import timezone


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.name}'


class Author(models.Model):
    fullname = models.CharField(max_length=255, null=False, unique=True)
    born_date = models.DateField(null=True)
    born_location = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.fullname}'


class Quote(models.Model):
    tags = models.ManyToManyField(Tag, related_name="tags")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    quote = models.TextField(null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quote}'

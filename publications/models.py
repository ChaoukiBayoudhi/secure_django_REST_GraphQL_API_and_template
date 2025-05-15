from django.db import models

class Publication(models.Model):
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    pub_date = models.DateTimeField('date published')
    authors = models.ManyToManyField('Author', related_name='publications')
    summary = models.TextField()
    def __str__(self):
        return f'title = {self.title}, pub_date = {self.pub_date}'

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    affeliation = models.CharField(max_length=200)
    orcId = models.CharField(max_length=200)
    def __str__(self):
        return self.name

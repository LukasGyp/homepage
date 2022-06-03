from django.db import models

# Create your models here.
class Profile(models.Model):
  name = models.CharField(max_length=20)
  age = models.IntegerField()


class BlogTag(models.Model):
  name = models.CharField(max_length=15)

  def __str__(self):
    return self.name


class BlogPost(models.Model):
  title = models.CharField(max_length=30)
  created = models.DateField(help_text='作成日')
  tags = models.ManyToManyField(BlogTag, blank=True)
  content = models.TextField()

  def __str__(self):
    return self.title
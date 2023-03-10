from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)
    avatar = models.ImageField(blank=True)
    occupation = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    picture = models.ImageField()
    heading = models.CharField(max_length=255)
    content = RichTextField(blank=False, null=False)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(to=Tag, blank=True)
    author = models.ForeignKey(to=Author, on_delete=models.DO_NOTHING, default=1)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.heading

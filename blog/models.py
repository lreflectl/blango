from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation


class Tag(models.Model):
  value = models.TextField(max_length=100)

  def __str__(self):
    return self.value


class Comment(models.Model):
    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # connect comment to multiple (any) models
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    # content_object = GenericForeignKey('content_type', 'object_id')  # default field names can be omitted
    content_object = GenericForeignKey()  # model to comment on (Post, User, etc.)

    def __str__(self):
      return str(self.content[:5]) + '...'


class Post(models.Model):
  author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
  created_at = models.DateTimeField(auto_now_add=True)
  modified_at = models.DateTimeField(auto_now=True)
  published_at = models.DateTimeField(blank=True, null=True)
  title = models.TextField(max_length=100)
  slug = models.SlugField()
  summary = models.TextField(max_length=500)
  content = models.TextField()
  tags = models.ManyToManyField(Tag, related_name='posts')

  comments = GenericRelation(Comment)  # map comments to get them from post

  def __str__(self):
    return self.title

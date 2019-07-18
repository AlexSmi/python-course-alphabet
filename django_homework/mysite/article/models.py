from django.db import models
from account.models import Profile
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation


class Article(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    description = RichTextUploadingField(null=True, blank=True)
    comments = GenericRelation('article.Comments')

    def __str__(self):
        return self.title


class Comments(models.Model):
    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    comments = GenericRelation('article.Comments')

    comment = RichTextUploadingField(null=True, blank=True)
    date = models.DateTimeField(
        'Date of adding a comment', auto_now_add=True, blank=True
    )

    moderation = models.BooleanField('moderation', default=True)

    class Meta:
        # sort comments in chronological order by default
        ordering = ('date',)

    def __str__(self):
        return "{}".format(self.author)

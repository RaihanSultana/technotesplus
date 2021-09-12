from django.db import models
from django.contrib.auth import get_user_model
from django.utils.timesince import timesince as djtimesince

User = get_user_model()


class Tag(models.Model):
    """ Table manages tags """

    name = models.CharField(max_length=255)


class Note(models.Model):
    """ Table manages data of notes """

    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.CharField(max_length=255, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True, related_name='note_tag')
    shared_user = models.ManyToManyField(User, blank=True, related_name="user_shared_notes")

    def timesince(self, now=None):
        """
        Shortcut for the ``django.utils.timesince.timesince`` function of the
        current timestamp.
        """
        return djtimesince(self.created_at, now)

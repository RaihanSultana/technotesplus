from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Note
import random
import string
from django.utils.text import slugify


def random_string_generator(size=5, chars=string.ascii_lowercase+string.digits):
    return "".join(random.choice(chars) for _ in range(size))


# def post_slug_generator(instance, new_slug=None):
#     creator_slug = instance.created_by.slug
#
#     slug = creator_slug + '-permalink-' + random_string_generator()
#     return slug


@receiver(post_save, sender=Note)
def personal_post_slug(sender, instance, created, **kwargs):
    """ Adds slug, once personal post is created """
    if not instance.slug:
        instance.slug = random_string_generator()
        instance.save()

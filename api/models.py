from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
import os


# Create your models here.


class Input(models.Model):
    text = models.TextField()
    audio_file = models.FileField(upload_to='audio_files/')

    def __str__(self):
        return self.id


def _delete_file(path):
    if os.path.isfile(path):
        os.remove(path)


@receiver(post_delete, sender=Input)
def delete_file(sender, instance, *args, **kwargs):
    if instance.audio_file:
        _delete_file(instance.audio_file.path)

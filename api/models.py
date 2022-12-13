from django.db import models

# Create your models here.


class Input(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    audio_file = models.FileField(upload_to='audio_files/')

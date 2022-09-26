from django.db import models


class MediaFolder(models.Model):
    title = models.CharField(max_length=6)
    note = models.CharField(max_length=200)

    class Meta:
        db_table = "media_folders"


class MediaType(models.Model):
    """image, video, audiofile"""
    title = models.CharField(max_length=6)
    note = models.CharField(max_length=200)

    class Meta:
        db_table = "media_types"


class Media(models.Model):
    """media files"""
    type = models.ForeignKey(MediaType, on_delete=models.CASCADE)
    folder = models.ForeignKey(MediaFolder, on_delete=models.CASCADE)

    class Meta:
        db_table = "media"


class MediaTag(models.Model):
    """media files"""
    title = models.CharField(max_length=6)
    note = models.CharField(max_length=200)
    media = models.ManyToManyField(Media)

    class Meta:
        db_table = "media_tags"

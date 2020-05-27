from django.db import models


class Members(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_name = models.CharField(max_length=64)

    class Meta:
        db_table = 'members'
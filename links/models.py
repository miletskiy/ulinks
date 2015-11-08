
from django.db import models

# Create your models here.

class Resource(models.Model):
    """Model for adding resources"""

    class Meta:
        verbose_name = "Resource"
        verbose_name_plural = "Resources"

    title = models.CharField(
        max_length = 256,
        blank = False,
        verbose_name = "Title",
        )

    link = models.URLField(
        max_length = 256,
        blank = False,
        verbose_name = "Link",
        )

    description = models.TextField(
        blank = True,
        verbose_name = "Description",
        )

    time_was_add = models.DateTimeField(
        auto_now_add = True,
        verbose_name= "Time add",
        )

    votes_pros = models.IntegerField(
        verbose_name='Likes for', 
        default=0,
        )

    votes_cons = models.IntegerField(
        verbose_name='Likes against', 
        default=0,
        )

    def __str__(self):
        return self.title

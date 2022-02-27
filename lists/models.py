from django.db import models
from django.db.models.deletion import CASCADE
from core import models as core_models


class List(core_models.TimeStampedModel):

    """List Model Definition"""

    name = models.CharField(max_length=80)
    user = models.OneToOneField("users.User", related_name="lists", on_delete=CASCADE)
    rooms = models.ManyToManyField("rooms.Room", related_name="lists", blank=True)

    def __str__(self):
        return self.name

    def counts_rooms(self):
        return self.rooms.count()

    counts_rooms.short_description = "Number of Rooms"

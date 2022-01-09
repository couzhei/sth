from django.db import models
import uuid

# Create your models here. These are generally our tables

'''Did you know after creating this class you have to run `python manage.py makemigrations`'''
class Project(models.Model):  # we inherit from django's model.Model class
    title = models.CharField(max_length=200)  # a char field like VARCHAR
    # null to true means we can allow for empty string
    description = models.TextField(null=True, blank=True)
    # blank is for django, while null is for the database (confused?)
    # some links are pretty long
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    # a timestamp, whenever the instance is created just insert a timestamp for it
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4,  # this is encoding actually
                          unique=True, primary_key=True, editable=False)  # by default django's models.Model class will create an id for us!!

    def __repr__(self) -> str:
        return self.title

    def __str__(self) -> str: # We use this to have some identifiable representation for our data in our table in the admin panel
        return self.__repr__()
from django.db import models
import uuid

# from django.db.models.expressions import Value # what is this?!?

# Create your models here. These are generally our tables

"""Did you know after creating this class you have to run `python manage.py 
makemigrations`"""


class Project(models.Model):  # we inherit from django's model.Model class
    title = models.CharField(max_length=200)  # a char field like VARCHAR
    # null to true means we can allow for empty string
    description = models.TextField(null=True, blank=True)
    # blank is for django, while null is for the database (confused?)
    # some links are pretty long
    featured_image = models.ImageField(
        null=True, blank=True, default="default.jpg")
    # After some consideration, I figured out that I need this new field
    # beside other fields, it's totally fine. The only thing I should take care
    # of is to run a migration and letting django know that we're using this
    # field. Another funny thing is that when we upload an image into the
    # django for any specific project, we end up having that image right in our 
    # root directory(please go on and try it!), so how are we going to specifiy this
    # problem? check the settings.py
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    # a timestamp, whenever the instance is created just insert a timestamp for it
    created = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(
        "Tag", blank=True
    )  # try unquoting this Tag and this will raise an error due to not defining the Tag variable
    # while by using single quotation marks will make this to search through the document to nail it
    # otherwise we might need to cut and paste the Tag class above this one!
    # note that the blank part means we don't need no education! I mean tag
    id = models.UUIDField(
        default=uuid.uuid4,  # this is encoding actually
        unique=True,
        primary_key=True,
        editable=False,
    )  # by default django's models.Model class will create an id for us!!

    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)

    def __repr__(self) -> str:
        return self.title

    def __str__(
        self,
    ) -> str:  # We use this to have some identifiable representation for our data in our table in the admin panel
        return self.__repr__()


# we're using this to demonstrate the creating process of a relationship between tables


class Review(models.Model):
    VOTE_TYPE = (  # this is for the sake of making reviews rateable!
        ("up", "Up Vote"),
        ("down", "Down Vote"),
    )  # this will be used to create a drop-down list
    # owner =
    # whenever a project is deleted, what are we going to do with the children?
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # models.SET_NULL whenever a project is deleted their reviews will be left alone and
    # the project  field right here will just be set to null
    # while CASCADE will delete all the reviews if a project is deleted
    body = models.TextField(null=True, blank=True)
    value = models.CharField(
        max_length=200, choices=VOTE_TYPE
    )  # choices makes the dropbox
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self) -> str:
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self) -> str:
        return self.name.capitalize()


# don't forget to use makemigrations (why?)
# also don't forget to add them in admin.py (why?)

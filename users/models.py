import email
from operator import mod
from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User
import uuid

# Create your models here.

# creating our first signal
from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
# look near bottom for defining these

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(
        null=True,
        blank=True,
        upload_to="profiles/",
        default="profiles/user-default.png",
    )
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self):
        # # if we create a profile without a user we'regonna get an error
        # return str(self.user.username)
        return str(self.username)


class Skill(models.Model):
    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )

    def __str__(self) -> str:
        return str(self.name)

# Recall that after creating models you have to makemigrations and migrate
# them, then in order to register them into the admin panel, you need
# to go the admin.py under the app's folder and register them

# using decorators
# from django.dispatch import receiver
# # those @methods are from this import

# # reciever
# @receiver(post_save, sender=Profile)
def profileUpdated(sender, instance, created, **kwargs):
    # These are printed out through terminal
    print('Profile saved!')
    print('instance:', instance)
    print('CREATED:', created)
    print('sender:', sender)

# Now we're going to introduce a useful functionality
# We want anytime a user is created, and istead of having
# to submit different forms, immediately and automatically
# a profile is created for them (User vs. Profile???)

def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name + " " + user.last_name
        )

# def deleteUser(sender, instance, **kwargs):
#     print('Deleting user...')

post_save.connect(profileUpdated, sender=Profile)
# post_delete.connect(deleteUser, sender=Profile)

post_save.connect(createProfile, sender=User)
# this means we're gonna fire this off any time
# a user object is created, a profile object is created

# One thing to note is that whenever we delete a user, because
# of the above on_delete=models.CASCADE argument which we passed
# to the One to One relationship with User class, its corresponding
# profile will be deleted. BUT NOT VICE versa! what if we want to
# have the same thing reverse? Well it's one of the convenient reasons
# that you might want to use django signals. This is as follows (commenting 
# above):

def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()

post_delete.connect(deleteUser, sender=Profile)


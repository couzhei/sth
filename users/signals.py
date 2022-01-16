from django.contrib.auth.models import User
from .models import Profile

# creating our first signal
from django.db.models.signals import post_save, pre_save, pre_delete, post_delete
# look near bottom for defining these

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
    print('Profile signal triggered')
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name # + " " + user.last_name
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


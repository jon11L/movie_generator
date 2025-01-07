from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from datetime import datetime



# Create a Profile models here that inherit from the django built-in User.
class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", )
    date_of_birth = models.DateField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='profile_pictures/default_user_pic.png')
    bio = models.TextField(max_length=2000, blank=True)

    # Time stamp
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.user.username


    def render_age(self):
        '''Return user's age.'''
        # calculate the age from date of birth to today.
        if self.date_of_birth:
            print(f"User's date_of_birth: {self.date_of_birth}") # debug
            today = datetime.today().date()
            birthdate = self.date_of_birth
            # check if birthday already happened this year or not.
            age = today.year - birthdate.year
            if (today.month < birthdate.month) or (today.month == birthdate.month and today.day < birthdate.day):
                age -= 1
                return age
        else:
            print("No age found ?")
            return None

# create Profile when a new User is created
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()

post_save.connect(create_profile, sender=User)
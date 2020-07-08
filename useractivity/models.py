from django.db import models

# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=200)
    user_id = models.CharField(max_length=200)
    tz = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name


class ActivityPeriod(models.Model):
    user = models.ForeignKey(
        User, related_name='activityperiods', on_delete=models.CASCADE)
    start_time = models.DateTimeField('log in')
    end_time = models.DateTimeField('log out')

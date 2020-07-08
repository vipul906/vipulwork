from .models import User, ActivityPeriod
from rest_framework import serializers


class ActivityPeriodSerializers(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ['start_time', 'end_time']


class UserSerializers(serializers.ModelSerializer):
    activityperiods = ActivityPeriodSerializers(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", 'user_name', 'user_id', 'tz', 'activityperiods']

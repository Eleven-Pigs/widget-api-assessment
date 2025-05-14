from rest_framework import serializers
from .models import Widget


class WidgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Widget
        fields = "__all__"
        read_only_fields = ("created_at", "updated_at")

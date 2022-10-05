from .models import Files
from rest_framework.serializers import ModelSerializer


class FilesSerializer(ModelSerializer):
    class Meta:
        model = Files
        fields = "__all__"

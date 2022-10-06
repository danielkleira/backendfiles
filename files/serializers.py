from .models import Files, UpFile
from rest_framework.serializers import ModelSerializer


class FilesSerializer(ModelSerializer):
    class Meta:
        model = Files
        fields = "__all__"


class UpFileSerializer(ModelSerializer):
    class Meta:
        model = UpFile
        fields = "__all__"

from django.core.files import File
import base64
from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):
    base64_image = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ('base64_image', 'id')

    def get_base64_image(self, obj):
        f = open(obj.image_file.path, 'rb')
        image = File(f)
        data = base64.b64encode(image.read())
        f.close()
        return data
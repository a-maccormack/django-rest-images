from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .serializers import ImageSerializer
from .models import Image

# Create your views here.
class ImageViewSet(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        file = request.data['file']
        image = Image.objects.create(image_file=file)
        return Response({'message': 'Uploaded', 'image_name': str(image.image_file.name)})
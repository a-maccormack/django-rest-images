from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ImageSerializer
from .models import Image

# Create your views here.
class ImageViewSet(ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        file = request.data['image_file']
        if file == '':
            raise Exception('Uploaded file cannot be blank')
        else:
            image = Image.objects.create(image_file=file)
            return Response({'mesage': 'Uploaded Succesfully', 'image_name': str(image.image_file.name)})

class RetrieveImage(APIView):
    def post(self, request):
        image_id = request.data['image_id']
        image = Image.objects.filter(pk=image_id).first()
        serializer = ImageSerializer(data={'id': image_id, 'image_file': image.image_file})
        if serializer.is_valid(raise_exception=True):
            data = serializer.get_base64_image(image)
            return Response({
                "base_64_image": data,
                "id": image_id
            })
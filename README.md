# django-rest-images
Basic django REST endpoint for image upload. Base64 serializer included for optional implementation

## Usage:
#### To Upload:
Send POST request to `http://127.0.0.1:8000/api/upload/` with image as *file* in body

#### To view Image:
Send GET request to `http://127.0.0.1:8000/media/{image_name}`

## Optional Encoding:
You can modify the code to include the Base64 image encoder located in the `images/serializers.py` file if you prefer to serve images this way (reccomended)

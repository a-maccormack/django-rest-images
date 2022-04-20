# django-rest-images
Basic django REST endpoint for image upload. Base64 serializer included for optional implementation

## Usage:
#### To Upload:
Send POST request to `http://127.0.0.1:8000/api/upload/` with image as *file* in body

#### To view Image:
Send GET request to `http://127.0.0.1:8000/media/{image_name}`

*OR*

Send POST request to `http://127.0.0.1:8000/api/retrieve/` with the following payload:
```json
{
  "image_id": your_image_id
}
```

This endpoint returns a base_64 encoded image that can then be decoded frontend side.

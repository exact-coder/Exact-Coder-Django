from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile

def compress_image(image):
    img = Image.open(image)
    quality = 75
    buffer = BytesIO()
    
    img.save(buffer,format='JPEG',quality=quality)
    buffer.seek(0)

    compressed_image = InMemoryUploadedFile(buffer,None,f'{image.name.split(".")[0]}.jpg','image/jpeg',buffer.tell(),None)

    return compressed_image

from django.db import models

# Create your models here.
def get_image_url(self):
    return '%s%s' %(settings.MEDIA_URL, self.image)
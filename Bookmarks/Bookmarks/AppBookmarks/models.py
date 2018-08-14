from django.db import models
import urllib.request
from django.http import HttpResponse

# Create your models here.

TYPE_CHOICES = (
    (1, ("Un define")),
    (2, ("Tool")),
    (3, ("Aviation")),
    (4, ("Interesting")),
    (5, ("Motorcycle")),
    (6, ("Programation")),
)

# Model for the Bookmark site
class Bookmark(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now_add=True)
    last_check = models.DateTimeField(auto_now_add=True)

    site_link = models.TextField(default='url')
    title = models.TextField(max_length=25, default='Site name')
    description = models.TextField(max_length=144, default= 'Short description')

    type = models.IntegerField(choices=TYPE_CHOICES, default=1)

    def save(self, *args, **kwargs):
        try:
            url = 'http://' + str(self.site_link)
            url_code = 1
            url_code = urllib.request.urlopen(url).getcode()
        except:
            pass


        if url_code == 200:
            super().save(*args, **kwargs)  # Call the "real" save() methode
            print('Valid', self.site_link)

        else:
            print('Invalid', self.site_link)
            return HttpResponse("This website is not valid.")




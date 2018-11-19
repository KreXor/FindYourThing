from django.conf import settings
from django.db import models
from django.utils import timezone

class ActivityType(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(null=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name	

		
class ActivityAddress(models.Model):
    address1 = models.CharField(
        "Address line 1",
        max_length=1024,
    )

    address2 = models.CharField(
        "Address line 2",
        max_length=1024,
        null=True,
		blank=True,
    )

    zip_code = models.CharField(
        "ZIP / Postal code",
        max_length=12,
    )

    city = models.CharField(
        "City",
        max_length=1024,
    )

    country = models.CharField(
        "Country",
        max_length=100,
    )

    long = models.FloatField(
        blank=True, 
        null=True
    )

    lat = models.FloatField(
        blank=True, 
        null=True
    )

    def __str__(self):
        return self.address1
	
    class Meta:
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

		
class Activity(models.Model):

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
	
    title = models.CharField(
        max_length=200
    )
	
    description = models.TextField()
	
    type = models.ForeignKey(
        ActivityType, 
        on_delete=models.CASCADE
    )
	
    created_date = models.DateTimeField(
        default=timezone.now
    )
	
    published_date = models.DateTimeField(
        blank=True, 
        null=True
    )
	
    webpage = models.URLField(
        max_length=200, 
        blank=True, 
        null=True
    )
	
    instagram = models.URLField(
        max_length=200, 
        blank=True,
        null=True
    )
	
    facebook = models.URLField(
        max_length=200, 
        blank=True, 
        null=True
    )
	
    tel = models.CharField(
        max_length=12,
        blank=True,
		null=True
    )

    email = models.EmailField(
        max_length=70,
        blank=True,
		null=True
    )
		
    address = models.ForeignKey(
        ActivityAddress, 
        on_delete=models.CASCADE
    )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

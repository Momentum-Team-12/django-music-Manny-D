from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    # email = models.EmailField(null=True, blank=True)
    # phone_number = models.CharField(max_length=11,
    #                                 validators=[phone_regex],
    #                                 null=True,
    #                                 blank=True)
    # address_1 = models.CharField(max_length=255, null=True, blank=True)
    # address_2 = models.CharField(max_length=255, null=True, blank=True)
    # city = models.CharField(max_length=255, null=True, blank=True)
    # state = USStateField(null=True, blank=True)
    # zip_code = USZipCodeField(null=True, blank=True)

class Note(models.Model):
    album = models.ForeignKey(
        Album, on_delete=models.CASCADE, related_name="notes")
    created_on = models.DateTimeField(auto_now_add=True)
    note = models.TextField(max_length=500)
from django.db import models
from django.contrib.auth.models import User
from chunked_upload.models import ChunkedUpload

class UploadedCSV(ChunkedUpload):
    # Fields corresponding to CSV columns
    name = models.CharField(max_length=255)
    domain = models.URLField()
    year_founded = models.IntegerField(null=True, blank=True)  # Make field optional
    industry = models.CharField(max_length=255)
    size_range = models.CharField(max_length=255)
    locality = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    linkedin_url = models.URLField()
    current_employee_estimate = models.IntegerField(null=True, blank=True) 
    total_employee_estimate = models.IntegerField(null=True, blank=True)

    # Additional fields
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


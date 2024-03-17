from django.urls import path
from dashboard import views

urlpatterns = [
    # Other URL patterns...
    path('upload/', views.upload_csv, name='upload_csv'),
]


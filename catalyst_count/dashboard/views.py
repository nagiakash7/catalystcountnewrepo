from django.shortcuts import render, redirect
from .models import UploadedCSV
from .forms import CSVUploadForm
import pandas as pd
import numpy as np
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UploadedCSVSerializer
from django.db.models import Q

#for the page to be rendered just after login
def profile(request):
    return render(request, 'profile.html')

#for uploading the csv and storing the values in database
def upload_csv(request): 
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            df = pd.read_csv(csv_file)
            
            # Replace 'NaN' values with None
            df = df.replace({np.nan: None})
            
            for index, row in df.iterrows():
                # Check if all required fields are not None before creating the object
                if all(row[field] is not None for field in ['name', 'domain', 'year founded', 'industry', 'size range', 'locality', 'country', 'linkedin url', 'current employee estimate', 'total employee estimate']):
                    uploaded_csv = UploadedCSV.objects.create(
                        name=row['name'],
                        domain=row['domain'],
                        year_founded=row['year founded'],
                        industry=row['industry'],
                        size_range=row['size range'],
                        locality=row['locality'],
                        country=row['country'],
                        linkedin_url=row['linkedin url'],
                        current_employee_estimate=row['current employee estimate'],
                        total_employee_estimate=row['total employee estimate'],
                        uploaded_by=request.user
                    )
            return redirect('profile.html')
    else:
        form = CSVUploadForm()
    return render(request, 'profile.html', {'form': form})



class UploadedCSVCountAPIView(APIView):
    def get(self, request):
        # Get filtering criteria from the request
        city = request.GET.get('city')
        state = request.GET.get('state')
        country = request.GET.get('country')
        industry = request.GET.get('industry')
        year_founded = request.GET.get('year_founded')
        
        # Start with a queryset of all objects
        queryset = UploadedCSV.objects.all()
        
        # Filter queryset based on provided criteria
        if city:
            queryset = queryset.filter(city__icontains=city)
        if state:
            queryset = queryset.filter(state__icontains=state)
        if country:
            queryset = queryset.filter(country__icontains=country)
        if industry:
            queryset = queryset.filter(industry__icontains=industry)
        if year_founded:
            queryset = queryset.filter(year_founded=year_founded)
        
        # Get the count of filtered objects
        count = queryset.count()
        return Response({'count': count})



def query_builder(request):
    return render(request, 'query.html')
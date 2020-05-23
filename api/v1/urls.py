from django.urls import path,include

"""API URLs."""

urlpatterns = [
    path('diseases/',include('diseases.urls')),
]

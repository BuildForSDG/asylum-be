from django.urls import path
from . import views

urlpatterns=[
    path('',views.endpointOverview, name="api-overview"),
    path('disease-list/',views.DiseaseListView.as_view(), name="disease-list"),
    path('disease-detail/<str:pk>/',views.diseaseDetail, name="disease-detail"),
    path('disease-create/', views.diseaseCreate, name='disease-create'),
    path('disease-update/<str:pk>/',views.diseaseUpdate, name='disease-update'),
    path('disease-delete/<str:pk>/',views.diseaseDelete,name='disease-delete')
]
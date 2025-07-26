from django.urls import path
from .views import FormDataListCreateView, FormDataDetailView

urlpatterns = [
    path('form_data/', FormDataListCreateView.as_view()),
    path('form_data/<int:pk>/', FormDataDetailView.as_view()),
]

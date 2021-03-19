
from django.urls import path
from .views import packages,PackageDetailView

from . import views

urlpatterns = [
    path('packages/', packages,name='package'),
    path('packages/<int:pk>/', PackageDetailView.as_view(), name='package-detail'),
    #
    # path('packages/', views.Home,name='home')

]

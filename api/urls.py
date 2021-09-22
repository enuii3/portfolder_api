from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('portfolios', views.PortfolioViewSet)

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('users/', views.ListUserView.as_view(), name='users'),
    path('', include(router.urls)),
]

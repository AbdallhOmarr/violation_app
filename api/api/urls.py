from django.urls import path, include
from rest_framework import routers
from api import views
from .views import CustomAuthToken, CustomLogout

router = routers.DefaultRouter()
router.register(r'departments', views.DepartmentViewSet)
router.register(r'trainees', views.TraineeViewSet)
router.register(r'trainers', views.TrainerViewSet)
router.register(r'violations', views.ViolationViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.register_user, name='register_user'),
    path('token/', CustomAuthToken.as_view(), name='api-token'),  # URL for obtaining a token
    path('logout/', CustomLogout.as_view(), name='api-logout'),  # URL for logging out
]

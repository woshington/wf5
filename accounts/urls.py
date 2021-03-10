from rest_framework import routers
from . import views
from django.urls import path, include

app_name = 'accounts'

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet, basename="user")
urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = router.urls

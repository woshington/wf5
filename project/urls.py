from rest_framework import routers
from . import views
from django.urls import path, include

app_name = 'project'

router = routers.DefaultRouter()
router.register(r'project', views.ProjectViewSet, basename="project")
router.register(r'management', views.ManagementViewSet, basename="management")
urlpatterns = [
    path('', include(router.urls)),
]

# urlpatterns = router.urls

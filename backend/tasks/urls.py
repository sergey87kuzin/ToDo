from django.urls import include, path
from rest_framework.routers import SimpleRouter

from . import views

router_v1 = SimpleRouter()
router_v1.register('users', views.UserViewSet, basename='users')
router_v1.register('tasks', views.TaskViewSet, basename='task')
api_v1_patterns = [
    path('', include(router_v1.urls))
]

urlpatterns = [
    path('v1/', include(api_v1_patterns)),
]

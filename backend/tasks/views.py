from rest_framework import viewsets
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated

from .models import Task, User
from .permissions import IsAuthorPermission
from .serializers import TaskSerializer, UserSerializer


class UserViewSet(viewsets.GenericViewSet, CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, IsAuthorPermission)

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

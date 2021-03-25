from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action

from .serializers import QuestionSerializer, AnswerSerializer, UserSerializer, StepsSerializer
from .models import Question, Answer, User, Steps
from .filters import UserFilter


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_class = UserFilter


class StepsViewSet(viewsets.ModelViewSet):
    serializer_class = StepsSerializer
    queryset = Steps.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class CreateUserView(viewsets.ViewSet):

    def create_token(self):
    user =
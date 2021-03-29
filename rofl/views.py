from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.decorators import action
import jwt

from .serializers import QuestionSerializer, AnswerSerializer, UserSerializer, StepsSerializer, FacultySerializer
from .models import Question, Answer, User, Steps, Faculty
from .filters import UserFilter
from .result import Result


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

    def create(self, request):
        data = request.data
        token = jwt.decode(data['user'], "ikss", algorithms=["HS256"])
        data['user'] = token['id']
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            user = User.objects.get(id=data['user'])
            question = Question.objects.get(id=data['question'])
            answer = Answer.objects.get(id=data['answer'])
            step = Steps.objects.create(user=user,
                                        question=question,
                                        answer=answer)
            step.save()
            return Response(self.get_serializer(step).data, status=201)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        data = request.data
        token = jwt.decode(data['user'], "ikss", algorithms=["HS256"])
        data['user'] = token['id']
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            user = User.objects.get(id=data['user'])
            question = Question.objects.get(id=data['question'])
            answer = Answer.objects.get(id=data['answer'])
            step = Steps.objects.create(user=user,
                                        question=question,
                                        answer=answer)
            step.save()
            return Response(self.get_serializer(step).data, status=201)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


class CreateUserView(viewsets.ViewSet):

    @staticmethod
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def create(self, request):
        ip = self.get_client_ip(request)
        user = User.objects.create(ip=ip)
        user.save()
        encoded_jwt = jwt.encode({"id": user.id}, "ikss", algorithm="HS256")
        return Response({'user': encoded_jwt})


class UserResView(viewsets.ViewSet):

    def list(self, request):
        res = {}
        user = self.request.query_params.get('user')
        token = jwt.decode(user, "ikss", algorithms=["HS256"])
        user_id = token['id']
        res = Result(user_id=user_id)
        top_fac = max(res.get_res(), key=res.get_res().get)
        res = Faculty.objects.get(name=top_fac)

        return Response(FacultySerializer(res).data)

    # def list(self, request):
    #     faculty_id = self.request.query_params.get('faculty_id')
    #     news = News.objects
    #     if faculty_id:
    #         faculty_id = self.split_args(faculty_id)
    #         news = news.filter(news_f__in=faculty_id)
    #
    #     serializer = self.serializer_class(news.all(), many=True)
    #     return Response(serializer.data)

from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r"question", views.QuestionViewSet)
router.register(r"answer", views.AnswerViewSet)
router.register(r"user", views.UserViewSet)
router.register(r"steps", views.StepsViewSet)
router.register(r"create_user", views.CreateUserView, basename='User')
router.register(r"get_res", views.UserResView, basename='Steps')


urlpatterns = [
    path('', include(router.urls)),
]



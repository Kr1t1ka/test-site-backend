from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r"question", views.QuestionViewSet)
router.register(r"answer", views.AnswerViewSet)
router.register(r"user", views.UserViewSet)
router.register(r"steps", views.StepsViewSet)
# router.register(r"^users/$", views.UserViewSet().test)

urlpatterns = [
    path('', include(router.urls)),
    # path("user/<str:token>/", views.UserViewSet.test()),
]

# urlpatterns = [
#     path("faculties/programs/", views.DirectionViewSet.as_view({'get': 'list',
#                                                                 'post': 'create'})),
#     path("faculties/programs/<int:pk>/", views.DirectionViewSet.as_view({'get': 'retrieve',
#                                                                          'put': 'update',
#                                                                          'delete': 'destroy'})),
#     path("faculties/programs/minimal-scores/", views.EgeScoreViewSet.as_view({'get': 'list',
#                                                                               'post':


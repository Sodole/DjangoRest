from django.urls import path, include
from djangorest import views
from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r"Snippet",views.SnippetViewSet)
urlpatterns = [
    path("", include(router.urls)),
    path("model", views.models2.as_view()),
    path("model/<str:pk>", views.models1.as_view()),
    path("model2/<int:pk>", views.models3.as_view())
]

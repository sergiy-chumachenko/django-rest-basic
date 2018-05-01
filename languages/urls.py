from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('languages', views.LanguageView)

app_name = 'languages'
urlpatterns = [
    path('', include(router.urls))
]

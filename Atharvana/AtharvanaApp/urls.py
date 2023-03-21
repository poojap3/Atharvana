from django.urls import path, include
from AtharvanaApp.views import *
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from . import views
from AtharvanaApp.views import *




app_name = 'AtharvanaApp'


router = routers.DefaultRouter()


urlpatterns = [
    path('', include(router.urls)),
    # path('signup/', SignupApi.as_view()),
    path('login/', LoginView.as_view(), name="LOGIN"),
    path('taskvalue/', TaskValueAPIView.as_view(), name="VALUE"),
    path('datewisevalue/', ValueDateAPIView.as_view(), name="DATEWISEVALUE"),
    ]

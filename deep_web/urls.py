from django.urls import path
from deep_web.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name='home')
]
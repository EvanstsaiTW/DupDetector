from django.urls import path, re_path
from . import views
from backend.views import IndexTemplateView;
urlpatterns = [
    path('home/', views.home, name = 'author-home'),
    path('api/random_data', views.random_data),
    path('about/', views.about, name = 'author -about'),
    re_path(r'^.*$', IndexTemplateView.as_view()),
]

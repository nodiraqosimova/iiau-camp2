from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.news_detail, name='news_detail')
]

from django.urls import path

from posts import views

urlpatterns = [
    path('', views.PostsList.as_view(), name='posts-list'),
    path('<int:pk>', views.PostDetail.as_view(), name='post-detail')
]

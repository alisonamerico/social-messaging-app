from django.urls import path

from . import views

urlpatterns = [
    path('', views.MsgListView.as_view(), name='home'),
    path('post/<int:pk>/', views.MsgDetailView.as_view(), name = 'post_detail'),
]

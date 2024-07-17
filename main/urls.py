from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about", views.about, name="about"),
    path("create", views.create, name="create"),
    path('update/<int:tasks_id>/', views.update, name='update'),
    path('delete/<int:tasks_id>/', views.delete, name='delete'),
    path('add_comment/', views.add_comment, name='add_comment'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/<int:task_id>/add_comment/', views.add_comment, name='add_comment'),

]
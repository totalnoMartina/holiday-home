from django.urls import path
from . import views


urlpatterns = [
    path('add_feed/', views.add_feedback, name='add_feed'),
    path('feedback/', views.see_feedbacks, name='feedback'),
]
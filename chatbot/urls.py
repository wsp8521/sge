from django.urls import path
from chatbot import views


urlpatterns = [
 path('chat/', views.chatbot, name='chatbot'),
 path('agent/', views.agent_ia, name='agent'),
]

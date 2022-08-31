from django.urls import path
from api import views

urlpatterns = [
    path('stuinfo/<int:pk>', views.student_details.as_view()),
    path('stuinfo/', views.student_list.as_view()),
]
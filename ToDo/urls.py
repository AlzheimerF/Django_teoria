from django.urls import path
from .views import registration_view, create_exercise_view

urlpatterns = [
    path('register/', registration_view),
    path('register/create_exercise/', create_exercise_view)
]

from django.urls import path
from .views import SensorsView, RetvieweSensorView, CreateMeasurement

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', RetvieweSensorView.as_view()),
    path('measurements/', CreateMeasurement.as_view())
]

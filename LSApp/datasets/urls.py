from django.urls import path

from datasets.views import GetFightDataset, GetBorderDataset

urlpatterns = [
    path("fights", GetFightDataset.as_view()),
    path("crossings", GetBorderDataset.as_view()),
]

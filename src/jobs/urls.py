from django.urls import path

from jobs.views import JobDetailView

urlpatterns = [
    path("<int:pk>/", JobDetailView.as_view(), name="job"),
]

from django.urls import path

from author.views import AthorView

urlpatterns = [
    path("", AthorView.as_view(), name="author"),
]

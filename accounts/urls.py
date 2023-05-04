from django.urls import path
from . import views

urlpatterns = [
    path("related/", views.MyView.as_view(), name="get_related_people"),
]

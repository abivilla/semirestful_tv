from django.urls import path
from . import views

urlpatterns = [
    path('shows', views.shows),
    path('shows/new', views.add_show),
    path('shows_desc/<id>', views.shows_desc),
    path('delete/<int:id>', views.delete),
    path('shows/<int:id>/edit', views.edit)
]
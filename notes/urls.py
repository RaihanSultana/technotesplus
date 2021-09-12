from django.urls import path, re_path
from django.views.generic import TemplateView
from .views import NotesCreateView, NotesListView, NotesDetailView, notes_delete_view

app_name = "notes"
urlpatterns = [
    path('notes/create/', NotesCreateView.as_view(), name='notes-create'),
    path('notes/list/', NotesListView.as_view(), name='notes-list'),
    path('notes/detail/<int:pk>', NotesDetailView.as_view(), name='notes-detail'),
    path('notes/delete/<int:pk>', notes_delete_view, name='notes-delete'),
]

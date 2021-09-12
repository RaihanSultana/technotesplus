from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.db.models import Q
from .models import Tag, Note

User = get_user_model()


class NotesCreateView(LoginRequiredMixin, View):
    template_name = 'notes-create.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        content = request.POST.get('content')
        tags = request.POST.getlist('tags')
        tag_list = tags[0].split(",")
        # create Note obj
        note_obj = Note.objects.create(title=title, content=content, created_by=request.user)

        # add tags
        for tag in tag_list:
            tag, created = Tag.objects.get_or_create(name=tag)
            note_obj.tags.add(tag)
            note_obj.save()

        messages.info(request, "New note have been created")

        return redirect('/')


class NotesListView(LoginRequiredMixin, ListView):
    model = Note
    template_name = 'notes-list.html'
    login_url = 'login'
    paginate_by = 10
    context_object_name = "notes"

    def get_queryset(self):
        # user can see only his own note or notes that is shared with him
        notes = Note.objects.filter(Q(created_by=self.request.user) | Q(shared_user=self.request.user))
        return notes


class NotesDetailView(LoginRequiredMixin, View):
    template_name = 'notes-detail.html'

    def get(self, request, *args, **kwargs):
        note = Note.objects.get(pk=kwargs['pk'])
        # filter only non admin
        users = User.objects.filter(is_staff=False)
        context = {
            'note': note,
            'users': users,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        content = request.POST.get('content')

        note_obj = Note.objects.get(pk=kwargs['pk'])
        note_obj.title = title
        note_obj.content = content
        note_obj.save()
        return redirect('notes:notes-list')


def notes_delete_view(request, pk):
    notes_obj = Note.objects.get(pk=pk)
    notes_obj.delete()

    return redirect('notes:notes-list')


def notes_share_view(request):
    note_id = request.POST.get('note_id')
    note_obj = Note.objects.get(pk=note_id)
    users = request.POST.getlist('users[]')
    for user in users:
        user_obj = User.objects.get(pk=int(user))
        note_obj.shared_user.add(user_obj)
        note_obj.save()

    return redirect('notes:notes-list')
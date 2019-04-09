from django.shortcuts import render
from .forms import NoteForm
from task1.models import *
from collections import Counter


def task1(request):
    form = NoteForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(form.cleaned_data)
        data = form.cleaned_data

        new_form = form.save()

    return render(request, 'make-note.html', locals())


def read_notes(request):
    note = Note.objects.order_by("-unique_words")
    return render(request, 'watch-notes.html', locals())

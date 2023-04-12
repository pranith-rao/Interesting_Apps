import random

from django.shortcuts import render
from django import forms
from . import util
from markdown2 import Markdown


markdowner = Markdown()

class Create(forms.Form):
    title = forms.CharField()
    textarea = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 100,'placeholder':"Enter content here..."}))

class Search(forms.Form):
    item = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search Encyclopedia'}))

class Edit(forms.Form):
    textarea = forms.CharField(widget=forms.Textarea(attrs={'rows': 10, 'cols': 100}))

def index(request):
    context = {}
    entries = util.list_entries()
    searched = []
    if request.method == "POST":
        form = Search(request.POST)
        if form.is_valid():
            item = form.cleaned_data["item"]
            for i in entries:
                if item in entries:
                    page = util.get_entry(item)
                    page_converted = markdowner.convert(page)
                    context = {
                        'page': page_converted,
                        'title': item,
                        'form': Search()
                    }
                if item.lower() in i.lower(): 
                    searched.append(i)
                    context = {
                        'searched': searched, 
                        'form': Search()
                    }
            return render(request, "encyclopedia/search.html", context)
        else:
            return render(request, "encyclopedia/index.html", {"form": form})
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries(), "form":Search()
        })

def create(request):
    if request.method == "POST":
        form = Create(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            textarea = form.cleaned_data["textarea"]
            entries = util.list_entries()
            if title in entries:
                return render(request, "encyclopedia/error.html", {"form": Search(), "message": "Page already exists"})
            else:
                util.save_entry(title,textarea)
                page = util.get_entry(title)
                page_converted = markdowner.convert(page)
                context = {
                    'form': Search(),
                    'page': page_converted,
                    'title': title
                }
                return render(request, "encyclopedia/entry.html", context)
    return render(request, "encyclopedia/create.html",{
        'create': Create(),"form":Search()
    })

def random_page(request):
    if request.method == 'GET':
        entries = util.list_entries()
        num = random.randint(0, len(entries) - 1)
        page_random = entries[num]
        page = util.get_entry(page_random)
        page_converted = markdowner.convert(page)
        context = {
            'form': Search(),
            'page': page_converted,
            'title': page_random
        }
        return render(request, "encyclopedia/entry.html", context)

def entry(request, title):
    entries = util.list_entries()
    if title in entries:
        page = util.get_entry(title)
        page_converted = markdowner.convert(page) 
        context = {
            'page': page_converted,
            'title': title,
            'form': Search()
        }
        return render(request, "encyclopedia/entry.html", context)
    else:
        return render(request, "encyclopedia/error.html", {"message": "The requested page was not found.", "form":Search()})

def edit(request, title):
    if request.method == 'GET':
        page = util.get_entry(title)
        context = {
            'form': Search(),
            'edit': Edit(initial={'textarea': page}),
            'title': title
        }
        return render(request, "encyclopedia/edit.html", context)
    else:
        form = Edit(request.POST) 
        if form.is_valid():
            textarea = form.cleaned_data["textarea"]
            util.save_entry(title,textarea)
            page = util.get_entry(title)
            page_converted = markdowner.convert(page)
            context = {
                'form': Search(),
                'page': page_converted,
                'title': title
            }
            return render(request, "encyclopedia/entry.html", context)




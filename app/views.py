from app import models

from django.shortcuts import render

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView

# Create your views here.

def about(request):
    return render(request, 'about.html')

class CreateBlog(CreateView):
    model = models.Blog
    template_name = 'index.html'
    success_url = reverse_lazy('pages')
    fields = ['titulo','subtitulo','cuerpo','autor','fecha','imagen']

class ListBlog(ListView):
    model = models.Blog
    context_object_name = 'blogs'
    template_name = 'pages.html'

class DetailBlog(DetailView):
    model = models.Blog
    template_name = 'detail.html'

class UpdateBlog(UpdateView):
    model = models.Blog
    template_name = 'edit.html'
    success_url = reverse_lazy('pages')
    fields = ['titulo','subtitulo','cuerpo']

class DeleteBlog(DeleteView):
    model = models.Blog
    template_name = 'delete.html'
    success_url = reverse_lazy('pages')

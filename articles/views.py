from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Articles


# Create your views here.
class ArticlesListView(ListView):
    model = Articles
    template_name = 'article_list.html'


class ArticlesDetailView(DetailView):
    model = Articles
    template_name = 'article_detail.html'


class ArticlesCreateView(CreateView):
    model = Articles
    fields = ('title', 'body', 'author',)
    template_name = 'article_new.html'


class ArticlesUpdateView(UpdateView):
    model = Articles
    fields = ('title', 'body',)
    template_name = 'article_edit.html'


class ArticlesDeleteView(DeleteView):
    model = Articles
    template_name = 'article_delete.html'
    success_url = reverse_lazy('articles_list')

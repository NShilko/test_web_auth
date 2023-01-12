from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .filters import PostFilter
from .forms import NewsForm, ArticlesForm
from datetime import datetime
from django.contrib.auth.mixins import PermissionRequiredMixin


class NewsList(ListView):
    model = Post
    queryset = Post.objects.filter(kind='NEWS').order_by('-date')
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now().strftime("%d.%m.%Y %H:%M")
        context['is_kind'] = 'Новости'
        context['filterset'] = self.filterset
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs


class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'publication.add_post'
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'


class NewsUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'publication.change_post'
    form_class = NewsForm
    model = Post
    template_name = 'news_edit.html'


class NewsDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')


class NewsDetail(DetailView):
    model = Post
    template_name = 'publ.html'
    context_object_name = 'publ'


class PublList(ListView):
    model = Post
    queryset = Post.objects.filter(kind='PUBL').order_by('-date')
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now().strftime("%d.%m.%Y %H:%M")
        context['is_kind'] = 'Статьи'
        context['filterset'] = self.filterset
        return context


class ArticlesCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'publication.add_post'
    form_class = ArticlesForm
    model = Post
    template_name = 'news_edit.html'


class ArticlesUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'publication.change_post'
    form_class = ArticlesForm
    model = Post
    template_name = 'news_edit.html'


class ArticlesDelete(DeleteView):
    model = Post
    template_name = 'news_delete.html'
    success_url = reverse_lazy('articles_list')


class ArticlesDetail(DetailView):
    model = Post
    template_name = 'articles.html'
    context_object_name = 'publ'

class NewsSearch(ListView):
    model = Post
    queryset = Post.objects.filter(kind='NEWS').order_by('-date')
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now().strftime("%d.%m.%Y %H:%M")
        context['is_kind'] = 'Поиск по новостям'
        context['filterset'] = self.filterset
        return context
